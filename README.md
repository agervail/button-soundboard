# button-soundboard

## Prepare the raspberry sdcard
Tested on ubuntu

`lsblk` to find the name of the sd card, then unmount partitions if any:
`umount /dev/mmcblk0p1`
`umount /dev/mmcblk0p2`

Copy the raspbian image into the sdcard:
`sudo dd bs=8M if=2019-09-26-raspbian-buster-lite.img of=/dev/mmcblk0 conv=fsync`

To enable the ssh-server you need to add a file on the sd-card in the boot partition. It needs to be a file named ssh:
(in boot partition) `touch ssh`

Find you IP (local) here it is 192.168.0.XXX sometimes it's 192.168.1.XXX

Launch that command before and after you connect the raspi to the network
`sudo nmap -sP 192.168.0.0/24 | awk '/^Nmap/{ip=$NF}/B8:27:EB/{print ip}'`

Find the new IP, congrats, it's your raspi !

## Install the soundboard on the raspberry
`ssh pi@192.168.0.XXX`
password => raspberry

Update password:
`passwd pi`

Install dependencies:
`sudo apt update`
`sudo apt install git python3-rpi.gpio python3-pygame`

Clone this repository

Tell Raspbian to look at "card #1" for the default audio. Card #0 is the built in audio, so this is fairly straightforward.
`sudo nano /usr/share/alsa/alsa.conf` and look for the following two lines:
defaults.ctl.card 0
defaults.pcm.card 0

Change both “0” to “1” and then save the file. That’s it!
