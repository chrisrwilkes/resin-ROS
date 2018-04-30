#!/bin/bash

chmod u+x pub.py
chmod u+x sub.py
mkdir src
cd src
catkin_init_workspace
cd ..
catkin_make
source devel/setup.bash
cd src
catkin_create_pkg resin_ringer rospy
mv ../pub.py resin_ringer/src
mv ../sub.py resin_ringer/src
mv ../piconzero.py resin_ringer/src
cd ..
source devel/setup.bash
roslaunch resin_ringer.launch
