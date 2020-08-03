---
author: maniacal labs
date: 2015-01-21 14:00:40+00:00
draft: false
title: Multi-Driver Demo with BiblioPixel
type: post
url: /2015/01/21/multi-driver-demo-with-bibliopixel/
categories:
- AllPixel
- BiblioPixel
- Kickstarter
---

Last time on the Maniacal Labs Blog... we told you about the awesome [new multiple driver](/2015/01/18/exciting-updates/) support added to [BiblioPixel](http://github.com/maniacallabs/bibliopixel) in the latest version. Well, check out the video below to see the proof!




{{< youtube jg0gHXLDid4 >}}



All the code from the video is below. More details are on the [BiblioPixel Wiki](https://github.com/ManiacalLabs/bibliopixel/wiki). And be sure to visit the [Maniacal Labs Forum](http://forum.maniacallabs.com/) to discuss usage or ask questions. Happy making!



{{< highlight py >}}
#Load driver for your hardware, visualizer just for example
import time
import bibliopixel.log as log
log.setLogLevel(log.DEBUG)

useSerial = False

if useSerial:
    from bibliopixel.drivers.serial_driver import *
    #Use DeviceIDManager.py to set or view your device IDs
    driverA = DriverSerial(LEDTYPE.NEOPIXEL, 8*8, deviceID = 0)
    driverB = DriverSerial(LEDTYPE.NEOPIXEL, 8*8, deviceID = 1)
    driverC = DriverSerial(LEDTYPE.NEOPIXEL, 16*8, deviceID = 2)
else:
    from bibliopixel.drivers.visualizer import *
    #When using multiple visualizers you must specify distinct ports
    driverA = DriverVisualizer(width=8, height=8, port=1610, pixelSize = 30, stayTop=True)
    driverB = DriverVisualizer(width=8, height=8, port=1611, pixelSize = 30, stayTop=True)
    driverC = DriverVisualizer(width=16, height=8, port=1612, pixelSize = 30, stayTop=True)


#load the LEDMatrix class
from bibliopixel.led import *
import bibliopixel.colors as colors

#change rotation and vert_flip as needed by your display
build = MultiMapBuilder()
build.addRow(mapGen(8,8, serpentine=(not useSerial)), mapGen(8,8, serpentine=(not useSerial)))
build.addRow(mapGen(16,8, serpentine=(not useSerial)))
#in the AllPixel version of the demo we used WS2812 matrices that were not serpentine, but the visualizer
#If using multiple different displays, use whatever it is for that display

#create LEDMatrix and load in generated map
#threaded updates are fastest when using multiple drivers
led = LEDMatrix(driver = [driverA, driverB, driverC], threadedUpdate = True, width = 16, height = 16, coordMap=build.map)

try:
    from matrix_animations import *

    anim = Bloom(led, dir=True)
    anim.run(amt=6, fps = 30)

except KeyboardInterrupt:
    pass

led.all_off()
led.update()
#since updates are threaded, give them time to finish before exiting the app
time.sleep(2)

{{< / highlight >}}
