---
author: maniacal labs
date: 2015-05-04 15:36:30+00:00
draft: false
title: BiblioPixel v1.2 is Here!
type: post
url: /2015/05/04/bibliopixel-v1-2-is-here/
---

Thousands of people have already downloaded [BiblioPixel](/bibliopixel) (for use with and without the [AllPixel](/AllPixel)) and we've received a ton of awesome feedback. Over the last couple months, we've taken that feedback and worked in a bunch of bug fixes and some cool new features.

Check out the details below, but if you want to jump right to it and get the latest version, you can do one of these two options:




  * If you installed originally with pip, run this command:
`sudo pip install bibliopixel --upgrade`
  * If you prefer to install manually, grab the [v1.2 zip file](https://github.com/ManiacalLabs/bibliopixel/archive/v1.2.1.zip), unzip it to a local directory and run:
` sudo python setup.py install`




In both cases, sudo is not needed if you are running Windows and this will work even if you have never installed it before. If upgrading, just be sure to use the same method you previously used.

Now that you've got it, here's what's new!




  * **[LEDCircle](https://github.com/ManiacalLabs/bibliopixel/wiki/LEDCircle)**: Inspired by the new AdaFruit APA102 Disk display, we've made working with circular displays easy! Check out all the details over at our [APA102 Disk review](/2015/05/04/review-code-adafruit-dotstar-disk/).
  * **[LEDPOV](https://github.com/ManiacalLabs/bibliopixel/wiki/LEDPOV)**: We've talked about it before, but the code for making things like our [POVStick](/2014/11/19/weekend-project-povstick/) project is now built right into BiblioPixel.
  * **[DriverAPA102](https://github.com/ManiacalLabs/bibliopixel/wiki/DriverAPA102)**: This new SPI-based driver allows you to run APA102 (DotStar) strips right from the SPI pins on devices like the Raspberry Pi and Beagle Bone Black!
  * **Threaded Animations**: Never wait around for your animations again! The latest code supports the _[threaded](https://github.com/ManiacalLabs/bibliopixel/wiki/Animations#runamt--1-fpsnone-sleepnone-max_steps--0-untilcomplete--false-max_cycles--0-threaded--false-jointhread--false)_ parameter which will make that animation run on a separate background thread, allowing you to continue doing other tasks in your main script or application. Great for web controlled projects!
  * **Many Bug Fixes and Improvements**: While not the exhaustive list, we have:


    * Improved DriverSerial device detection
    * Improved DriverNetwork reliability
    * Cleaned up the logic of many classes and methods to make them more robust and better at handling any issues.
    * Fixed many, many bugs.



That's all for now. We hope you love the new features!
