import rclpy 
from rclpy.node import Node 
from nav_msgs.msg import Odometry 
from geometry_msgs.msg import Pose, Twist
from std_msgs.msg import Header

class Odometry_subscriber(Node):
    def __init__(self):
        super().__init__('odometry_subscriber')
        self.Odom_subscriber = self.create_subscription(Odometry, '/Odometry', self.subscriber_callback, 10)

    def subscriber_callback(self, msg):

        position_x = msg.pose.pose.position.x
        position_y = msg.pose.pose.position.y
        position_z = msg.pose.pose.position.z

        orientation_w = msg.pose.pose.orientation.w
        orientation_z = msg.pose.pose.orientation.z

        linear_vel_x = msg.twist.twist.linear.x 
        angular_vel_z = msg.twist.twist.angular.z 

        self.get_logger().info(
            f"Receiving: "
            f"Position: (x = {position_x:.2f}, y = {position_y:.2f}, z = {position_z:.2f}) "
            f"Orientation: (w = {orientation_w:.2f}, z = {orientation_z:.2f}) "
            f"Velocity: (linear = {linear_vel_x:.2f}, angular = {angular_vel_z:.2f}) "
        )
        
def main(args = None):
    rclpy.init(args = args)
    odometry_subscriber = Odometry_subscriber()
    rclpy.spin(odometry_subscriber)
    odometry_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__': 
    main()