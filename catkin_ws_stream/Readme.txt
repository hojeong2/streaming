
This is for socket video stream 

pkg: stream_name
script: 
- stream_server.py: this node subscribe the ros senssor_mags/image and open the streaming server
- stream_client.py: this node receive the streaming video 
- image_pub.py: this node just for debugging, simple image publish node


#1 Host IP
you need to check your ip and set the host ip 
- stream_server.py
- stream_client.py

-> host_ip ='192.168.x.xx'

#2 Topic Name
you need to set which topic would you subscribe
- stream_server.py

-> rospy.Subscriber("TOPIC NAME",Image,self.callback)

#3 Launch

roslaunch stream_pkg stream.launch

and rosrun stream_pkg image_pub.py



