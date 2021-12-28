# PiZeroISSTrackerGadget
A small Raspberry Pi Zero / Display HAT Mini based gadget to show where the ISS currently is on a small display screen.

**Hardware**

This little gadget makes use of two bits of hardware - although I'm sure similar products should work equally well.

I'm in the UK, so in my case I've used:

1. A Display Hat Mini by Raspberry Pi

https://shop.pimoroni.com/products/display-hat-mini

2. A Raspberry Pi Zero 2, in this case with colour-coded headers already soldered on:

https://thepihut.com/products/raspberry-pi-zero-2?variant=41181426942147

3. A micro-SD card with Raspberry OS (Bullseye) Lite installed.  SSH is enabled.

4. A Micro USB cable and the correct power source.

I won't go into too many details about setting the Pi up, other than to say that in my case I run the Pi "headless" (https://www.youtube.com/watch?v=dhY8m_Eg5iU), with SSH enabled. I can then edit files using Visual Studio Code via its SSH add-on.  Details of how to set that up can be found in this youtube video: https://www.youtube.com/watch?v=lKXMyln_5q4


**Source Code**

The source code for the project currently consists of:

1. iss.py - the main python source file
2. map.jpg - a 320x200 resolution world map image, plus a section of "black" added to the bottom of the image to make the full image 320x240 pixels.
3. iss.gif - at the moment this is simply a square of white - the mask file below then turns that into a white "iss" image on-screen.
4. iss_mask.gif - this masks out just the shape of the ISS itself.  You can mess around with these images to your taste.
5. times-ro.ttf - download this file from here: https://www.download-free-fonts.com/details/86847/times-roman


**Execution**

Place all 5 files into the same folder on your pi, and execute:

_python iss.py_

If all is well, you should see your world map image and a very simple image representing the ISS at its current location.
