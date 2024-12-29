import rospy
from ubt_msgs.srv import *

def tts_handle_client(handle,msg,interrupt,Async):
    rospy.wait_for_service('voice_tts_start')
    try:
        tts_function = rospy.ServiceProxy('voice_tts_start', voice_tts_start)
        resp1 = tts_function(handle,1,msg,interrupt,Async)
        return resp1.rc
    except rospy.ServiceException as e:
        rospy.logerr(f"Service Call failed: {e}")

def tts_to_speak(msg):
    handle = 1
    
    interrupt = 1
    
    Async = False
    
    tts_handle_client(handle,msg.interrupt,Async)
    
if __name__ == "__main__":
    rospy.loginfo("This is a TTS test using ros")
    
    tts_to_speak("0xlol was here")