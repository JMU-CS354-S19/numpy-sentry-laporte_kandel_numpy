#!/usr/bin/env python

""" 
SentryBot lets us know if an intruder walks past.

Author: 
Version:
"""

import rospy

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
	rospy.Publisher('/mobile_base/commands/sound',Image,queue_size=1)
	prev = None
	current = None
        rospy.spin()

    def depth_callback(self, depth_msg):
        """ Handle depth callbacks. """

        # Convert the depth message to a numpy array

	if(self.current != None)
		prev = current

        depth = self.cv_bridge.imgmsg_to_cv2(depth_msg)

	

        # YOUR CODE HERE.
	
	depthNum = np.array([depth])
	size = np.shape
	#depthMid = depthNum[:,1:2]
	colMid = size[1]/2
	current = colMid
	sumPrev = sumPrev[~np.isnan(sumPrev)]
	sumCur = sumCur[~np.isnam(sumCur)]
	sumPrev = np.sum(prev)
	sumCur = np.sum(current)
	depthVal = np.absolute(current) - np.absolute(prev)
	

	
	
	
	
	
        # HELPER METHODS ARE GOOD.


if __name__ == "__main__":
    SentryNode()
