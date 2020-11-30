import paho.mqtt.client as paho
import psutil as ps
import time
import json

broker="127.0.0.1"
port=1883
data = {'cpu0':{},'cpu1':{}}

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
def on_disconnect(client, userdata, rc):
   print("client disconnected ok")
   
print(json.dumps(data))
client1= paho.Client("control1")                           #create client object
client1.on_disconnect = on_disconnect
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
client1.subscribe("Cpu")
while True:
	result = ps.sensors_temperatures()
	millis = int(round(time.time() * 1000))
	data['cpu0']['Temperature'] = result['coretemp'][1][1]
	data['cpu1']['Temperature'] = result['coretemp'][2][1]
	data['cpu0']['Time'] = millis
	data['cpu1']['Time'] = millis
	ret= client1.publish("Cpu",json.dumps(data))    
	time.sleep(3)
client1.disconnect()

