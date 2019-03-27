---
title: Meter Clock Part 2
date: 2019-03-27T18:10:33-04:00
draft: false
tags: []
categories: []
weight: 20
# slug:
# description:
author: haooken
---

A while back...an embarrassingly long while back...the [Meter Clock](https://maniacallabs.com/2014/07/08/meter-clock-pt1/) made an appearance. We left that project back in 2014 intending to “either print or build from wood a case of some kind”. And as sometimes happens, projects get put on the back burner. Well I was hungry to finally finish this project, so I brought it to the front burner to finish cooking.

{{< figure src="!header.jpg" >}}

Kitchen analogies aside, I did want to put some finishing touches on this project. I knew I wanted something simple, but nice looking. A wood box would work, but seemed a little, I dunno, obvious. But the newfound availability of some rather nice [Subtractive]({{< ref "/posts/2019/2/CNC_Dust_Boot_for_Dewalt_Router" >}}) [Manufacturing]({{< ref "/posts/2019/3/Custom_CNC_Wasteboard" >}}) equipment started the creative juices flowing. Adding to that was the fact that the meters themselves are designed to be panel mounted. And a well-tuned laser cutter can cut very nice holes in a variety of materials, specifically acrylic. I immediately saw an opportunity to make use of a tool that I built some time ago that also applied controlled heat to plastic. And thus, the wood-and-bent-acrylic combination became the order of the day.

The final design would feature the meters and associated electronics mounted to a piece of acrylic. This acrylic would be bent in such a way so as to stand on its own. In order to add some stability and make it look nicer than just a piece of plastic, wood legs would be fabricated, each having a slot for the acrylic to slide into, thereby ‘bookending’ the clock.

{{< figure src="MC_Design.jpg" >}}

This was also an opportunity for me to get some more experience with the CAM part of Fusion 360. Adam has done a fantastic job setting up our [Probotix Comet CNC](https://www.probotix.com/CNC-ROUTERS/CNC-ROUTER-GX2525-COMET), and provided excellent guidance. With his help, we finalized the design for the legs and dialed in the Feeds and Speeds. Given the choice of a very nice piece of red oak, slow and steady was the order of the day. This material was a little more dense than the MDF the CNC had munched on up to that point. But our track history is not to let our machines have an [easy go of things]({{< ref "/posts/2018/9/Button_Pixel__Bixel" >}}). Fortunately, all went well, and the legs worked out great. We were both quite impressed by the quality we were able to achieve. The grain pattern is pretty awesome, and definitely why a wood element was desired for this part of the project.

{{< figure src="MC_Cutouts.jpg" >}}

With the legs accounted for, and with something to size the acrylic to, we threw together a design for the part that would actually hold the meters. There are holes for the meter bodies and the m3 mounting studs, as well as a hole for the LED wire to come out from the rear of the display. The only special part of the design was the inclusion of a notch on either side at the point where the acrylic would bend. This serves two purposes: provide a reference point for applying heat to bend, and to prevent the deformation of the acrylic from keeping the plastic from fitting. Without these notches, the acrylic might “bunch up” at the back of the bend, and there would no longer be a nice flat surface making contact with interior of the notches in the legs.

{{< figure src="MC_Bend_1.jpg" >}}

The acrylic bending jig uses a piece of 30ga nichrome wire stretched between two posts. The wire is positioned so that it is just barely below the level of the acrylic. Close, but not making contact. The aluminum channel helps to focus the heat, and prevent the plywood from scorching. A variable bench supply works well enough to supply, in this case, about 35W (20.1V, 1.76A) through the wire. Note that the top of the wire is connected to a spring. This is intentional, as the wire will expand when heated. This spring allows for the wire to be under constant tension, thus preventing it from sagging and heating the acrylic unevenly. Once the acrylic is in position and the power applied, it only took about a minute for the acrylic to be pliable enough to bend around a form. The ‘form’ was a piece of 4x4 with a 30 degree cut taken out, to give a 60 degree wedge. Our initial test went well, as did the final bend. Oh, and it did actually fit (insert sigh of relief here).

{{< figure src="MC_Bend_2.jpg" >}}

So all in all, a successful day in the Subtractive Manufacturing wing of the Maniacal Labs home office. The ‘final’ touches happened later, and included a few quick sprays of lacquer to seal and protect the wood, and to make it pop. Love that grain! A few strategic applications of a gel-type CA glue should keep the legs on the acrylic (which was a snug fit to begin with). Though if needed, some epoxy might be used, we’ll see.

{{< figure src="MC_Final_2.jpg" >}}

I was a long time in the works, but when the stars align to provide that creative spark, it’s neat to see the results. And I think this project finally has the completion it deserves. And the techniques used will be fun to call upon in the future for other projects. I think Adam and I definitely want to try more hardwood CNC projects. And of course, shooting high-powered lasers at plastic is always fun, provided there is adequate ventilation ;)