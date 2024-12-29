import time
import rospy
from ubt_msgs.srv import *

def handle_led_client(type,mode,color):
    rospy.wait_for_service('hal_led_set')
    try:
        rospy.ServiceProxy('hal_led_set',led)
        resp1 = handle_led_client(type,mode,color)
        return resp1.rc
    except rospy.ServiceException as e:
        rospy.logerr('Service Call Failed: e')

def head_led_turn_on_red():
    type = 2
    mode = 1
    color = 1
    handle_led_client(type,mode,color)

def head_led_turn_off_blue():
    type = 2
    mode = 1
    color = 3
    handle_led_client(type,mode,color)

def button_led_blink_red():
    type = 1
    mode = 6
    color = 1
    handle_led_client(type,mode,color)

def button_led_normal_blue():
    type = 1
    mode = 2
    color = 3
    handle_led_client(type,mode,color)


if __name__ == "__main__":
    rospy.loginfo("This is a Led Test using ros")
    
    head_led_turn_on_red()
    time.sleep(3)
    head_led_turn_off_blue()
    time.sleep(3)
    button_led_blink_red()
    time.sleep(3)
    button_led_normal_blue()    
        