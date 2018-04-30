#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
speed = 60
import piconzero as pz, time
import sys
import tty
import termios
#define the display text

pz.init()

def callback(data):
   rospy.loginfo("I receive %s", data.data)
   counter = 0
   while counter < data.data:
      pz.forward(speed)
      time.sleep(.05)
      pz.stop()
      time.sleep(.1)
      counter += 1
#define the subscriber def random_subscriber():
def random_subscriber():
    rospy.init_node('random_subscriber')
    rospy.Subscriber('rand_no',Int32, callback)
    rospy.spin()

if __name__=='__main__':
    random_subscriber()
