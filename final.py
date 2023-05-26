import network
import socket
from time import sleep
import machine
from machine import Pin
import utime
from machine import PWM
import json
import urequests
apiKey="o.s2kyXs8P5lZe3QVXOErIbezBQTuUgpzC"
url = "https://api.pushbullet.com/v2/pushes"
headers = {'Access-Token': apiKey, 'Content-Type': 'application/json'}

data = {'type':'note','body':'Someone entered the House','title':'AntiTheft Security System'}
dataJSON = json.dumps(data)

MID=1500000
MIN=1000000
MAX=2000000
led = Pin(0, Pin.OUT)
buzzer = Pin(1, Pin.OUT)
pwm = PWM(Pin(15))

pwm.freq(50)

pwm.duty_ns(MID)

analog_value1 = machine.ADC(28)
analog_value2 = machine.ADC(27)

ssid = 'Project'
password = '12345678'
# 
def sensor():
    pwm.duty_ns(MID)
    reading1 = analog_value1.read_u16()
    reading2 = analog_value2.read_u16() 
    print("ADC: ",reading1)
    if reading1>=2000:
        print("ADC1:servo1  ")
        r = urequests.post(url, headers=headers,data=dataJSON)
        print(r.json()['receiver_email'])
        pwm.duty_ns(MAX)
        utime.sleep(.5)
    if reading2>=2000:
        r = urequests.post(url, headers=headers,data=dataJSON)
        print(r.json()['receiver_email'])
        print("ADC2:servo2 ")
        pwm.duty_ns(MIN)
        utime.sleep(.5)
    #utime.sleep(.5)
    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage():
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>Door Control</title>
            </head>
            <center><b>
            <form action="./open">
            <input type="submit" value="open" style="height:120px; width:120px" />
            </form>
            <table><form action="./close">
            <input type="submit" value="close" style="height:120px; width:120px" />
            </form>
            <form action="./ledon">
            <input type="submit" value="ledon" style="height:120px; width:120px" />
            </form>
             <form action="./sensorData">
            <input type="submit" value="sensorData" style="height:120px; width:120px" />
            </form>
            <form action="./ledoff">
            <input type="submit" value="ledoff" style="height:120px; width:120px" />
            </form>
            <form action="./buzzeron">
            <input type="submit" value="buzzeron" style="height:120px; width:120px" />
            </form>
            <form action="./buzzeroff">
            <input type="submit" value="buzzeroff" style="height:120px; width:120px" />
            </form>
            </body>
            </html>
            """
    return str(html)

Mot_A = Pin(2, Pin.OUT)
Mot_B = Pin(3, Pin.OUT)
def open_gate():
    Mot_A.value(1)
    Mot_B.value(0)
    utime.sleep(3)
    Mot_A.value(0)
    Mot_B.value(0)
    print("open")
def close_gate():
    Mot_A.value(0)
    Mot_B.value(1)
    utime.sleep(3)
    Mot_A.value(0)
    Mot_B.value(0)
    print("close")
def serve(connection):
    #Start web server
    while True:
        print("okkkkkk")
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        #print(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        print(request)
        if request == '/open?':
            open_gate()
        elif request =='/close?':
            close_gate()
        elif request =='/sensorData?':
            sensor()
        elif request =='/ledon?':
            led.value(1)
        elif request =='/ledoff?':
            led.value(0)
        elif request =='/buzzeron?':
            buzzer.value(1)
        elif request =='/buzzeroff?':
            buzzer.value(0)
        html = webpage()
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()

