#include <rviz_panel_tutorial/demo_panel.hpp>
#include <QVBoxLayout>
#include <rviz_common/display_context.hpp>

namespace rviz_panel_tutorial {
    DemoPanel::DemoPanel(QWidget * parent): Panel(parent) {
        const auto layout = new QVBoxLayout(this);
        label_ = new QLabel("[no data]");
        button_ = new QPushButton("GO!");
        layout -> addWidget(label_);
        layout -> addWidget(button_);

        QObject::connect(button_, &QPushButton::released, this, &DemoPanel::buttonActivated);
    }

    DemoPanel::~DemoPanel() = default; 

    void DemoPanel::onInitialize() {
        node_ptr_ = getDisplayContext() -> getRosNodeAbstraction().lock();
        rclcpp::Node::SharedPtr node = node_ptr_ -> get_raw_node();
        publisher_ = node -> create_publisher<std_msgs::msg::String>("/output", 10);
        subscription_ = node -> create_subscription<std_msgs::msg::String>("/input", 10, std::bind(&DemoPanel::topicCallback, this, std::placeholders::_1));
    }

    void DemoPanel::topicCallback(const std_msgs::msg::String & msg) {
        label_ -> setText(QString(msg.data.c_str()));
    }

    void DemoPanel::buttonActivated() {
        auto message = std_msgs::msg::String();
        message.data = "Button clicked!";
        publisher_ -> publish(message);
    }
}

#include <pluginlib/class_list_macros.hpp>
PLUGINLIB_EXPORT_CLASS(rviz_panel_tutorial::DemoPanel, rviz_common::Panel)