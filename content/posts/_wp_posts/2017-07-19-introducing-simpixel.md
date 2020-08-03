---
author: adam
date: 2017-07-19 14:38:36+00:00
draft: false
title: Introducing SimPixel
type: post
url: /2017/07/19/introducing-simpixel/
---

[BiblioPixel](/bibliopixel) supports a wide array of hardware through its driver system but one of the biggest annoyances was always having to actually _have_ that hardware in order to test your code. That's why, very early on, we added the visualizer to the library which worked well for small displays, but was never great with high pixel counts or fast framerates. For over two years we've wanted to replace it with something better but could never settle on something that would have high performance and run on every operating system that BiblioPixel already does.

But at the 2015 [SparkCon](http://sparkcon.com), here in Raleigh, we met [Michael Clayton](https://palebluepixel.org/) who I actually now work with at Red Hat. At SparkCon, Michael showed off his awesome [Kimotion](https://palebluepixel.org/projects/kimotion/) project which shows high performance, WebGL-based, animations in a browser using data captured from an XBox Kinect sensor via a Python server. This was clearly perfect for replacing the visualizer in BiblioPixel but the idea remained just an idea for another year while other things were worked on.

But after some further discussion with Michael we decided that, mainly because he is a WebGL wizard, we could probably knock out a new visualizer in a day. So we met up one Saturday and, in about 9 hours, threw together something that put the original visualizer to extreme shame. We call it [SimPixel](https://github.com/ManiacalLabs/SimPixel).

{{< youtube KIZA-ze8ODQ >}}

This baby will do buttery smooth 60 frames per second with thousands of pixels without skipping a beat. We actually use it to stress test BiblioPixel!

Being that it's written in JavaScript and WebGL, all you need to run it is any relatively modern web browser. BiblioPixel communicates with it over super fast websockets which actually means you can even connect to another system on the same network for the pixel data.  Check out [Michael's blog post](https://palebluepixel.org/2017/03/10/meet-simpixel/) for more information about how SimPixel works. In general, we use it locally on the same machine. This is what enables the [`bibliopixel demo`](https://github.com/ManiacalLabs/bibliopixel/wiki/Demo-Command) command in the new BiblioPixel v3.0 to show off the functionality of BiblioPixel without any required hardware. It's so easy even, that you can go from nothing installed to seeing awesome pixels in 16 seconds!

{{< youtube CXOJoKK4nzQ >}}

And because SimPixel is web-based there's not even anything to install. In the video above, BibliPixel simply opens a browser to [SimPixel.io](http://simpixel.io) which is all you need. If you do, however, want to see the code (it's open source, of course!) or run it locally you can find all the details at the [SimPixel GitHub repo](https://github.com/ManiacalLabs/SimPixel).

Because of SimPixel, you can easily see BiblioPixel in action with absolutely zero code.

```
pip install bibliopixel
bibliopixel demo
```

That's it! Install BiblioPixel and then run the demo! http://SimPixel.io will automatically launch and connect to the BiblioPixel animations that are now running. SimPixel is also fully supported in BiblioPixel's new "[Projects](https://github.com/ManiacalLabs/bibliopixel/wiki/Projects)" feature, meaning you can create your own setup with nothing but some basic configuration.

Stay tuned as we'll be highlighting more of BiblioPixel's great new features soon :)
