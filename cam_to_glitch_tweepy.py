import os
import random
from PIL import Image

import tweepy

import subprocess
import time 

import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()

#Oauth keys and secrets
consumer_key  = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#Oauth Process 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Create Interface
api = tweepy.API(auth)

def getBytes(image):
    with open(image, 'rb') as im:
        data = im.read()
        bytes = bytearray(data)
        return bytes

def getJpgHeaderLength(image_bytes):
    for i in (range(len(image_bytes)-1)):
        if (image_bytes[i] == 255) & (image_bytes[i+1] == 218):
            result = i
            break
    return result


def glitchJpgBytes(image, amount=None, seed=None, iterations=None):
    if amount is None:
        amount = random.randint(0, 99)
    elif amount > 99:
        amount = 99

    if seed is None:
        seed = random.randint(1, 99)
    elif seed > 99:
        seed = 99
    elif seed < 1:
        seed = 1

    if iterations is None:
        iterations = random.randint(1, 110)

    parameters = {'amount': amount, 'seed': seed, 'iterations': iterations}

    print parameters

    amount = float(amount)/100
    seed = float(seed)/100
    bytes = getBytes(image)
    headerlength = getJpgHeaderLength(bytes)

    for i in (range(iterations)):
        max_index = len(bytes) - headerlength - 4
        px_min = int((max_index / iterations) * i)
        px_max = int((max_index / iterations) * (i + 1))
        delta = (px_max - px_min) * 0.8
        px_i = int(px_min + (delta * seed))

        if (px_i > max_index):
            px_i = max_index

        byte_index = headerlength + px_i
        bytes[byte_index] = int(amount * 256.0)
    new_name = 'new_' + image
    new_name = image.rsplit('.')[0] + '_glitched.jpg'
    with open(new_name, 'wb') as output:
        output.write(bytes)

    return (new_name, image, parameters)


def savetoPNG(glitched_image):
    image = glitched_image[0]
    old_image = glitched_image[1]
    parameters = glitched_image[2]
    png_name = image.rsplit('.')[0] + '.png'

    while True:
        try:
            im = Image.open(image)
            im.save(png_name)
            os.remove(image)
            print 'succes'
            break
        except IOError:
            print 'oops'
            parameters['iterations'] -= 1
            second_attempt = (
                glitchJpgBytes(old_image,
                               amount=parameters['amount'],
                               seed=parameters['seed'],
                               iterations=(parameters['iterations'])))
            image = second_attempt[0]


def glitchJpg(image, amount=None, seed=None, iterations=None):
    glitched_image = glitchJpgBytes(image, amount, seed, iterations)
    savetoPNG(glitched_image)

def snapDisp():

	subprocess.call('killall feh', shell=True)
	image = cam.get_image()
	image = cam.get_image()
	image = cam.get_image()
	pygame.image.save(image,'temp.jpg')
	pygame.image.save(image,'temp.jpg')
	pygame.image.save(image,'temp.jpg')
	viewPng = subprocess.Popen("feh temp.jpg -F -Z", shell=True)
	

def glitchDisp():

	subprocess.call('killall feh', shell=True)	
	glitchJpg('temp.jpg')
	viewPng = subprocess.Popen("feh temp_glitched.png -F -Z", shell=True)


def tweetDisp():

	im = Image.open("temp_glitched.png")
	im.save("temp_glitched_jpg.jpg")
	photo_path = 'temp_glitched_jpg.jpg'
	status = 'Testing a Python/Tweepy App' + time.strftime("%Y-%m-%d %H:%M")
	api.update_with_media(photo_path, status=status)
	viewPng = subprocess.Popen("feh sharescreen.png -F -Z", shell=True)	
        

def buttons():
	while '0' not in tempa[0] and '0' not in tempb[0] and '0' not in tempc[0]:
		file1.seek(0)
		tempa[0] = file1.read()
		file2.seek(0)
		tempb[0] = file2.read()
		file3.seek(0)
		tempc[0] = file3.read()
		time.sleep(.1)
	
		if '0' in tempa[0]:
			snapDisp()
		if '0' in tempb[0]:
			glitchDisp()
		if '0' in tempc[0]:
			tweetDisp()
	


GPIO_MODE_PATH= os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
GPIO_PIN_PATH=os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
GPIO_FILENAME="gpio"

pinMode = []
pinData = []

HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"
INPUT_PU = "8"

for i in range(0,18):
	pinMode.append(os.path.join(GPIO_MODE_PATH, 'gpio'+str(i)))
	pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+str(i)))

file = open(pinMode[2], 'r+') 
file.write(INPUT_PU)         
file.close()

file = open(pinMode[3], 'r+') 
file.write(INPUT_PU)         
file.close()

file = open(pinMode[4], 'r+') 
file.write(INPUT_PU)         
file.close()

tempa = ['']   
tempb = ['']   
tempc = ['']   


while True:

	file1 = open(pinData[2], 'r') 
	file2 = open(pinData[3], 'r') 
	file3 = open(pinData[4], 'r') 
	tempa[0] = file1.read()
	tempb[0] = file2.read()
	tempc[0] = file3.read()
	
	buttons()
        

