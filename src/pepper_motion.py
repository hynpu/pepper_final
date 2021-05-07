#!/usr/bin/env python
import rospy

from std_msgs.msg import Int8
from geometry_msgs.msg import Twist

# pub = rospy.Publisher('chatter', Twist, queue_size=1)


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    msg = Twist()
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    if data.data == 4:
        msg.linear.x = 0.6
        msg.linear.y = 0
        msg.angular.z = 0
    elif data.data == 3: #SLAM in the Future
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = 0
    elif data.data == 0:
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = -0.7
    elif data.data == 2:
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = 0.7
    else: 
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = 0
     
    pub.publish(msg)
    rate = rospy.Rate(20) # 10hz
    rate.sleep()
    
def listener():
    rospy.init_node('pepper_motion', anonymous=True)
    rospy.Subscriber('cur_gest', Int8, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()