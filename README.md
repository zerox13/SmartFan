
---
title: 'Automating a floor fan with DHT11 sensor'
disqus: hackmd
---
> Abdulsalam Aldahir (aa225jy)
Estimated time: 2 hours
 

![](https://i.imgur.com/KPZZ61f.jpg)

This project is about how to control a floor fan using lopy4 with a dht11 sensor. With dh11 we can measure the tempture and the humadity This will be used to dermine if the fan need to be turned on or off. The fan can be also controlled by google home if you want.
### Objective

This project will give you a basic idea about internet of things. With this project you will make life easier by makeing the fan you are using kind of smart, it will be able to determine if it should be turned on or off by itself. The fan will also be controled by google home which will give us more flexibility. The data of the sensor will be saved mainly to be shown in a dashboard, but it can also be helpful for further analysis.

### Material

For this project you will need the following material:

| Item            | Website to buy from | Price   |
| --------------- | ------------------- | ------- |
| Lopy4           | [Pycom][1]          | 34.95€  |
| Expansion Board | [Pycom][2]          | 16.00€  |
| Antenna         | [Pycom][7]          | 8.00€   |
| Usb cable       | [Webhallen][3]      | 49 SEK  |
| DHT11           | [kjell][4]          | 49 SEK  |
| Smart plug      | [kjell][5]          | 299 SEK |
| Fan             | [mediamarkt][6]     | 349 SEK |

[1]: https://pycom.io/product/lopy4/

[2]: https://pycom.io/product/expansion-board-3-0/

[3]: https://www.webhallen.com/se/product/277015-Belkin-MIXIT-USB-kabel-2-m-Svart

[4]: https://www.kjell.com/se/produkter/el-verktyg/arduino/moduler/temperatur-och-luftfuktighetssensor-for-arduino-p87877

[5]: https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwin4t6v27zqAhUpIHsKHcDzCT8YABAEGgJsZQ&ohost=www.google.com&cid=CAESQeD2-claZdu4y1E-HEpVakYMuy_48-V3MlH6AfanHXE2fo1Z2utiMTzC8QDwz41OEzONy-nh0gF1e3WFfELUYG2o&sig=AOD64_3Z42SxWlV0qt9V9Nq1qu6sfeFg-w&ctype=5&q=&ved=2ahUKEwizzNav27zqAhWNlIsKHf9IAuQQ9aACegQICxA3&adurl=

[6]: https://www.mediamarkt.se/sv/product/_tristar-ve-5893-golvfl%C3%A4kt-40-cm-1309716.html?rbtc=%7C%7C%7C%7Cp%7C%7C&gclid=Cj0KCQjw3ZX4BRDmARIsAFYh7ZIS_Zdt6Sxqd4QW-2kPlu_8Pf24orOBY0sOl5a7XDJDv2NdE340WPcaAguaEALw_wcB&gclsrc=aw.ds

[7]: https://pycom.io/product/external-wifi-antenna/
## Material specification
* **Lopy4**, is Micropython-programmable IoT platform which is used 
* **Expansion Board**, is uesd to 
* **Antenna**: This is used to give lopy4 the ability to detect wifi network  
 OBS: If you want to use Lora or Sigfox you might need the antenna that works with them.
* **Usb cable**, is used to power the lopy4 and upload the code form the computer.
* **DHT11** The sensor that will measure the temp and humidity.
* **D-link smart plug** a smart plug which is used to give us the ability to conrol the fan remotely.
* **Fan**, Any fan or anything you want to automate.

### Computer setup

Before to start the project, lets start prepareing our computer with an IDE.
In this toutrial i will use Atom which can be downloaded from [here](atom.io), but you are free to use the editor of your chice.

We will also need to install a plugin to help us upload and run the code into the lopy4 device.
To install it on a mac go to preferences -> packages and search for pymakr. Or just go [here](https://atom.io/packages/pymakr) and click on install which will open atom and install the plugin.
### Putting everything together
So lets put everything together. As showen below, the dht11 sensor will measure and give it to lopy4, the lopy4 will think and determine if it should turn the fan off or on. To turn the fan off or on, the lopy4 will send a webrequest over wifi to the smart plug.
![](https://i.imgur.com/iXc2EIw.png)


So you need to plug the fan to smart plug. And to connect the dh11 sensor to lopy4, 

connect 3v3 -> the middle pin, G9 -> +, GND -> -
or just follow the below picture.

![](https://i.imgur.com/eWnD0iL.png)




### Platform

In this toutrial we will keep it simple and use Pybytes to transmitt the data to the internet and IFTTT to automate turning on and off the fan. Pybytes is Pycoms platform, it is so easy to use, this will work as our databse and dashboard. You can use another platform like grafana if you like, which gives you more functionality(triggers for exemple), but this require more work with MQTT broker and MQTT client. With pybytes you get all that for ready to use with a single line of code. And since we will use IFTTT for turning on and off, we can use to send notifications to the phone too.   

![](https://i.imgur.com/bPFNDMu.png)


### Preparing some webhooks 
To make the lopy4 turn the smart plug(the fan) on and off by itself we need to make that work as a webrequest. For this we will make it very simple and use [IFTTT](http://ifttt.com/create) with a smart  plug. You can choose any smart plug you want you just need to make sure it is supproted by IFTTT. 

In this toutrial we will use the Dlink smart plug.
![](https://i.imgur.com/V51XLhV.jpg)

You will need to make an accout and setup the device. Follow the instructions that comes with it, it is pretty simple though.  

Next is to go to [IFTTT](http://ifttt.com) or just use the IFTTT app on your phone.
You can download the app from [Google play](https://play.google.com/store/apps/details?id=com.ifttt.ifttt&hl=en) or [App store](https://apps.apple.com/us/app/ifttt/id660944635)

After making an account we start by making a webhook to turn the plug on. So we go to *create* and click on the **+** beside the word *This* and search and choose webhook as shown below  

![](https://i.imgur.com/VRD0eqy.png)

After choosing webhook, we click on *revice a web requset* and give it a name, we will need later, for example i will call it *turn_on*. 

Now we click on the **+** beside *That* and search for *mydlink* You will need to connect your Dlink account which you should have created while setting up the smart plug  

![](https://i.imgur.com/nAUR13o.png)

Now we choose *turn on plug*  --> choose the device --> finsh 

And now we are done, all we need is to get a the link request that turns on the fan. So we go to the [Documentation](https://maker.ifttt.com/use/p5leuMpGRoYmQPxcgtjD-9Tg8QfnPeX8Mce1Et2H2su) of Webhooks where you find the link with your key and test it. Put the the name we gave to the request and Click test. This should turn on the fan if the plug is connected. 

Now we will need to do this again, but this time to turn off.

If you wish to get notifications of the phone, you will also need to make another webhook for that. It is similar to what is done above, but instead of mydlink choose notification 

![](https://i.imgur.com/BiVFhBd.png)

For this you will need to have the IFTTT app installed on your phone with the same acount.

After that you will have 3 web request ready to use in the code.

### The code
Now what is left is to put everything together in code. Please download all the code from my [github](https://github.com/zerox13/SmartFan). All you need to do is just to replace the key of the links in the webhooks file with your unique key, or just replace the whole links.
```python=
import urequests

class webhooks:
    onUrl="https://maker.ifttt.com/trigger/turn_on/with/key/YOURKEY"
    offUrl="https://maker.ifttt.com/trigger/turn_off/with/key/YOURKEY"
    notifUrl="https://maker.ifttt.com/trigger/tempRH/with/key/YOURKEY"
    ....
```

After this you should be able to run the code and everything should work!

below is the main function that run everything. If you wish to change something (e.x the limit to turn of or on) it is this file you need to edit. 

```python=
import time
from machine import Pin
import _thread
from dht import DTH
import pycom
from webhooks import webhooks

# Type 0 = dht11
# Type 1 = dht22
th = DTH('P23', 0)
pycom.heartbeat(False)


def send_env_data():
    while True:
        result = th.read()
        while not result.is_valid():
            time.sleep(.5)
            result = th.read()
        print('Temp:', result.temperature)
        print('RH:', result.humidity)
        try:
            if(result.temperature > 25):
                webhooks.turn_onOff(True)
                webhooks.send_notif(result.temperature, result.humidity)
            else:
                webhooks.turn_onOff(False)
        except:
            pass
            
        pybytes.send_signal(2,result.temperature)
        pybytes.send_signal(3,result.humidity)

        pycom.rgbled(0x00ff)
        time.sleep(60*30)
        pycom.rgbled(0xff00)

_thread.start_new_thread(send_env_data, ())

```
Please note that the urequests file is not written by me, and here is the source of it. [here](https://github.com/jotathebest/micropython-lib/blob/master/urequests/urequests.py)
### Transmitting the data / connectivity

The data is trnasmitted via Wifi. It is maybe smart to use LoRa if there is a gateawy near you. LoRa needs less power and have a much bigger range than Wifi. In our case we are not transmitting big chunks of data, which is a great for useing LoRa. However this toutrial will only use Wifi because i think it does not make that big diffrence and i actully have no gateway near me.

The data is sent to pybytes using the pycom library. To get this work, you need to create an acount on pybytes to add the device from the devices menu, you then select lopy4 and add the SSID and the Password of your Wifi network. After that we will be ready to send data as shown in the code above (line 31 and 32)

The data is also sent to my phone every 30 minutes. The data is sent to the phone as a notification via [IFTTT](http://ifttt.com) as explained previously.



### Presenting the data

As mentioned before, pybytes will work as the database and the dashboard. Below is how the dashborad looks like in pybytes.

![](https://i.imgur.com/Jktr0OM.png)

The data also is sent to the phone, below is a screen show how the notification looks like. 

![](https://i.imgur.com/92Gwi7p.jpg)


### Finalizing the design

Below is how my setup looks like i reality.

![](https://i.imgur.com/7O4oeSs.jpg)

I still dont have a case for the device yet, so i put it in an old raspberry pi case xD. 

This project was really fun for me. Now my fan is kind of thinking, hehehe.

You can absoulty be creative and change the fan with something else you want to automate, the fan was just an exemple.

I hope you enjoyed and learned something!

