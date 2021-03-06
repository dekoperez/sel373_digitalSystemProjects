import paho.mqtt.client as mqtt
import time


# Mqtt Object
class Mqtt(object):

    """Mqtt class

    """

    # Attributes

    message = None

    # Method: Magic

    def __init__(self):
        """mqtt.__init__
        @Description:

        @Args:
            void

        @Returns:
            void
        """
        self.client = mqtt.Client()
        self.client.on_connect = Mqtt.on_connect
        self.client.on_message = Mqtt.on_message
        self.client.connect("192.168.1.111", 1883, 60)
        self.client.loop_start()

    # Method: Static

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        """mqtt.on_connect
        @Description:

        @Args:
            client:
            userdata:
            flags:
            rc:

        @Returns:
            void
        """

        print("Connected with result code " + str(rc))
        client.subscribe("home/hallSensor")
        client.subscribe("home/pirSensor")
	client.subscribe("home/battery")

    @staticmethod
    def on_message(client, userdata, msg):
        """mqtt.on_message
        @Description:

        @Args:
            client:
        userdata:
        msg:

        @Returns:
            void
        """

        Mqtt.message = msg.topic + "&" + str(msg.payload)
        print Mqtt.message

    # Method: Class

    def getPayload(self):
        """self.getPayload
        @Description:

        @Args:
            void

        @Returns:
            Mqtt.message:
        """

        return Mqtt.message

    def publish(self, id):
	"""self.publish
        @Description:

        @Args:
            id:

        @Returns:
            self.message:
        """

        self.client.publish('home/lock', id)
        time.sleep(2)

#myMqtt = Mqtt()
#while True:
#    myMqtt.publish('b')
#    time.sleep(2)
