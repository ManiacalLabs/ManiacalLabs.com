---
author: adam
date: 2017-08-14 17:51:25+00:00
draft: false
title: Introducing the PiPixel - Raspberry Pi & Digital LEDs Simplified
type: post
url: /2017/08/14/introducing-the-pipixel-raspberry-pi-digital-leds-simplified/
---
{{< figure src="/wp-content/uploads/2017/08/Simplex.png" caption="" >}}


It would be an understatement that we here at Maniacal Labs loves all things LED. With our first major product we brought you the AllPixel, allowing super simple LED control from anything with a USB port and Python. At the time one of the major reasons we went that direction was that the things we wanted to do were too big (like [Colossus](/Colossus)) for something like the original Raspberry Pi to handle. But a lot has changed in the intervening years and we found ourselves building more and more with a Raspberry Pi at the heart, running the show.

But connecting LEDs to the Pi and providing power was never as simple as it was with the [AllPixel](/AllPixel). We'd have some jumper wires hanging off the GPIO header manually wiring power into the LEDs. So, in a fit of "spend a bunch of time to save a bunch of time" we designed the [PiPixel](/pipixel) kit.
{{< figure src="/wp-content/uploads/2017/08/FullyAssembled.jpg" caption="" >}}


It provides all you need to drive LEDs directly off your Raspberry Pi with as little hassle as possible: Power input, signal level shifting, and data/power output. Data output is selectable and available on SPI, GPIO 13, and GPIO 18. Via these data outputs and our [BiblioPixel](/bibliopixel) LED animation framework, it can handle the control of the following LED types:




  * APA102 ("DotStar")
  * SK9822
  * WS2801
  * LPD8806
  * WS281x ("NeoPixel")


As you may note, this is not as many protocols as the [AllPixel](/AllPixel), some just cannot be handled by the Raspberry Pi, but this does cover most of the popular chipsets.

The PiPixel will also work with any other library that utilizes the SPI port (/dev/spi0.0), GPIO 13, or GPIO 18. But, of course, we highly recommend that you check out our feature rich [BiblioPixel](/bibliopixel) library.

Best of all, we designed the PiPixel to be super cheap and you can pick one up on [Tindie](https://www.tindie.com/products/10276/) for a mere $8.50.

Of course, as with everything else we do, the PiPixel is open source and you can checkout all the design files over on [GitHub](https://github.com/ManiacalLabs/pipixel).

Assembly and usage documentation is available at the above linked [GitHub](https://github.com/ManiacalLabs/pipixel) repo, but be sure to check out the video below for a full walkthrough.

{{< youtube wtbaeGrnpRE >}}

For questions, comments, or support, head over to our [Maniacal Labs Users Google Group](https://groups.google.com/forum/#!forum/maniacal-labs-users).
