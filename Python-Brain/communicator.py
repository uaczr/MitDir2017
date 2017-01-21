##@package communicator
#@author Christoph Hellmann
#@date 21.01.2017
#@brief  Communication functions


import paho.mqtt.client as mqtt
import logger

class topic:
    name = ""
    value = 0
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

## Communicator Class
#
#Used for communication with peripherals via MQTT
class communicator():
    sub_topics = []
    pub_topics = []
    client = 0
    connected = False
    ## Constructor
    def __init__(self):
        logger.debug("Creating Communicator.")
        self.client = mqtt.Client()
        self.client.user_data_set(self)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message


    ## Callback on_connect
    @staticmethod
    def on_connect(client, userdata, rc):
        logger.debug("Connected with result code "+str(rc))
        userdata.connected = True
        for topic in userdata.sub_topics:
            client.subscribe(topic.name)
            logger.debug("Subscribing to topic " + topic.name)

    ## Callback on_message
    @staticmethod
    def on_message(client, userdata, msg):
        logger.debug(msg.topic + " " + str(msg.payload))
        for topic in userdata.sub_topics:
            if(msg.topic == topic.name):
                topic.value = msg.payload
    ## Connect
    def connect(self, ip, port, keep_alive):
        logger.debug("Connecting to " + str(ip) +":"+ str(port))
        self.client.connect(ip,port=port,keepalive=keep_alive)

    def loop_forever(self):
        logger.debug("Running MQTT-Loop.")
        self.client.loop_forever()

    def add_sub_topic(self, topic):
        self.sub_topics.append(topic)
        if(self.connected == True):
            self.client.subscribe(topic.name)

    def publish(self, topic):
        if(self.connected):
            logger.debug("Publishing " + str(topic.value) + " to " + str(topic.name) + ".")
            self.client.publish(topic.name, topic.value)




