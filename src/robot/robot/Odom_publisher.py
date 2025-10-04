import rclpy 
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Twist, TransformStamped
from std_msgs.msg import Header 
from tf2_ros import TransformBroadcaster
import math

class Odometry_publisher(Node): 
    def __init__(self):
        super().__init__('odometry_publisher')
        self.Odom_publisher = self.create_publisher(Odometry, '/Odometry', 10)
        self.timer = self.create_timer(0.1, self.publisher_callback)
        self.tf_broadcaster = TransformBroadcaster(self)

        self.position_x = 0.0
        self.position_y = 0.0
        self.position_z = 0.0

        self.orientation_w = 1.0
        self.orientation_z = 0.0

        self.vel_linear_x = 0.2
        self.vel_angular_z = 0.5

    def publisher_callback(self): 
        self.position_x += self.vel_linear_x * math.cos(self.orientation_z) * 0.1
        self.position_y += self.vel_linear_x * math.sin(self.orientation_z) * 0.1

        self.orientation_z += self.vel_angular_z * 0.1

        self.orientation_z = math.atan2(math.sin(self.orientation_z), math.cos(self.orientation_z))

        msg = Odometry()
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'odom'

        msg.pose.pose.position.x = self.position_x
        msg.pose.pose.position.y = self.position_y
        msg.pose.pose.position.z = self.position_z

        msg.pose.pose.orientation.w = self.orientation_w
        msg.pose.pose.orientation.z = self.orientation_z

        msg.twist.twist.linear.x = self.vel_linear_x
        msg.twist.twist.angular.z = self.vel_angular_z

        self.Odom_publisher.publish(msg)
        self.publish_tf2()
        self.get_logger().info(
        f"Publishing: "
        f"Position: (x={msg.pose.pose.position.x:.2f}, y={msg.pose.pose.position.y:.2f}, z={msg.pose.pose.position.z:.2f}), "
        f"Orientation: (w={msg.pose.pose.orientation.w:.2f}, z={msg.pose.pose.orientation.z:.2f}), "
        f"Linear Velocity: (x={msg.twist.twist.linear.x:.2f}), "
        f"Angular Velocity: (z={msg.twist.twist.angular.z:.2f})"
        )

    def publish_tf2(self):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'

        t.transform.translation.x = self.position_x
        t.transform.translation.y = self.position_y
        t.transform.translation.z = self.position_z

        t.transform.rotation.w = math.cos(self.orientation_z/2)
        t.transform.rotation.z = math.sin(self.orientation_z/2)

        self.tf_broadcaster.sendTransform(t)

def main(args = None):
    rclpy.init(args = args)
    odometry_publisher = Odometry_publisher()
    rclpy.spin(odometry_publisher)
    odometry_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()