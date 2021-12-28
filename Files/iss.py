#!/usr/bin/env python3

import sys
from PIL import Image, ImageFont, ImageDraw
import ST7789 as ST7789
import json
import urllib.request
import time

__DEBUG__ = False

disp = ST7789.ST7789(
    height=240,
    width=320,
    rotation=180,
    port=0,
    cs=1,
    dc=9,
    backlight=13,
    spi_speed_hz=60 * 1000 * 1000,
    offset_left=0,
    offset_top=0
)

disp.begin()

#
# World Map image - 320x240
#
mapImg = Image.open("map.jpg")
mapImgWidth = mapImg.width
mapImgHeight = mapImg.height

#
# ISS Gif file - this is just a pure white square
#
issImg = Image.open("iss.gif")
issImg = issImg.rotate(90)
issImgWidth = issImg.width
issImgHeight = issImg.height

#
# The mask which will turn the white iss gif file into an actual image
#
issMaskImg = Image.open("iss_mask.gif")
issMaskImg = issMaskImg.rotate(90)

#
# Font for text at the bottom
#
font = ImageFont.truetype("times-ro.ttf", 18)


#
# Convert lat/lon into a pixel coordinate on our map, adjusted so that the ISS image will be centred on that pixel
#
def calcXY(lat, lon):
    global mapImgWidth, mapImgHeight
    global issImgWidth, issImgHeight
    x = int((mapImgWidth / 360.0) * (180 + lon)) - int(issImg.width / 2)
    y = int((mapImgHeight / 180.0) * (90 - lat)) - int(issImg.height / 2)
    return x,y



while True:
    #
    # Load the current status of the ISS in real-time
    #
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    #
    # Extract the ISS location
    #
    location = result["iss_position"]
    lat = float(location['latitude'])
    lon = float(location['longitude'])

    #
    # Convert the lat/lon into a coordinate where we will draw the ISS gif
    #
    result = calcXY(lat, lon)
    iss_x = result[0]
    iss_y = result[1]

    #
    # Create a copy of our world map, paste the iss gif onto it along with a mask.
    #
    img = mapImg.copy()   
    img.paste(issImg, (iss_x, iss_y), issMaskImg)

    #
    # Write the location of the ISS at the bottom of the world map
    #
    draw = ImageDraw.Draw(img)
    text = f"Latitude: {lat}, Longitude: {lon}"    
    draw.text((10, 220), text, (170, 170, 170), font=font)
    
    #
    # Display the final image
    #
    disp.display(img)

    #
    # Wait 5 seconds and do it all again
    #
    time.sleep(5)
