#!/usr/bin/env python
import rospy

from std_msgs.msg import Int8
from geometry_msgs.msg import PoseStamped

pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    rate = rospy.Rate(10) # 10hz
    msg = PoseStamped()
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    msg.header.frame_id = "base_link"
    
    if data.data == 0:
        msg.pose.position.x = 0.1
        msg.pose.position.y = 0.0
        msg.pose.position.z = 0.0
        msg.pose.orientation.x = 0.0
        msg.pose.orientation.y = 0.0
        msg.pose.orientation.z = 0.0
        msg.pose.orientation.w = 1.0
    elif data.data == 1:
        msg.pose.position.x = -0.1
        msg.pose.position.y = 0.0
        msg.pose.position.z = 0.0
        msg.pose.orientation.x = 0.0
        msg.pose.orientation.y = 0.0
        msg.pose.orientation.z = 0.0
        msg.pose.orientation.w = 1.0
    else: 
        msg.pose.position.x = 0.0
        msg.pose.position.y = 0.0
        msg.pose.position.z = 0.0
        msg.pose.orientation.x = 0.0
        msg.pose.orientation.y = 0.0
        msg.pose.orientation.z = 0.0
        msg.pose.orientation.w = 1.0
     
    pub.publish(msg)
    rate = rospy.Rate(10) # 10hz
    rate.sleep()
def listener():
    rospy.init_node('pepper_motion', anonymous=True)
    rospy.Subscriber('cur_gest', Int8, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()