import glob
import sys
import re
import csv
import os
import errno
import shutil


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


csv.field_size_limit(sys.maxsize)

posts_csv = sys.argv[1]

posts = {}
with open(posts_csv, 'rt', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        posts[row[0]] = row[18]

all_files = glob.glob('./*.md')


def find_gallery(md):
    with open(md, encoding="utf8") as md_f:
        content = md_f.read()
        return [content[m.start(): m.end()] for m in re.finditer('\[gallery.*\]', content)]


def parse_gallery(gal):
    gal = gal.replace('[gallery ', '').replace(']', '')
    fields = gal.split(' ')
    result = None
    for field in fields:
        sub = field.split('=')
        if sub[0] == 'ids':
            result = list(filter(None, sub[1].replace('"', '').split(',')))
    return result


def parse_images(ids):
    result = []
    for i in ids:
        if i in posts:
            result.append(posts[i].replace('http://maniacallabs.com', '').replace("'", ""))
        else:
            print('ID {} invalid'.format(i))
    return result


def copy_images(imgs, dest):
    out_dir = '../../../static/wp-content/galleries/' + dest + '/'
    src_base = 'C:/dev/ml_data'

    mkdir_p(out_dir)
    for i in imgs:
        print('{} -> {}'.format(src_base + i, out_dir))
        try:
            shutil.copy(src_base + i, out_dir)
        except Exception as e:
            print(e)

    return '/wp-content/galleries/' + dest + '/'


for f in all_files:
    g_list = find_gallery(f)
    if g_list:
        print(f)
        with open(f, 'r', encoding="utf8") as out:
            cont = out.read()

        c = 0
        for g in g_list:
            ids = parse_gallery(g)
            imgs = parse_images(ids)
            # TODO Dest needs counter
            gal_dir = copy_images(imgs, f.replace('.\\', '').replace('.md', '/{}'.format(c)))

            cont = cont.replace(g, '{{< gallery dir="' + gal_dir + '" />}}')

            c += 1

        cont += ('\n' + '')
        with open(f, 'w') as out:
            out.write(cont)

        print('')
