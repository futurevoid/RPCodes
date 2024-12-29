import rospy
from std_msgs.msg import Int32

def button_times_callback(msg):
    rospy.loginfo(f"button subscriber: detect button times: {msg.data}")
    
if __name__ == '__main__':
    rospy.loginfo("This is a button msg test using ros")
    
    rospy.init_node('button')
    
    rospy.Subscriber('hal_button_info', Int32, button_times_callback)
    
    rospy.spin()