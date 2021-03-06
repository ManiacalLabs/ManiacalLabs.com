---
author: maniacal labs
date: 2014-11-19 13:15:51+00:00
draft: false
title: 'Weekend Project: POVStick'
type: post
url: /2014/11/19/weekend-project-povstick/
categories:
- Cool Stuff
- Making Of
- Projects
- Tutorial
---

To showcase how much the [AllPixel](https://www.kickstarter.com/projects/1101128588/allpixel-usb-interface-for-all-your-led-needs/) and BiblioPixel can simplify your projects, we wanted to put together a fun project that really highlighted their versatility. So we decided to build a persistence of vision light painter, or POVStick as we keep calling it.

The POVStick consists of 2 meters of 48 LED/m LPD8806 strips, for a total of 96 pixels vertical resolution. This is controlled by an AllPixel connected to a Raspberry Pi B+ with a USB WiFi module. Finally, this is all powered by a 16Ah lithium-ion battery pack. It's 2.1A  per port output was more than enough to run the LEDs and Pi for quite some time.

{{< gallery dir="/wp-content/galleries/2014-11-19-weekend-project-povstick/0/" />}}

Next is the special that makes it all work... the software. Fortunately, BiblioPixel is really easy to enhance and extend, so I came up with the LEDPOV class. This builds on top of [LEDMatrix](https://github.com/ManiacalLabs/bibliopixel/wiki/LEDMatrix) but in stead of displaying the full matrix, breaks the image up into vertical columns and displays those one at a time, split over the given total frame time.




    from bibliopixel.led import *
    import bibliopixel.image as img
    from bibliopixel.drivers.serial_driver import *
    import bibliopixel.gamma as gamma

    #Takes a matrix and displays it as individual columns over time
    class LEDPOV(LEDMatrix):

        def __init__(self, driver, povHeight, width, rotation = MatrixRotation.ROTATE_0, vert_flip = False):
            self.numLEDs = povHeight * width

            super(LEDPOV, self).__init__(driver, width, povHeight, None, rotation, vert_flip, False)

        #This is the magic. Overriding the normal update() method
        #It will automatically break up the frame into columns spread over frameTime (ms)
        def update(self, frameTime = None):
            if frameTime:
                self._frameTotalTime = frameTime

            sleep = None
            if self._frameTotalTime:
                sleep = (self._frameTotalTime - self._frameGenTime) / self.width

            width = self.width
            for h in range(width):
                start = time.time() * 1000.0

                buf = [item for sublist in [self.buffer[(width*i*3)+(h*3):(width*i*3)+(h*3)+(3)] for i in range(self.height)] for item in sublist]
                self.driver.update(buf)
                sendTime = (time.time() * 1000.0) - start
                if sleep:
                    time.sleep(max(0, (sleep - sendTime) / 1000.0))

    #convert 6 character hex colors to RGB tuple
    def hex2rgb(hex):
        """Helper for converting RGB and RGBA hex values to Color"""
        hex = hex.strip('#')
        if len(hex) == 6:
            split = (hex[0:2],hex[2:4],hex[4:6])
        else:
            raise ValueError('Must pass in either a 6 character hex value!')

        r, g, b = [int(x, 16) for x in split]

        return (r, g, b)

    argv = sys.argv
    argc = len(argv)

    file = ""
    bright = 255
    col_time = 50
    bgcolor = (0,0,0)

    #load in command line args
    if argc > 1:
        file = argv[1]
    else:
        print "Must specifiy an input file!"
        sys.exit(2)

    #get brightness value
    if argc > 2:
        bright = int(x=argv[2])

    #col_time is time to display each vertical line for, in ms
    if argc > 3:
        col_time = int(argv[3])

    #bgcolor is the color that will be used on transparent pixels
    if argc > 4:
        bgcolor = hex2rgb(argv[4])

    #open the file so it is not loaded each time through
    i = img.Image.open(file)

    img_width = i.size[0]
    totalFrameTime = img_width * col_time

    print "Image Display Time: {0:.1f}s".format(totalFrameTime/1000.0)

    driver = DriverSerial(LEDTYPE.LPD8806, num = 96, c_order=ChannelOrder.BRG, SPISpeed=16, gamma=gamma.LPD8806)

    #automatically configure matrix width to image width.
    #change povHeight to match your setup
    led = LEDPOV(driver, povHeight = 96, width = img_width, rotation=MatrixRotation.ROTATE_0, vert_flip=True)
    led.setMasterBrightness(bright)

    img.showImage(led, imageObj = i, bgcolor=bgcolor)

    try:
        while True:
            led.update(frameTime=totalFrameTime)
    except KeyboardInterrupt:
        led.all_off()
        led.update()





Usage is as follows:




    python LEDPOV.py image_file brightness column_time background_color
    brightness: 0-255
    column_time: time (ms) to display each vertical column of the image
    background_color: hex color value to use for transparent pixels, otherwise black (#000000)




After a little more testing, LEDPOV will be added to the main BiblioPixel code so that it will be more easily available to all.

To use, just run the script with the desired image and set your camera to do a long exposure for slightly longer than it will take the image to display. To help with this, the script outputs the total display time of each image. You will likely need to play around with ISO and aperture settings before getting it exactly right and, of course, doing this at night will provide the best results. It is also best to add a little blank lead-in on each image so that you know when to start moving. When the lights go out have someone hit the shutter and start walking at a steady pace. If you get it right, you should get some awesome pictures like these:

{{< gallery dir="/wp-content/galleries/2014-11-19-weekend-project-povstick/1/" />}}

To keep things fully mobile, we controlled the POV script from an SSH session running on an Android tablet. We highly recommend [JuiceSSH](https://play.google.com/store/apps/details?id=com.sonelli.juicessh&hl=en) and [Hacker's Keyboard](https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard&hl=en) for a great mobile SSH terminal experience.

If you like this and want to make your own, check out our Kickstarter for the [AllPixel](https://www.kickstarter.com/projects/1101128588/allpixel-usb-interface-for-all-your-led-needs/)!

