# button-soundboard
On ubuntu

lsblk to find the name of the sd card
then

mount /dev/mmcblk0p1
mount /dev/mmcblk0p2

Copy the image onto the sdcard

sudo dd bs=8M if=2019-09-26-raspbian-buster-lite.img of=/dev/mmcblk0 conv=fsync

To enable the ssh-server you need to add a file on the sd-card in the boot partition.
It needs to be a file named ssh
touch /media/yocto/boot/ssh


Find you IP (local) here it is 192.168.0.* sometimes it's 192.168.1.*

Launch that command before and after you connect the raspi to the network
sudo nmap -sP 192.168.0.0/24 | awk '/^Nmap/{ip=$NF}/B8:27:EB/{print ip}'

Find the new IP, congrats, it's your raspi !

ssh pi@192.168.0.99
password =>
raspberry

update password: passwd raspberry


sudo apt-get install python-rpi.gpio python3-rpi.gpio


import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library


def button_callback(channel):
    print("Button was pushed!")


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up


