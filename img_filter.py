import glob
import os

with open('C:\dev\exitwp-for-hugo\matches.txt', 'r') as m:
    matches = ['.' + l.strip().replace('\\', '/') for l in m.readlines()]

all_files = glob.glob('./wp-content/**/*.*', recursive=True)
all_files = [a.replace('\\', '/') for a in all_files]
print(len(all_files))
deletions = []
for f in all_files:
    # print(f)
    if f not in matches:
        deletions.append(f)
print(len(deletions))


for d in deletions:
    print(d)
    os.remove(d)

# print(os.getcwd())
# print(len(deletions))
