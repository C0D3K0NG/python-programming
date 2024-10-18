#!/bin/python3
from vidstream import CameraClient	#from the vidstream module we are importing a class called Camera client which will be the sending side of the camera chat
from vidstream import StreamingServer	#from the vidstream module we are importing a class called Streaming Server which will be the receiving side of the camera chat
import threading	#we are importing the threading module to perform streaming and receiving at the same time with delays
import time		#time module to make a delay or downtime in which threading will work, connection of two devices might perform an exception if we didnt give it the time to sync


sending=CameraClient('192.168.68.252',5555)
receiving=StreamingServer('192.168.43.128',5555)

threading.Thread(target=receiving.start_stream).start()
time.sleep(2)
threading.Thread(target=sending.start_server).start()

while(input("") != "stop"):
	continue
sending.stop_server()
receiving.stop_stream()
