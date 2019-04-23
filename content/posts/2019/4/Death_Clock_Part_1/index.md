---
title: Death Clock - Part 1
date: 2019-04-24T12:00:00-04:00
draft: false
tags: []
categories: []
weight: 20
# slug:
# description:
author: Adam Haile
---

I have a morbid sense of humor. And I'm also a firm believer in not wasting any time in life; choosing to focus making the most of the time I have, creating new and interesting things. But even I need a reminder sometimes, and that's where the "Death Clock" comes in.

No, not the cartoon metal band. What I'm talking about is a giant clock counting down until the day I'll (likely, based on life expectancy averages) die. Like I said; morbid sense of humor. But I choose to see it as a daily reminder that life is short and there's no sense in wasting any of it.

This project really started from a fascination with 7-segment displays and wanting to make a really large display. I knew I wanted one but not why at first... then the countdown idea struck me and it's stuck ever since. Sure, giant 7-segment displays have been made many times before but that's just an opportunity to do mine different.

For one, basically all that I've ever seen use the standard strip LEDs that we all know and love. One of the best I've seen was made by [John Park @ Adafruit](https://learn.adafruit.com/ninja-timer-giant-7-segment-display/overview) and uses multiple layers of acrylic to form and diffuse the segments. I absolutely loved the look, and considered replicating it but, no, I've got to do my own thing ;) Then I remembered seeing 8mm bulb style WS2812 LEDs. They look just like the old analog RGB LEDs, with 4 pins and everything. Except that the pins are 5V, ground, data in, and data out. In reality, they aren't WS2812 at all, but APA106-F8 which are protocol compatible. Digital LEDs is a confusing landscape ;)

So, these gave me the idea of trying to replicate an old bulb-style 7-segment digit, like you would've seen on an old stadium score board or the original [NASA launch countdown](https://gizmodo.com/the-history-of-nasas-iconic-countdown-clock-and-a-look-1663838383).

Next step was, of course, CAD modeling a single digit. I wanted it have the same slight slant that most 7-segment displays had which definitely complicated things a bit. I settled on a 7&deg; tilt as looking right. To get ahead of the process a bit, I wanted to create some custom PCBs that would make assembling the digit really easy. I had the idea to give each one a 90&deg; point so that each of the segments could be flush fit together and soldered. But since I had a 7&deg; slant, that meant I would have to tilt the point by 3.5&deg; in opposing directions to make everything work out.

Clear as mud, right? Yeah, I thought so too and this is why I modeled it all in CAD. The basic point is that I wanted the PCBs to work unmodified for all segments and I realized that by adding those opposing angles to each point I could use the PCB either "face up" or "face down" and have all possible orientations. Here, take a look:

{{< figure src="0.jpg" >}}

The green and red faces of the modeled PCBs specify which face is up. More about how all these connect in a bit.

The display was designed so that it could be CNC routed out of 12mm thick sheet material and have all the PCB's snuggly fit, with the LEDs poking through to the front, being the only thing that can be seen.

With that sorted out, I was confident enough to design the PCBs in KiCAD and ship them off to [OSHPark](https://oshparkc.com). They really aren't all that complicated as they just pass the LED data signal from one LED to the next and provide power. The tricky bit is in that 45&deg; point. It has 5 pads on it, mirrored around the center point pad, which is ground. The middle pad on each side is data (in or out, depending on side of PCB) and the outer pad on each side is 5V.

{{< figure src="1a.jpg" caption="Ignore the tabs in the above picture, I had not sanded them off yet" >}}

The full KiCad project can be found on [GitHub](https://github.com/ManiacalLabs/DeathClock/tree/master/Segment).

By using the above described pad orientation, the correct pads will always line up no matter how you orient the PCB. With exception of data direction, of course. The ground and 5V pads are always solder-jumped across while the data pad is only connected as data flow is required.

As mentioned earlier, I had to solder some "face up" and others "face down", as shown below:

{{< figure src="1.jpg" caption="Yes, there are 8 instead of 7. 4 of one orientation and 3 of the other were needed and I couldn't remember which at the time." >}}

With these soldered and functionality confirmed, I could move on to creating the frame of the display over on the CNC. This was all prepared in Fusion 360, of course and you can download the project including all the CAM processes on [GitHub](https://github.com/ManiacalLabs/DeathClock/blob/master/Fabricate/Segment.f3z).

I'm no expert on CNC and CAM, so I'll just leave some pictures of it in process and fully routed for you to enjoy :)

{{< figure src="2.jpg" >}}
{{< figure src="3.jpg" >}}

If you want to learn more about these things, I highly recommend checking out [NYC CNC](https://www.youtube.com/user/saunixcomp), [Lars Christensen](https://www.youtube.com/user/cadcamstuff) and [Winston Moy](https://www.youtube.com/user/krayvis) on YouTube. They taught me everything I know :)

One thing I will say is that the original plan was to use MDF for this part, mainly because it's cheap. But after having to do some seriously cleaning on the CNC from all the CNC dust, I've got to say the cost savings isn't worth the other costs you will pay. MDF is nasty, terrible stuff. What I found instead was a local supplier of high quality Baltic birch plywood. This isn't your big box store junk plywood... this 12mm (yes, it's metric!) sheet has 9 plys with no voids! And seriously, it's a dream to cut. Just look back at the picture above and note how it produces actual chips, and not fine dust. Don't think I'm ever going back.

Though, as I write this I realized it might have made more sense to laser cut everything. I could use thinner 3mm or 6mm material for the front panel and just cut holes. The holes will align all the PCBs via the LEDs and once everything is soldered together, it's really not going anywhere. Then just cut a spacer frame to offset a back-plate and it's good to go. But hey, that's why this is a prototype and this is only "Part 1" :)

Anyways, speaking of assembly, now is time to put the PCBs in the frame!

{{< figure src="4.jpg" >}}

Above I show two segments installed and ready to be soldered. At this point, however, I realized I needed to be extra careful about the direction of the dataflow and, as you can see, added some annotation to the frame to make sure I didn't forget.

{{< figure src="5.jpg" >}}

As you can see the LED data flows around in, well, a figure 8 pattern. Entering on one side and exiting on the other, eventually connecting to more digits in the chain. I had to also be careful to reference by CAD model frequently so that I know where to use "face up" and where to use "face down" segments. Though, because of that opposing 3.5&deg; offset points it would actually be hard to install them incorrectly.

{{< figure src="6.jpg" >}}

Last was to install the controller for this whole party. In the picture above, I'm using an [Adafruit Pro Trinket](https://www.adafruit.com/product/2000). Which worked fine for initial testing but, once I really started playing, it ended up being replaced with a [Teensy 3.2](https://www.pjrc.com/store/teensy32.html) - Same size and an order of magnitude more power!

Fortunately I had the foresight to install a connector instead of just directly soldering everything. In the final display this will most certainly be swapped out for an internet connected device so that, if nothing else, it can always have the correct time. But as this was to act as a mobile demo (more on that shortly), I didn't want to have any requirements on a WiFi connection.

{{< figure src="7.jpg" >}}

Last but not least it all got topped off (well, "backed off" in this case) with a laser cut, clear acrylic back panel to protect everything while letting it all be seen. While this is primarily a prototype for the final display, Dan and I are going to be at the inaugural [KiCon](https://kicad-kicon.com) this weekend (Apr 26 & 27, 2019) and I've *got* to have something fun to show off! So being able to see those perfect purple PCBs was of course high priority ;)

I won't get deep into the code here as it's all just simple stuff to test the display. You can check it out on [GitHub](https://github.com/ManiacalLabs/DeathClock/blob/master/SingleDigit/SingleDigit.ino) of course if you would like. Instead, I'll jump straight to the good stuff; the video:

<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/p/BwYIX1hBhj-/?utm_source=ig_embed&amp;utm_medium=loading" data-instgrm-version="12" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/p/BwYIX1hBhj-/?utm_source=ig_embed&amp;utm_medium=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div><div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;"> View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div></a> <p style=" margin:8px 0 0 0; padding:0 4px;"> <a href="https://www.instagram.com/p/BwYIX1hBhj-/?utm_source=ig_embed&amp;utm_medium=loading" style=" color:#000; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none; word-wrap:break-word;" target="_blank">Wrapped up the code on the giant #blinky #led 7 segment display that will be coming to #kicon next week. Runs on a #teensy 3.2 with &#34;APA106&#34; #leds... Or bulb style #neopixels. And using @oshpark PCBs, of course. Just a prototype of a much larger display to come in the future. But should be fun to show off.</a></p> <p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;">A post shared by <a href="https://www.instagram.com/maniacallabs/?utm_source=ig_embed&amp;utm_medium=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px;" target="_blank"> Maniacal Labs</a> (@maniacallabs) on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2019-04-18T00:44:00+00:00">Apr 17, 2019 at 5:44pm PDT</time></p></div></blockquote> <script async src="//www.instagram.com/embed.js"></script>

So, there it is. In all it's rainbow digit glory. I'll have a more in-depth write-up on the code after the final display is made. This post is already in-depth enough as it is. Maybe someday I'll write a project post that's under 1000 words... unlikely though.

It's still a work in progress of course, but fell free to check out all the files for everything done so far on the [DeathClock GitHub repo](https://github.com/ManiacalLabs/DeathClock).

Happy making! :)