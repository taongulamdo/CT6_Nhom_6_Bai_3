from urllib import request,parse
from time import sleep

#VUFO5A2KBUX8ZUER
#id 2252681

def make_param_thingspeak(temp, humi, dist):
    params = parse.urlencode({'field1': temp, 'field2': humi, 'field3': dist}).encode()
    return params
def thingspeak_post(params):
    api_key_write:"VUFO5A2KBUX8ZUER"
    req = request.Request('http://api.thingspeak.com/update',method="POST")
    req.add_header("Content-Type","application/x-www-formm-urlencoded")
    r = request.urlopen(req, data = params)
    respone_data = r.read
    return respone_data
def main():
    from seeed_dht import DHT
    from grove.display.jhd1802 import JHD1802
    from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
    lcd = JHD1802()
    sensor = DHT('11', 16)
    ultrasonic = GroveUltrasonicRanger(5)
    dist = ultrasonic.get_distance()
    humi, temp = sensor.read()
    print('temperature {}C, humidity {}%'.format(temp, humi))
    print('{:.2f} cm'.format(dist))
    lcd.setCursor(0, 0)
    lcd.write('dist:{0:2}cm'.format('%.2f' % dist))
    lcd.setCursor(1, 0)
    lcd.write('tem:{0:1}C '.format(temp))
    lcd.setCursor(1, 8)
    lcd.write('hum:{}%'.format(humi))
    while True:
            
            try:
                params_thingspeak = make_param_thingspeak(temp,humi,dist)
                data = thingspeak_post(params_thingspeak)
                sleep(20)
            except:
                print('No connection,tryAgain')
                sleep(2)
if __name__ == "__main__":
    main()
