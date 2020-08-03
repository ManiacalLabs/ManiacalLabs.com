---
author: adam
date: 2016-06-28 12:32:38+00:00
draft: false
title: 'Jumbo1K: 32x32 LED Networked Display'
type: post
url: /2016/06/28/jumbo1k-32x32-led-networked-display/
categories:
- 3D Printing
- BiblioPixel
- Cool Stuff
- Making Of
- Tutorial
---

Over two years ago, I bought this [awesome display panel](https://www.adafruit.com/products/1484):
{{< figure src="/wp-content/uploads/2016/06/1484-02.jpg" caption="1484-02" >}}


It's a 7.5" square, 32x32 resolution, 6mm LED spacing, panel that would normally be used for digital signage. Though it is a "dumb" display that requires CPU intensive multiplexing (it's supposed to be driven by an FPGA or ASIC), with the right tools it can be way easier to use than building, ahem, [other](/colossus) [types](/WyoManiacalDisplay) of displays ;) I have covered this exact panel a [few](/2015/01/23/adafruit-matrix-hat-support-for-bibliopixel/) [other](/2015/02/14/adafruit-matrix-hat-raspberry-pi-2-speed-test/) [times](/2015/06/01/bibliopixel-controlling-a-jumbotron/), but after a couple years of sitting in my LED storage it was _time_ to finally make it something awesome.

To jump straight to the good stuff, check out the build video below, or continue on after the break for the full details.

{{< youtube J78uUcMCJ8c >}}

<!-- more -->



### Case



The core of this particular display is, in a way, the case. Ever LED display I've made up to this point has used digital LED strips or strings, which are great but also not meant for particularly high pixel density. This makes even low resolution displays [pretty large](/colossus), and as such, I've usually resorted to constructing the structure of the displays out of wood. But at only 7.5" square, with pixels only 6mm apart, it was just the right size to design a 3D printed case that would be printable within the build volume of our MakerBot Replicator 2. Almost, anyways... each half had to be separated into two parts that slot together and are secured with screws, so this made a great excuse to also learn how to design multi piece printed parts.
{{< figure src="/wp-content/uploads/2016/06/CaseFront.png" caption="CaseFront" >}}


The front of the case is, as mentioned, printed in to halves which are identical and fit together when rotated 180 degrees to one another. There is both an opening and mount screw holes for the panel itself, as well as a slot into which the 8" square frosted acrylic slides. It's actually designed such that the only way to get the acrylic in is with the case front in two halves, so the design limitation worked out nicely in this case as it holds the acrylic in with nothing more than the slot itself.
{{< figure src="/wp-content/uploads/2016/06/CaseBackBottom.png" caption="CaseBackBottom" >}}

{{< figure src="/wp-content/uploads/2016/06/CaseBackTop.png" caption="CaseBackTop" >}}


The back of the case is _not_ in identical halves as the bottom holds not only all of the connection ports but the Raspberry Pi 3 that drives the whole thing. The top, however, is entirely plain and merely exists to round out the back and cover everything. But like the front the back pieces have the same rotational symmetry that allows them to fit together.

The front and back then screw together using ten M3x30mm screws that thread all the way through the back and into the front. Speaking of screws, for the sake of simplicity the case is also designed such that all fastening screws and completely self threading. This is achieved by making the screw hole slightly smaller than the threads. For example, for an M3 screw I typically make a 2.7-2.9mm hole. Smaller if the hole will be printed horizontally and larger if vertically. This is because on printers like the Rep2, the dimensional accuracy in the X/Y planes (parallel to the plate) is not as good as the Z-axis accuracy. In fact, it's affected by the Z-axis layer height with the smaller the layer height, the more dimensionally accurate it will be on the X/Y plane. Just be sure to take this into account when designing. The point here is that this allows adding no extra hardware and not needing a nut on the other side of each hole. The downside is the durability of the hole. Re-threading a screw runs the risk of damaging the threads such that the screw no longer holds, as does over torquing the screw. Make this mistake and you will strip the threads making it useless. Note in the above video that I started all the screws with an electric driver but always finish them by hand. Last, because of this torque issue the holding force will be fairly low, which can be fixed with more print shells (4 or more) and coarser threads, but for this project no real pressure was needed, just enough to hold it all together, so M3-0.7 screws sufficed.

