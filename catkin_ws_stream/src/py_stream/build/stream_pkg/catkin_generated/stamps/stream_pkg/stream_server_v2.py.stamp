#!/usr/bin/env python	
#-*- coding:utf-8 -*-	


from matplotlib import image

import rospy
import cv2

import socket, cv2, pickle, struct
import imutils

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


## Socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
#host_ip = '192.168.10.101' # Enter the Drone IP address
#host_ip = '223.171.137.67' # Enter the Drone IP address LTE
#host_ip = '172.30.38.156'
host_ip = '192.168.0.6'
print('HOST IP:',host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
server_socket.listen()
print("Listening at",socket_address)



class Nodo(object):

    def __init__(self):
        # Params
        self.image = None
        self.br = CvBridge()
        # Node cycle rate (in Hz).
        self.loop_rate = rospy.Rate(1)

        # Publishers
        # self.pub = rospy.Publisher('stream_image', Image,queue_size=10)

        # Subscribers
        rospy.Subscriber("stream_image",Image,self.callback)

    def callback(self, msg):
        rospy.loginfo('Image received...')
        self.image = self.br.imgmsg_to_cv2(msg)


    def start(self):
        rospy.loginfo("Timing images")
        #rospy.spin()
        while not rospy.is_shutdown():
            # rospy.loginfo('publishing image')
            br = CvBridge()
            if self.image is not None:
                # self.pub.publish(br.cv2_to_imgmsg(self.image))
                self.loop_rate.sleep()

if __name__ == '__main__':
    rospy.init_node("stream_node", anonymous=True)
    my_node = Nodo()
    my_node.start()



