import rospy
from ubt_msgs.srv import *

def vision_handle_client(x):
    rospy.wait_for_client('vision_ai_event')
    
    try:
        face1 = rospy.ServiceProxy('vision_ai_event',vision_ai_event)
        resp1 =face1(x)
        return resp1.rc
    except rospy.ServiceException as e:
        rospy.logerr("Service Call Failed:{e}")

if __name__ == "__main__":
    rospy.loginfo("This is a Face Analysis test using ros")
    
    x = "face_analyse"
    rstr = vision_handle_client(x)
    
    rospy.loginfo(f"in: {x}  return: {rstr}")