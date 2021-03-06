
#!/usr/bin/env python

""" 
SentryBot lets us know if an intruder walks past.
Author:Ryan LaPorte Bivek Kandel
Version:
"""

import rospy

from kobuki_msgs.msg import Sound
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import numpy as np


class SentryNode(object):
    """Monitor a vertical scan through the depth map and create an
    audible signal if the change exceeds a threshold.
    Subscribes:
         /camera/depth_registered/image
       
    Publishes:
        /mobile_base/commands/sound
    """

    def __init__(self):
        """ Set up the Sentry node. """
        rospy.init_node('sentry')
        self.cv_bridge = CvBridge()
        rospy.Subscriber('/camera/depth_registered/image',
                         Image, self.depth_callback, queue_size=1)
        self.sound_pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=1)
        self.sound = Sound()
        self.sound.value = 1
        self.prev = None
        self.avg = 0
        self.th = 1.3
        self.alpha = .9
        rospy.spin()

    def depth_callback(self, depth_msg):
        """ Handle depth callbacks. """

        # Convert the depth message to a numpy array
        depth = self.cv_bridge.imgmsg_to_cv2(depth_msg)
        curr = depth[:,depth_msg.width/2]
        # YOUR CODE HERE.
        
	if self.prev != None :
            depth_num = curr - self.prev
            depth_num = depth_num[~np.isnan(depth_num)]
            depth_num = np.linalg.norm(depth_num)
            self.avg = self.avg * self.alpha + depth_num * (1 - self.alpha)
	    print depth_num/self.avg
            if depth_num/self.avg > self.th :
                self.sound_pub.publish(self.sound)
        self.prev = curr
	
        # HELPER METHODS ARE GOOD.


if __name__ == "__main__":
    SentryNode()