Another important design piece of the case is that instead of trying to design in openings for whatever various connection couplers I usually find on amazon I decided it would be cleaner this time around to use [keystone jacks](https://en.wikipedia.org/wiki/Keystone_module). The beauty of these is that they employ a completely standardized opening and securing mechanism regardless of the actually connection being used. So as you see in the design, three of the four ports are all identical. Sadly, I was unable to find a 2.1mm barrel port keystone for the power, but three out of four ain't bad :) But by using keystones, not only does it not matter where you get the keystone jacks from, but you can put whatever connection you want in any opening. In this case, I used Ethernet, HDMI, and USB with the last two mainly for setup of the Pi without having to open the case. See the parts list below for the exact components I used, including the barrel port that does fit the hole in the case.

As to make this and future designs easier I made the keystone jack receiver as a separate [design file](https://github.com/ManiacalLabs/Jumbo1K/blob/master/KeystonePort.stl). This way, for anything you want a keystone jack receiver in, just place the part in the design and merge it with your main solid.



### Control



As covered [previously](/2015/06/01/bibliopixel-controlling-a-jumbotron/), these LED panels can be controlled via [BiblioPixel](/bibliopixel) with a Teensy 3 and the [SmartMatrix Shield](http://docs.pixelmatix.com/SmartMatrix/shieldref.html). It's also possible to control directly via the Raspberry Pi (without the Teensy in between) as [also covered before](/2015/01/23/adafruit-matrix-hat-support-for-bibliopixel/), but the downside I've found to this is the solution, while functional, is basically bit-banging the GPIO pins and crazy CPU intensive, leaving little CPU resources for actually running BiblioPixel. The beauty of using the Teensy and SmartMatrix however is that it can use some wizardry known as [DMA](https://en.wikipedia.org/wiki/Direct_memory_access) allowing it to drive the panel multiplexing at high speed with almost no CPU usage. This means that not only can you drive more pixels (up to 32x128 with the latest SmartMatrix library) but push frames quicker by allowing the Teensy CPU more time to handle new data requests.

Previous articles I've written on this topic used a modified version of the AllPixel firmware that pulled in the SmartMatrix module of the [FastLED](http://fastled.io) library. This was done because we already used FastLED so the change was trivial. This time, however, I've rewritten most of the driver firmware and removed FastLED entirely. Not because I dislike it now or anything, but because the very latest of the SmartMatrix library is not yet supported by FastLED. Certainly a downside, but the upside here is that this latest SmartMatrix, as mentioned, has support for **many** more pixels as well as a plethora of other great improvements. Also, FastLED was chosen because it allowed supporting multiple LED types in the same firmware. But in this case, that was no longer necessary... so off it went in favor of what turned out to be much simpler. Right now I have not extended the firmware to easily support other than a 32x32 display but that will certainly be coming in the very near future. All the code and usage details can be found in the [BiblioPixelSmartMatrix](https://github.com/ManiacalLabs/bibliopixelSmartMatrix) repository.

With the driver hardware and firmware complete all that left was something easily contained in the case to control the whole thing. When I first got this display, that was to be a Pi B+ but not only was the Pi 2 released in the meantime, but the Pi 3. I could've used a Pi 2, which I already had, but why not use an excuse to finally try out the Pi 3. Even better, it's integrated WiFi made it _much_ easier to have the only required cable on the display be power, making for a super clean display.



### Parts



Finally, to keep you from searching all over for what exactly I used, here is the full parts list:

<table cellpadding="0" cellspacing="0" class="waffle" >

<tr >
Qty
Item
Source
</tr>

<tbody >
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >P6 32x32 LED Panel
</td>

<td class="s3 softmerge" dir="ltr" >


[https://www.adafruit.com/products/1484](https://www.adafruit.com/products/1484)

</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >8A@5V Supply
</td>

<td class="s3 softmerge" dir="ltr" >


[https://www.amazon.com/gp/product/B00MHV7576/](https://www.amazon.com/gp/product/B00MHV7576/)

</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >1' microUSB Cable
</td>

<td class="s2" dir="ltr" >Generic
</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >3' HDMI Cable
</td>

<td class="s3 softmerge" dir="ltr" >


[https://www.amazon.com/gp/product/B014I8SP4W/](https://www.amazon.com/gp/product/B014I8SP4W/)

</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >1.5' USB B Cable
</td>

<td class="s3 softmerge" dir="ltr" >


[https://www.amazon.com/gp/product/B009GUVZOK/](https://www.amazon.com/gp/product/B009GUVZOK/)

</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >1' Ethernet cable
</td>

<td class="s2" dir="ltr" >Generic (custom)
</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >Teensy 3.2
</td>

<td class="s2" dir="ltr" >Various (Adafruit, PJRC, OSHPark)
</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >SmartMatrix Shield
</td>

<td class="s3 softmerge" dir="ltr" >


[http://docs.pixelmatix.com/SmartMatrix/shieldref.html](http://docs.pixelmatix.com/SmartMatrix/shieldref.html)

</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >Raspberry Pi 3
</td>

<td class="s3 softmerge" dir="ltr" >


[https://www.amazon.com/gp/product/B01CD5VC92/](https://www.amazon.com/gp/product/B01CD5VC92/)

</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >8GB microSD
</td>

<td class="s2" dir="ltr" >Generic
</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >HDMI Keystone
</td>

<td class="s3 softmerge" dir="ltr" >


[https://www.amazon.com/gp/product/B005ZAOA5G/](https://www.amazon.com/gp/product/B005ZAOA5G/)

</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >USB Keystone
</td>

<td class="s3 softmerge" dir="ltr" >


[https://www.amazon.com/gp/product/B00W2CWDLS/](https://www.amazon.com/gp/product/B00W2CWDLS/)

</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >Ethernet Keystone
</td>

<td class="s3 softmerge" dir="ltr" >


[https://www.amazon.com/gp/product/B016O9SXCM/](https://www.amazon.com/gp/product/B016O9SXCM/)

</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >Barrel Jack
</td>

<td class="s3 softmerge" dir="ltr" >


[https://www.amazon.com/gp/product/B00OE6A1J6/](https://www.amazon.com/gp/product/B00OE6A1J6/)

</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >1
</td>

<td class="s2" dir="ltr" >8"x8"x1/8" Frosted Acrylic
</td>

<td class="s4" dir="ltr" >[http://www.acrylite-shop.com](http://www.acrylite-shop.com)
</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >4
</td>

<td class="s2" dir="ltr" >M2.5x6mm (Raspberry Pi)
</td>

<td class="s2" dir="ltr" >Generic
</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >10
</td>

<td class="s2 softmerge" dir="ltr" >


M3x30mm (Case front to back)

</td>

<td class="s2" dir="ltr" >Generic
</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >8
</td>

<td class="s2" dir="ltr" >M3x20mm (Case half tabs)
</td>

<td class="s2" dir="ltr" >Generic
</td>
</tr>
<tr style="height: 20px;" >

<td class="s1" dir="ltr" >2
</td>

<td class="s2" dir="ltr" >M3x12mm (Panel to case)
</td>

<td class="s2" dir="ltr" >Generic
</td>
</tr>
</tbody>
</table>

One last side note: The case is designed with six mounting holes for the panel itself. But as you can see, I only used two of them. Honestly, this is because I screwed up the design slightly and the side holes don't perfectly align. Instead of redesigning and reprinting, I realized that using all six was complete overkill and two screws was more than enough.

If you have any questions or make your own, be sure to let us know!
