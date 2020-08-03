---
author: adam
date: 2017-09-27 17:39:39+00:00
draft: false
title: Infinity Mirror
type: post
url: /2017/09/27/infinity-mirror/
---

When it comes to LED related builds there's one right of passage that we somehow let fall by the wayside... An Infinity Mirror.

{{< youtube z1lSGxYMoW4 >}}

We have a ridiculously long backlog of things we'd like to build and very often they stay on the list until one day when an idea strikes or a perfect core component presents itself. In this case it was finding a good deal on 144 pixel/m APA102 LED strips that were initially intended for use with another project. The eureka moment here was when the realization was made that a ring of 120 pixels would make for a fantastic clock (see end of video above) because, well, we try to make a clock out of everything. Why is 120 pixels perfect? Because 120 is divisible by 60, 24, and 12 evenly, making it absolutely ideal for a clock. And what better way to show off our latest product, the [PiPixel](/pipixel)?!
{{< figure src="/wp-content/uploads/2017/09/Mirror.jpg" caption="" >}}

{{< figure src="/wp-content/uploads/2017/09/pipixel-1.jpg" caption="" >}}


<!-- more -->

For those unaware, an infinity mirror is created by sandwiching lights between a full mirror (on the back) and half, a.k.a. two-way, mirror (on the front). The light from the pixels reflect back and forth between the back and front mirrors and eventually out through the front mirror, creating the effect you can see in the video above.

Most DIY infinity mirror builds you may see use square or rectangular mirrors because, as we found, finding a round half mirror is a major pain. Half mirrors are already sort of a specialty item and most suppliers that will custom cut will only do rectangular shapes. But after emailing several potential suppliers to ask if they could do a round cut, [Tap Plastics](https://www.tapplastics.com/) finally came to the rescue by agreeing to do the cut. So we ordered a 1/4" full mirror and 3/16" half mirror cut to 12" diameter circles.

The main reason a 12" diameter circle was chosen was that we measured the total circle created by the 120 LED strip to be roughly 10.5", and we needed to have enough material on the frame for the sake of structure. The round frame was modeled in Fusion 360 in 4 pieces that slotted and epoxied together and were small enough to be printed on our Replicator 2 printer. The inner diameter of this frame was also modeled with an concave channel which allowed hot gluing the LED strip to the inside edge of the frame while still remaining flush with the 10.5" inner diameter. One of the 4 frame pieces also has an elliptical hole in it to allow the power and data wires from the LED strip to pass out of the frame and be connected to the controller.

The only other major components bringing the whole thing together are the four "locks" that sandwich the two acrylic mirror pieces around the frame, and bolt into an M3 nut that is inlaid to the inside of the frame ring. This will allow easy disassembly of the entire mirror if ever required.

You can view and download all the component files via the [Fusion 360 project](http://a360.co/2ytYnjY).

One other item that the above CAD design includes is a stand for the mirror. It neatly holds the whole assembly upright, provides a clean and hidden pass-through for the wires, as well as a convenient mount for a Pi Zero or full size Raspberry Pi to drive the whole thing. We've of course chose to use our new [PiPixel](/pipixel) LED hookup Pi HAT to get this up and running in no time.

This of course means that driving animations on the mirror is super easy using our latest and greatest [BiblioPixel](/bibliopixel) features. The quickest way being to run:

```
bibliopixel run https://github.com/adammhaile/bibliopixelProjects/blob/master/SparkCon2017/Infinity.json
```

If you look directly at that JSON file you will see that some manipulation of the ring layout had to be done in the `layout` section. We used `rotation` to rotate the orientation of the ring 180 degrees because the ring starts on the bottom, so that the wires could be hidden in the stand. Also, the `reverse_angle` option was used because the LEDs were installed into the ring frame counter-clockwise instead of clockwise. This was merely an oversight during construction :P
