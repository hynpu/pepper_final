#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
from collections import Counter

# hyper param
rate_hz = 10
sec_required = 2 # need 2 sec to capture a gesture
rec_gesture = True
ges_list = [1,1,1,1,1,1,1,1,1,1]
GES_THRES = len(ges_list) * 0.4 # in the past N cycles, at least # of thres should be this gesture
cur_ges = 1

# className_list = ['left','palm','right','weird','yes']

def callback(data):

  if rec_gesture == True:
    ges_list.pop(0)
    ges_list.append( data.data )


def most_frequent_gest(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0], occurence_count.most_common(1)[0][1]

def main():
  # loop through all the time
  rate = rospy.Rate(rate_hz)
  rospy.Subscriber("gesture_class", Int8, callback)
  while not rospy.is_shutdown():
    most_prob_gest, gest_occurance = most_frequent_gest(ges_list)

    # print(most_prob_gest)

    # if cur gest cnt reach thres, then pub; otherwise pub STOP to PEPPER
    if gest_occurance > GES_THRES:
      rospy.loginfo(rospy.get_caller_id() + 'Current occurance %s, %s', gest_occurance, most_prob_gest)
      pub.publish( most_prob_gest )
    else:
      pub.publish( 1 )
    rate.sleep()

if __name__ == '__main__':

  rospy.init_node('gest_proc', anonymous=True)
  pub = rospy.Publisher('cur_gest', Int8, queue_size=1)

  main()