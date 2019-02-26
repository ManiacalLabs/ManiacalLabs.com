---
title: CNC Dust Boot for Dewalt Router
date: 2019-02-25T15:35:45-05:00
draft: false
tags: []
categories: []
weight: 20
# slug:
# description:
# author:
---

{{< figure src="!header.jpg" >}}

Back in May of 2018 I acquired two amazing tools from our friend Justin, who runs [WyoLum](http://wyolum.com); a laser cutter and a CNC router. The laser cutter got setup first because, well, LASERS. But I finally got around to getting the CNC up and running over the last few months. As with all things I find interesting, I dove right in and sought to create the best possible for the machine. First thing on my list was dust collection. For one, with a laser in the same shop space I really needed to keep the airborne particles down. And also, I like my lungs, so it seemed like a good idea to not have to babysit the machine with a vacuum hose.

One of the other upgrades I did immediately was to install a newer [Dewalt DWP611](https://amzn.to/2XpSZvw) trim router as the main cutting spindle. There are some definite pros and cons to this choice, but in my case it was made because just about every hobby to prosumer level CNC router I could find used that model. I figured that way I could rely on the abundance of tooling and speeds & feeds available for that specific router. And for that matter, the machine I have itself, a [Probotix Comet](https://www.probotix.com/CNC-ROUTERS/CNC-ROUTER-GX2525-COMET) had switched in recent years to shipping with the same router (mine is and older model).

There's obviously no real lack of existing dust boot options out there for the DWP611. Probotix themselves [sells one](https://www.probotix.com/DUST-BOOT) and there are a ton of others for sale, or even many open designs on [Thingiverse](https://www.thingiverse.com/search?q=Dewalt+611+dust&dwh=405c747ad451c0d). But, as [XKCD](https://xkcd.com) so aptly put it:

![Standards](https://imgs.xkcd.com/comics/standards.png)

The real story here though, is that I spent a ton of time researching my options and everything I found was one of:

- Commercial and decently expensive (> $150)
- Designed for a different machine like the Shapeoko or X-Carve
- Free design, but didn't work with my spindle mount, hose, or something else.

Trust me, I would've rather just take an existing option and use that. But finding nothing that met all my needs, I rolled my own.

{{< figure src="render.png" >}}

The main requirements were that it needed to fit the 2.5" hose from my shop vacuum, be as low profile as possible, and allow for easy bit changes.

The hose was easy enough and just required a few measurements to model a hole with the right taper. It *should* work with nearly any other 2.5" hose but in my case it was designed specifically for the hose on my [Ridgid Vacuum](https://amzn.to/2EwEP41).

The latter two requirements basically went together and led me to two important design features;

First, I modeled an opening in the top section, which mounts firmly to the router body. This allowed for still being able to depress the collet lock button without removing the boot.

Second, the bottom section of the boot attaches to the top with magnets. In my case I used some 12mm x 3mm round neodymium magnets that I happened to find at the local orange hardware store. This worked out to be more than enough holding power that it won't go anywhere but is easy enough to remove.

The magnets are secured by epoxying them into the four holes on each section. Just be sure to clean out any print imperfections from the holes and to scuff up the magnets to the epoxy can grab. And most important: align the orientation of magnets between top and bottom so it actually sticks!

The whole thing is held onto the router body by two M3x18 bolts and nuts that compress the mounting ring onto the body.

Last but not least, it needs a "brush" of sorts. You can buy brush strips but I wanted to be able to see the cutting as it happened so opted instead for some "16 gauge" clear vinyl that I picked up at the local fabric store. This was cut into a 48" x 2" strip and then mounted to the bottom section by way of the 3mm holes along the edge and M3x4 screws. This was the most precarious part as I had to wrap the strip around the bottom twice, while marking hole locations. Then I used a leather hole punch to make holes for the screws. Once it was all mounted I cut thin strips all around to make it into more of a brush.

And that's it! After some initial testing it works pretty darn well. There's still some dust escape of course, but it is worlds better than without. The length of the brushes kind of depends on what type of bits you use and maybe having multiple bottom sections with different lengths would be a good idea. But for now it's fine with the one length.

{{< figure src="1.jpg" >}}


That's all for now, if you want to make your own, the STLs and Fusion 360 files are available over on [Github](https://github.com/ManiacalLabs/ProbotixComet/tree/master/DustBoot).
