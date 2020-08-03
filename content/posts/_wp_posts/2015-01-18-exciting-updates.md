---
author: maniacal labs
date: 2015-01-18 16:11:46+00:00
draft: false
title: Exciting Updates!
type: post
url: /2015/01/18/exciting-updates/
categories:
- AllPixel
- Announcements
- BiblioPixel
- Kickstarter
---

It's been a little over a month since the Kickstarter for our [AllPixel](/AllPixel) finished and things are progressing nicely. We've certainly learned a lot about communicating with an overseas manufacturer and designing a product for mass production. Nothing a few tiny tweaks couldn't fix. Our goal has always been to deliver the best possible product. The final boards should be going into production within the next week or two!

During the campaign, we set a stretch goal of providing multiple driver support to [BiblioPixel](https://github.com/ManiacalLabs/bibliopixel). Sadly, we didn't actually meet that goal. But we couldn't just let it go... version 1.1.x of BiblioPixel is now available with full support for multiple drivers! Now, you can run a display with as many AllPixels as your computer can handle the data for! No longer is your display limited to the 700 pixel limit of the AllPixel... wire in another and BiblioPixel will magically make both act as one! For more details, check out the [BiblioPixel Wiki](https://github.com/ManiacalLabs/bibliopixel/wiki/Multiple-Driver-Support).

In the effort to provide multiple driver support, we also added threaded display updates. This allows all the updates to the display to happen on background threads (one per driver). The details are all a bit technical, but what this means is higher animation frame-rates, especially when using multiple drivers. For example, if you have four AllPixels connected, they will all update the display at the same time... _while_ the next frame is being generated! With these two new features, we hope to really make BiblioPixel even more of an animation power house.

As a little side bonus, we also added a [new driver](https://github.com/ManiacalLabs/bibliopixel/wiki/DriverHue) to BiblioPixel that allows control of the Philips Hue LED lights. They aren't nearly as fast as the usual LED lights your used to using with BiblioPixel as they are meant for home lighting, but this will allow super easy control of Hue lights directly from BiblioPixel.

That's all for now! Stay tuned.
