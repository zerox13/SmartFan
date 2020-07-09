import urequests

class webhooks:
    onUrl="https://maker.ifttt.com/trigger/turn_on/with/key/PUTYOURKEY"
    offUrl="https://maker.ifttt.com/trigger/turn_off/with/key/PUTYOURKEY"
    notifUrl="https://maker.ifttt.com/trigger/tempRH/with/key/PUTYOURKEY"

    def send_notif(value1, value2):
        try:
            print("Sending post req")
            req = urequests.post(url=notifUrl, json={'value1': value1, 'value2': value2})
            print("Req sent")
            print(req)
            done = False
        except:
            print("err")
            pass

    def turn_onOff(onOff=False):
        try:
            if(onOff):
                req = urequests.post(url=onUrl)
            else:
                req = urequests.post(url=offUrl)

            print("Truning on/off")
        except:
            print("Err turning on/off")

    #
