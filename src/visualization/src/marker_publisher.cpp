#include <rclcpp/rclcpp.hpp>
#include <visualization_msgs/msg/marker.hpp>

class MarkerPublisher: public rclcpp::Node {
    public:
        MarkerPublisher(): Node("marker_publisher") {
            publisher_ = this -> create_publisher<visualization_msgs::msg::Marker>("visualization_marker", 10);
            timer_ = this -> create_wall_timer(
                std::chrono::seconds(1),
                std::bind(&MarkerPublisher::timer_callback, this)
            ); 
        }

    private:
        void timer_callback() {
            auto marker = visualization_msgs::msg::Marker();

            marker.header.frame_id = "/my_frame";
            marker.header.stamp = rclcpp::Clock().now();

            marker.ns = "basic_shape";
            marker.id = 0;

            marker.type = visualization_msgs::msg::Marker::SPHERE;

            marker.action = visualization_msgs::msg::Marker::ADD;

            marker.pose.position.x = 0;
            marker.pose.position.y = 0;
            marker.pose.position.z = 0;

            marker.pose.orientation.x = 0.0;
            marker.pose.orientation.y = 0.0;
            marker.pose.orientation.z = 0.0;
            marker.pose.orientation.w = 1.0;

            marker.scale.x = 1.0;
            marker.scale.y = 1.0;
            marker.scale.z = 1.0;

            marker.color.a = 1.0;
            marker.color.r = 0.0f;
            marker.color.g = 1.0f;
            marker.color.b = 0.0f;

            publisher_ -> publish(marker);
        }

        rclcpp::Publisher<visualization_msgs::msg::Marker>::SharedPtr publisher_;
        rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MarkerPublisher>());
    rclcpp::shutdown();
    return 0;
}