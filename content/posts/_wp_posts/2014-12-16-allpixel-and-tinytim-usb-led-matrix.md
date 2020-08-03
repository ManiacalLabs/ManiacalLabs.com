---
author: dan
date: 2014-12-16 13:00:53+00:00
draft: false
title: More Fun With the AllPixel and TinyTiM
type: post
url: /2014/12/16/allpixel-and-tinytim-usb-led-matrix/
categories:
- Cool Stuff
- Kickstarter
- Projects
---

As a follow-on to our [previous article](/2014/11/24/sharing-among-the-community/) on the TiM and TinyTiM displays from [WyoLum](http://wyolum.com), I wanted to demonstrate some of the flexibility of the [AllPixel](/AllPixel) in terms of how well it can pair with already existing products. The TinyTim is an as-yet-unreleased product from WyoLum, but it will be dropping soon. It's really a slick board, consisting of 64 WS2812 LEDs arranged in an 8x8 grid. There are plenty of connections on the back of the PCB to easily wire together multiple displays, in either parallel or serial data transfer configurations. For this build, just one was used, and it was turned into a stand-alone USB LED Matrix.

{{< figure src="/wp-content/uploads/2014/12/TinyTim_RasPiAPlus.jpg" caption="TinyTim_RasPiAPlus" >}}

<!-- more -->

The innards of the device are, of course, a TinyTiM and an AllPixel. The enclosure is a cheap shadow box-style frame I picked up from a local crafts store for a few bucks. Behind the glass front is a sheet of regular printer paper. This worked very well as a diffuser, even on the rather low max brightness setting used in the code.  Taped to the sheet of paper is the TinyTiM/AllPixel "assembly." Sorry I don't have a picture of that, but I used clear packing tape on the four corners of the TinyTiM to attach it to the paper. There's some cardboard and a paperboard backing that hold the paper/assembly pressed against the glass.

{{< figure src="/wp-content/uploads/2014/12/TinyTim_AllPixelMounted.jpg" caption="TinyTim_AllPixelMounted" >}}

One of the optional features of the AllPixel is the ability to add a protection diode, which enables the connected LEDs to receive power directly from the USB port. Obviously, you are limited to a few hundred milliamps of current. This translates to a small number of LEDs running at full brightness or a slightly larger number running at lower brightness. I've opted for the later on this build, with the max brightness fixed in code to 1/4 power (64 out of 255).

I first used an external power supply to test the animations so I could get a precise reading of the current drawn. It peaked at about 300mA for a second or two. Everything else was well below that. The AllPixel itself only draws a few milliamps when running, so I was well within the limits for a standard 500mA USB port. Once I was happy with the current draw, I removed the external supply, installed the protection diode to enable USB power, and closed the box up.

{{< figure src="/wp-content/uploads/2014/12/TinyTim_Rear.jpg" caption="TinyTim_Rear" >}}

{{< figure src="/wp-content/uploads/2014/12/TinyTim_Front.jpg" caption="TinyTim_Front" >}}

So basically what your left with is a slick-looking 8x8 USB LED matrix. Using the [BiblioPixel](https://github.com/ManiacalLabs/bibliopixel) Python library, which directly supports the AllPixel, coding up animations is not to complex, even for a non-Software Engineer such as myself. Since it's Python-based, it can run on a wide variety of platforms. I happened to pick up a Raspberry Pi A+ not too long ago, and I figured I'd give it a whirl driving the display.

{{< figure src="/wp-content/uploads/2014/12/TinyTim_Final.jpg" caption="TinyTim_Final" >}}
Of course, it works a treat. No muss, no fuss, easy to set up and take down for other applications.

Many thanks to the folks at [WyoLum](http://wyolum.com) for letting us test drive the TinyTiM. I'll definitely be picking up a few more once it goes on sale to the public.

If you're interested in the [AllPixel](/AllPixel), our Kickstarter has ended, but to be notified as soon as it is available for purchase, follow us on [Twitter](https://twitter.com/ManiacalLabs) and sign up for our newsletter.

Thanks for reading!

-Dan
