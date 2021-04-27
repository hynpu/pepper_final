#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
from collections import Counter

# hyper param
rate_hz = 20
sec_required = 2 # need 2 sec to capture a gesture
rec_gesture = True
ges_list = [4,4,4,4,4,4,4,4,4,4]
GES_THRES = len(ges_list) * 0.6 # in the past N cycles, at least # of thres should be this gesture
cur_ges = 4

# className_list = ['flow','left','ok','right','stop']

def callback(data):

  if rec_gesture == true:
    ges_list.pop(0)
    ges_list.append( data.data )

    print(ges_list)


def most_frequent_gest(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0], occurence_count.most_common(1)[0][1]

def main():
  # loop through all the time
  rate = rospy.Rate(rate_hz)
  while not rospy.is_shutdown():
    most_prob_gest, gest_occurance = most_frequent_gest(ges_list)

    # if cur gest cnt reach thres, then pub; otherwise pub STOP to PEPPER
    if gest_occurance > GES_THRES:
      pub.publish( most_prob_gest )
    else:
      pub.publish( 4 )
    rate.sleep()

if __name__ == '__main__':

  rospy.init_node('gest_proc', anonymous=True)
    rospy.Subscriber("gesture_class", Int8, callback)
  pub = rospy.Publisher('cur_gest', Int8, queue_size=10)

  main()