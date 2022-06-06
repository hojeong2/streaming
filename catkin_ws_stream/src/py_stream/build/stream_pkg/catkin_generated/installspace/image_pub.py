#!/usr/bin/env python	# 파이썬을 쓴다면 반드시 달아주자
#-*- coding:utf-8 -*-	# 한글 주석을 달기 위해 사용한다.

from matplotlib import image
import rospy
import cv2

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError



def image_pub():
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    rospy.init_node("steam_webcam",anonymous=True)
    image_pub = rospy.Publisher("stream_image", Image,queue_size=1)

    bridge =CvBridge()

    while not rospy.is_shutdown():
        ret, cv_image= cap.read()

        image_pub.publish(bridge.cv2_to_imgmsg(cv_image,"bgr8"))
        rospy.loginfo("Image Pub")
    cap.release()
image_pub()

# cv2.destroyAllWindows