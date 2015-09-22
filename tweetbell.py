import RPi.GPIO as GPIO
import pygame.mixer as mixer
import subprocess

from time import sleep as sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mixer.init( 48000, -16, 1,1024)
bell = mixer.Sound("doorbell.wav")

channel = mixer.Channel(1)

message = "\"There's somebody at the door!! #Winning #GrotBags #HASHTAG #HACKEDIT\""
command = "twitter -egee@pimoroni.co.uk set %s" % message
print(command)

while 1 :
    sleep(0.1)
    if(GPIO.input(4) == 0):
      channel.play( bell )
      subprocess.call(command, shell= True)
      sleep(10)


