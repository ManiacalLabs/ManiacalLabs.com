---
author: dan
date: 2014-12-09 13:00:21+00:00
draft: false
title: Binary Epoch Christmas Tree
type: post
url: /2014/12/09/binary-epoch-christmas-tree/
categories:
- Clocks
- Cool Stuff
---

So I have 15 meters of LPD8806 programmable LED lights on my fake Christmas tree. But I feel I can up the Nerd quotient even more.

Inspired by the [Binary Epoch Clock](/product/becv1/) kit, I added an animation to the tree that turns it into a giant unreadable binary clock. The lights are controlled by a RasPi running the [BiblioPixel](https://github.com/ManiacalLabs/bibliopixel) library, with the [AllPixel](/allpixel) making the hardware interfacing a snap.



Unix epoch time (number of seconds since 12:00am Jan 1 1970) is represented in binary notation. The strand of lights shows 32 places. Green represents a 'one', red, a 'zero'. The top of the tree is the Least Significant Bit, the bottom the Most Significant Bit. There is an option to reverse the order of the bits (so that I could make the first bit be at the bottom of the tree instead). Once I clean up the code a bit, I'll incorporate this into the [BiblioPixel source code](https://github.com/ManiacalLabs/bibliopixel) as a strip animation example.

In closing, my Christmas tree is an unreadable binary clock. Your argument is invalid.

-Dan




