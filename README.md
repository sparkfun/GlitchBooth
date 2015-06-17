GlitchBooth
===========

NPoole 10/23/14

GlitchBooth Demo for the pcDuino3 and CSI Camera Module

Featured on Sparkfun.com 10/24/14 New Product Friday

Based on the jpglitch project found at https://github.com/Kareeeeem/jpglitch 
(included here in full)

Description: This project uses the pcDuino3 (https://www.sparkfun.com/products/12856) and 2MP Camera Module (https://www.sparkfun.com/products/13100) to capture a photo and artistically corrupt it. A button press on D2 will capture an image, save it to the disk and display it using Feh (http://feh.finalrewind.org/). A button press on D3 will process the last image captured using the jpglitch method, save the output to the disk and display it using Feh. 

Using the "cam_to_glitch_tweepy" script allows the GlitchBooth to post glitched images to the Twitter stream of your choice using the Tweepy (http://www.tweepy.org/) framework. This action is triggered by a button press on D4. In order for Tweepy to work properly, you will need to register a Twitter App and insert your API Keys into the script. The GlitchBooth will also require a relatively stable internet connection. 

Simply connect the camera module to your pcDuino3 and run the Python script! 

Enjoy! 
