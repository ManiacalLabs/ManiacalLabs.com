---
author: adam
date: 2017-06-26 12:20:06+00:00
draft: false
title: BiblioPixel v3.0 Is Here!
type: post
url: /2017/06/26/bibliopixel-v3-0-is-here/
---
{{< figure src="/wp-content/uploads/2017/06/bibliopixel-1.png" caption="" >}}


It's amazing to think that nearly 5 years ago, before Maniacal Labs even, I released [RPi-LPD8806](https://github.com/adammhaile/RPi-LPD8806), which would eventually become [BiblioPixel](/bibliopixel), our pure Python pixel animation framework. Back then it was only for the Raspberry Pi and only for LPD8806 LEDs... and I barely knew Python at the time!

Over the years, it has morphed and grown into a massively capable framework with support for so much more than that original library. But no year in BiblioPixel's history has been more significant than this last year. I'd always had future plans for it but mainly updates happened as necessary to support other projects I was working on. The most significant, of course, being the [AllPixel](/AllPixel). But for more than a year now, [Tom Ritchford](http://tom.ritchford.com/) (who actually first contacted me because of RPi-LPD8806 way back in 2013) has taken the vision of BiblioPixel to a whole new level. And if you'll believe it, this is just the start.

So, who's Tom? In his own words:

_[Tom Ritchford](http://tom.ritchford.com/) has been writing computer programs for a living since 1979. His alter ego [Tom Swirly](http://tom.swirly.com/) does music, lights and sound with computers for fun. He currently lives in Amsterdam where he is writing a book._

After thousands of emails and hundreds of commits, BiblioPixel 3.0 is faster, cleaner, stronger, happier and in every conceivable way better than it's predecessor. You will go from zero to blinking lights in under a minute!

What's new? Just to name a few highlights...




  * Full Python 3.4+ support! (In fact we dropped Python 2 support)
  * Near complete core rewrite that's faster than ever!
  * Run BiblioPixel with nothing more than a config file, zero code!
  * SimPixel, our all-new WebGL based visualizer. Get started with no hardware at all!
  * Tight integration with BiblioPixelAnimations, our repository of pre-made animations.


Even with all this, it's still about 90% compatible with all your old code and only requires [minimal modifications](https://github.com/ManiacalLabs/bibliopixel/wiki/Porting-from-2.x-to-3.x).

Get started and [install now](https://github.com/ManiacalLabs/bibliopixel/wiki/Installation)!



#### Footnotes






  * Talk about blast from the past, here's a demo video I posted of RPi-LPD8806 from October, 2012:
{{< youtube g5upsgqASiY >}}
  * [Original post](https://web.archive.org/web/20121028064857/http://www.adamhaile.net:80/projects/raspberrypi-led-strip-control/) (on a defunct website) I made about the RPi-LPD8806 library which is how Tom got involved.
  * So, what does nearly 5 years of work on BiblioPixel look like? Thanks to [gource](http://gource.io/) we get this pretty video:
{{< youtube NOIAom7oCqY >}}

