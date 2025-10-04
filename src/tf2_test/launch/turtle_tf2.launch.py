from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.substitutions import LaunchConfiguration 
from launch.actions import DeclareLaunchArgument

def generate_launch_description(): 
    return LaunchDescription([
        Node(
            package = 'turtlesim',
            executable = 'turtlesim_node', 
            name = 'sim'
        ),
        Node(
            package = 'tf2_test',
            executable = 'turtle_tf2_broadcaster', 
            name = 'broadcaster1', 
            parameters = [{'turtlename': 'turtle1'}]
        ), 
        DeclareLaunchArgument(
            'target_frame', 
            default_value = 'turtle1',
            description = 'target fame name'
        ), 
        Node(
            package = 'tf2_test',
            executable = 'turtle_tf2_broadcaster', 
            name = 'broadcaster2', 
            parameters = [{'turtlename': 'turtle2'}]
        ), 
        Node(
            package = 'tf2_test', 
            executable = 'turtle_tf2_listener', 
            name = 'listener', 
            parameters = [{'target_frame': LaunchConfiguration('target_frame')}]
        )
    ])