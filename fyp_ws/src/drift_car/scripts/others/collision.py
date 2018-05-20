#!/usr/bin/env python
import rospy
from gazebo_msgs.msg import ContactsState
from sensor_msgs.msg import Image

from cv_bridge import CvBridge, CvBridgeError

def listener():
    rospy.init_node('collision', anonymous=True)
    while(True):
        # left_front = rospy.wait_for_message('/drift_car/collision/left_front', ContactsState, timeout=1)
        # right_front = rospy.wait_for_message('/drift_car/collision/right_front', ContactsState, timeout=1)
        # left_rear = rospy.wait_for_message('/drift_car/collision/left_rear', ContactsState, timeout=1)
        # right_rear = rospy.wait_for_message('/drift_car/collision/right_rear', ContactsState, timeout=1)

        # if (len(right_front.states)) >= 1:
        #     for contact in right_front.states:
        #         if not contact.collision2_name == "ground_plane::link::collision":
        #             print(contact.collision2_name)
        bridge = CvBridge()
        image = rospy.wait_for_message('/drift_car/camera/image_raw', Image, timeout=1)
        try:
            cv_image = bridge.imgmsg_to_cv2(image, "rgb8")
        except CvBridgeError as e:
            print(e)
        print(cv_image.shape)

if __name__ == '__main__':
    listener()
