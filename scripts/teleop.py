#!/usr/bin/env python3
 
from pynput.keyboard import Key, Listener, KeyCode
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('teleop', anonymous=True) 
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10) 
rate = rospy.Rate(10) 
move = Twist()

def on_press(key):
    try:
        if key == KeyCode(char='w'):
            move.linear.x = 0.5
            print("forward")

        elif key == KeyCode(char='s'):
            move.linear.x = -0.5
            print("backward")
            
        elif key == KeyCode(char='a'):
            move.angular.z = 0.5
            print("right")
        
        elif key == KeyCode(char='d'):
            move.angular.z = -0.5
            print("left")    

    except:
        if key == Key.esc:
            print("quit on esc")
            return False  

def on_release(key): 
    try:
        move.linear.x = 0.0
        move.angular.z = 0.0
        
    except:
        if key == Key.esc:
            print("quit on esc")
            return False 



listener = Listener(on_press=on_press, on_release=on_release, suppress=False)
listener.start()

while listener.running and not rospy.is_shutdown():
    rospy.loginfo(move)
    pub.publish(move)
    rate.sleep()