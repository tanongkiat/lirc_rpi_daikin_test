# lirc_rpi_daikin_test
Daikin ARC480 Airconditioner LIRC Infrared Remote Test

I was trying to make IOT AC control for my Daikin AC. But I couldn't found any working LIRC configuration from the internet.

after debuged for few hours, so here is the working configuration, tested on RPI3.


**A. CONFIGURATE INFRARED LIRC in RPI3**
>> 1. apt-get update 
>> 2. apt-get install lirc
>> 3."vi /boot/config.txt"
>> 4. find "#dtoverlay=gpio-ir-tx,gpio_pin=18"
>> 5. uncomment "dtoverlay=gpio-ir-tx,gpio_pin=18"
>> 6. Reboot
>> Notes: A.gpio-ir-tx is for sending the Infrared Signal , we will not to uncomment for receive via lirc, we will capture by using GPIO no need to change in this boot config. 
>>        B. if you uncomment both receive and send , it will causes errors.

**B. Setup REMOTE Configuration**
>> daikin.lircd.conf
1. This is my AC remote , ARC480A33 , I captures just enough for my uses. By capturing process is easy I will explain next.
2. To use this configuration ,this file have to be put inside the folder /etc/lirc/lircd.conf.d
3. after put this file , we have to restart service lirc "sudo /etc/init.d/lircd restart"

**C. Test Configuration.**
>> irlist
1. Just run this tools if the configuration is ok, it will return all buttons.

root@raspberrypi:/home/pi/myirrecord# ./irlist 

0000000000000001 OFF2
0000000000000002 OFF
0000000000000003 ON
0000000000000004 FANONLY
0000000000000005 TEMP25

**D. Send Signal to AC**
>> iron
For turn on AC
>> iroff
For turn off AC
>> iroff2
For turn off AC -> I found 2 patterns So I capture both.
>> irfan
For FanOnly Mode
>> ir25
Set Temperature to 25 Degree Celcius

**E. Capture Remote**
>> in.py
refer to https://github.com/dannyshaw/daikin-pi
However the thing inside that git , wasn't work with my AC.
this tools will help you understand your infrared protocol.
-> I'm using TSOP4308 https://www.vishay.com/docs/81926/tsop4038.pdf as the IR Receiver.
-> Just connect PIN1 -> to GPIO17 , PIN2 -> Ground , PIN3 -> VCC(3.3V)
-> run ./in.py
-> point Remote to in.py
-> If you want to capture RAW Code -> edit in.py change raw = True, it will printout RAW CODE.
-> Copy RAW and paste inside the configuration file.
-> NOTES: in my case if RAW > 20000 , it didn't work I split to 2 lines and it work.
-> for example, 
-> if we capture 452    25500
-> split to 2 lines like this,
->              452     20000
->              10      5500
-> put 500 at the end of RAW code

*** DONE **** HOPE THIS WILL HELP **** *
