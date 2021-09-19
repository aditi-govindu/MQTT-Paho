# MQTT-Paho
Use paho-python to display publishers and subscribers of temperature sensor readings
![Use of MQTT broker] (https://miro.medium.com/max/2625/1*7MwXy5N4rx4mAxZ2KZrwJQ.png)

# What is MQTT?
MQTT or Message Queuing Telemetry Transport is a messaging protocol used in TCP/IP model. It has the following principles:

* Lightweight with minimal overhead in data transfer
* Constant session awareness
* Reliable, robust and simple to use
* Support for 3 levels of QoS
* Traditional Client-Server architecture

It is used in **Internet of Things** applications to publish-view real time sensor data. Facebook messenger, Instagram, AWS solar IoT projects etc. also use MQTT protocols

# About
**publisher.py**

Python code to publish random numbers in range of 30-100 to a HiveMQ broker on the internet. These numbers will be displayed on the command prompt, when subscriber requests data from same broker

**subscriber.py**
Python code to view random numbers published by publisher.py. Code will terminate when Ctrl + C is entered in command prompt

# Libraries used
* paho (*pip install paho-mqtt*)
* time
* random

# References
https://www.emqx.com/en/blog/what-is-the-mqtt-protocol

http://www.steves-internet-guide.com/into-mqtt-python-client/
