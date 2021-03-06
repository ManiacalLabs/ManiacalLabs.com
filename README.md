# ManiacalLabs.com is generated by Hugo from this source

Below is really just for the Maniacal Labs team. But hey, you might learn some things. If you'd like to contribute or just want to talk to us, checkout our [contact page](https://maniacallabs.com/contact/)

# Setup / Requirements

Install Hugo v0.44+ using the [installation instructions](https://gohugo.io/getting-started/installing).
Basically, go to the [Releases Page](https://github.com/gohugoio/hugo/releases), grab the version for your system, unzip, and install to your system path. Note: While some linux distributions have packages in their native managers, many of these are very old. Please grab the latest.

# Creating New Content

All content lives under the `content` directory in the root of this repo.

Typically you would use `hugo new <path>` to add new content, but for the sake of consistency, this process has been wrapped in a little python script. (The fact that a golang program is wrapped in python is not lost on me.)

In the root of this repo is `new.py` which can be invoked as follows:

```
python new.py post "Awesome New Post"
hugo new posts/2018/7/New_Website/index.md
~/dev/ManiacalLabs.com/content/posts/2018/7/New_Website/index.md created

New doc created @ ~/dev/ManiacalLabs.com/content/posts/2018/7/New_Website/index.md
Static resources may be included in the same directory
and referenced as a relative path.
```

As you can see above the script also automatically creates a `<year>/<month>` sub directory in an attempt to keep the directory structure uncluttered.

Note that `post` is not the only type option. You may also use `buildlog`, `product`, and `project` which will automatically place the new content into the appropriate sub-type directory.

If you want to simply create a root level page, just use `hugo new <page_name>`

Note: `new.py` will automatically populate the author field based on `git config user.name`

# Content Front-Matter
All Hugo docs have "front-matter" at the top of the markdown file that will look something like this:

```
---
title: Awesome Post
date: 2018-07-13T18:35:08-04:00
draft: false
tags: []
categories: []
# slug:
# description:
# author:
---
```

The contents of this front-matter is just standard YAML syntax. Regardless of the generated path for the content, the data here entirely determines the final path. For example, the URL of the post will become `/:year/:month/:day/:title/` based on the `date` and `title` values in the front-matter.

The `slug` option will override the final URL instead of what's described above. It's probably best not to use this unless you really know what you are doing.

`tags` and `categories` are optional but encouraged and can be a list of anything.

**The most important thing to note** is that all new content will default to `draft: true` which means that they *will not* be rendered out the the live website if commited to the master branch. Leaving this as true until ready to go live with the post is encouraged.  Please see [Local Hugo Server](#local-hugo-server) below for details on using drafts.

# Scheduling Posts

You can now setup posts to be published in the future. By default `new.py` sets the `date` field in the content front-matter to be the time of file creation. This will cause the post to go public as soon as it hits master. Instead you may change the `date` field to something like:

`2020-03-05T00:00:00`

This will not go live until March 5, 2020 at midnight.

**PLEASE NOTE**: You should always set the time to 00:00:00 otherwise the post may not go live until the next day, due to how Travis is scheduled.

Travis will rebuild master once per day, and any posts dated before the time of that build will then be pushed.

# Content Resources

Because `new.py` automatically creates an `index.md` file inside a directory instead of a single file without a parent directory you may include resources such as images directly inside that directory alongside the post. For example:

```
\posts
  \2018
    \7
      \new_post
        index.md
        main_image.png
```

Now, you could include that image in the post with just `![main](main_image.png)` instead of require a full or root-relative path.

# Static Resources

For resources which must remain at an easily known location but don't need to live with the post itself, use the `static` directory at he root of this repo. Anything under that will follow the same path structure from the root of the site. So, `./static/images/logo.png` will be available at http://maniacallabs.com/images/logo.png

# Images

Note: ALL images should be no larger that 960x960 unless you have a really good reason for it!

There are a couple of ways to add images to a page, the simplest being the standard markdown image syntax:

`![Image AltText](image.png)`

The path can be anywhere in the site but it's easiest ot include in the document directory (assuming you used `new.py`). This standard markdown format will display the image centered on the page and not have a link or any special qualities. If you want images to be a little more special use one of the options below.

The [`figure` shortcode](https://gohugo.io/content-management/shortcodes/#figure) has far more display options, detailed on the [Hugo docs site](https://gohugo.io/content-management/shortcodes/#figure).
Beyond the Hugo `figure` basics, this site is also configured to automatically use [Photoswipe](http://photoswipe.com/) to display the image in nice full-screen gallery mode. At the most basic, `figure` can be used like:

`{{< figure src="image.png" caption="Adam Haile" >}}`

To go even further the `gallery` shortcode is available, provided by [Hugo Easy Gallery](https://www.liwen.id.au/heg/)

At its simplest, the `gallery` shortcode will take a directory of images and automatically create a pretty gallery using Photoswipe.

`{{< gallery dir="/images/galleries/my_gallery_12/" />}}`

Unfortunately, this must use directories under `static` so the path above would actually be `/static/images/galleries/my_gallery_12/` locally. You may optionally specify each image directly with a `figure` shortcode like this:

```
{{< gallery >}}
    {{< figure link="sydney-harbour.jpg" caption="Sydney Harbour" >}}
    {{< figure link="cc_jeepers.jpg" caption="Capital Chorus" >}}
    {{< figure link="test-setup.jpg" caption="Arduino test setup" >}}
{{< /gallery >}}
```

If done that way, the images may be stored alongside the content doc. For more usage details see the [Hugo Easy Gallery docs](https://www.liwen.id.au/heg/).

The `gallery` shortode also supports automatically finding and using smaller thumbnail images for the gallery. See the gallery docs linked above for more.

# Header Images

Maybe there's a better way to do this, but I've not found it yet... The theme is setup to take the first image for apost and use it in the sumary on the various post lists. However, this is *not* the first image referenced in the `index.md` file of the post. It's the first `image resource` as Hugo defines it. Which basically means the first image file in that directory.

Therefore, to keep a sensible standards, all posts should have an image named `!header.<png|jpg>`. The `!` will make sure it's the "first" image seen by Hugo. But if you want it to show up on the actual post page, you still have to include it in the document. That is not required.

# Local Hugo Server

The other reason to have Hugo installed locally is that you can use it as a development server while creating new content. From the repo root, simply run the provided script which wraps everything you need:

`./gohugo`

This will run the hugo development server in verbose mode (best for hunting down render errors) and render draft and future dated documents (-D -F).

The site can then be previewed at http://localhost:1313/

Hugo is supposed to automatically rerender and reload the site in the browser on detected file changes. This typically works fine for basic content additions and updates. But it doesn't seem to work so well when updating site layout or styling. If making such changes, it's best to stop and restart the server after changes.
