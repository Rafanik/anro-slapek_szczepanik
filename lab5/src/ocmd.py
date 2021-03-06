import sys
import rospy
import rospy
from lab2.srv import params_oint
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import json
from sensor_msgs.msg import *
from tf.transformations import *
from visualization_msgs.msg import Marker
from geometry_msgs.msg import PoseStamped
import math
import PyKDL as kdl
from tf.transformations import *
kat=0.2
xaxis, yaxis, zaxis = (1, 0, 0), (0, 1, 0), (0, 0, 1)
rotation = kdl.Rotation(1, 0, 0, 0, math.cos(kat), -math.sin(kat), 0, math.sin(kat), math.cos(kat))
translation = kdl.Vector(0,0,0.5)

time = 10
def kwadrat(radius):
    trajektoria(radius, radius, 0, 10)
    trajektoria(-radius, radius, 0, 10)
    trajektoria(-radius, -radius, 0, 10)
    trajektoria(radius, -radius, 0, 10)
    trajektoria(radius, radius, 0, 10)

def elipsa(x, y):
    i=0.0
    xi=0.0
    yi=y
    n=100
    for i in range(n):
	xi=x*math.cos(math.pi*2.0*i/n)
	yi=y*math.sin(math.pi*2.0*i/n)

	zi = 0
	frame = kdl.Frame( rotation, translation)
	vector = kdl.Vector(xi,yi,zi)
	end=frame*vector
	
        trajektoria(end.x(), end.y(),end.z(), 0.2)       

def trajektoria(x, y, z, time):
    rospy.wait_for_service('oint')
    try:
        trajektoria = rospy.ServiceProxy('oint', params_oint)
        resp1 = trajektoria(x, y, z, 0, 0, 0, time)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    elipsa(2.2,1.8)
    #kwadrat(1.7)
