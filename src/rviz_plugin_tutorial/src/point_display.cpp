#include <rviz_plugin_tutorial/point_display.hpp>
#include <rviz_common/logging.hpp>

namespace rviz_plugin_tutorial {
    using rviz_common::properties::StatusProperty;

    void PointDisplay::onInitialize() {
        MFDClass::onInitialize();
        point_shape_ = std::make_unique<rviz_rendering::Shape>(rviz_rendering::Shape::Type::Cube, scene_manager_, scene_node_);
        color_property_ = std::make_unique<rviz_common::properties::ColorProperty>(
            "Point Color",
            QColor(36, 64, 142),
            "Color to draw the point.",
            this
        );
        updateStyle(); 
    }

    void PointDisplay::processMessage(const rviz_plugin_tutorial_msg::msg::Point2D::ConstSharedPtr msg) {
        RVIZ_COMMON_LOG_INFO_STREAM("We got a message with frame " << msg -> header.frame_id);

        Ogre::Vector3 position;
        Ogre::Quaternion orientation;

        if (!context_ -> getFrameManager() -> getTransform(msg -> header, position, orientation)) {
            RVIZ_COMMON_LOG_DEBUG_STREAM("Error transforming from fram '" + msg -> header.frame_id + "' to frame '" + qPrintable(fixed_frame_) + "'");
        }

        scene_node_ -> setPosition(position);
        scene_node_ -> setOrientation(orientation); 

        if (msg -> x < 0) {
            setStatus(StatusProperty::Warn, "Message", "I will complain about points with negative x values");
        } else {
            setStatus(StatusProperty::Ok, "Message", "OK");
        }

        Ogre::Vector3 point_pos;
        point_pos.x = msg -> x;
        point_pos.y = msg -> y;
        point_shape_ -> setPosition(point_pos);
    }

    void PointDisplay::updateStyle() {
        QColor color = color_property_->getColor();
        Ogre::ColourValue ogre_color(
            color.redF(), color.greenF(), color.blueF(), color.alphaF());
        point_shape_->setColor(ogre_color);
    }

}

#include <pluginlib/class_list_macros.hpp>
PLUGINLIB_EXPORT_CLASS(rviz_plugin_tutorial::PointDisplay, rviz_common::Display)