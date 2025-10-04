from geometry_msgs.msg import TransformStamped

import rclpy
from rclpy.node import Node 

from tf2_ros import TransformBroadcaster

class FixedFrameBroadcaster(Node): 
    def __init__(self):
        super().__init__('fixed_frame_broadcaster')
        self.tf_broadcaster = TransformBroadcaster()
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self): 
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'turtle1'
        t.child_frame_id = 'carrot1'

        t.transform.translation.x = 0.0
        t.transform.translation.y = 2.0
        t.transform.translation.z = 0.0

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(t)

def main(): 
    rclpy.init()
    fixed_frame_broadcaster = FixedFrameBroadcaster()
    try: 
        rclpy.spin(fixed_frame_broadcaster)
    except KeyboardInterrupt: 
        pass 

    rclpy.shutdown()