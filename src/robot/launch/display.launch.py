from launch import LaunchDescription
from launch_ros.actions import Node
import os 
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command

def generate_launch_description():
    package_name = 'robot'
    urdf_file_path = os.path.join(get_package_share_directory(package_name), 'urdf', 'robot.urdf')
    rviz_config_path = os.path.join(get_package_share_directory(package_name), 'rviz', 'display_config.rviz')

    if not os.path.exists(urdf_file_path):
        raise FileNotFoundError(f"URDF file not found: {urdf_file_path}")
    if not os.path.exists(rviz_config_path):
        raise FileNotFoundError(f"RViz config file not found: {rviz_config_path}")
    
    return LaunchDescription([
        Node(
            package = 'robot_state_publisher',
            executable = 'robot_state_publisher', 
            arguments = [urdf_file_path], 
            parameters=[{'robot_description': Command(['xacro ', urdf_file_path])}],
            output = 'screen'
        ), 
        Node(
            package = 'rviz2',
            executable = 'rviz2', 
            arguments = ['-d', rviz_config_path], 
            output = 'screen'
        ), 
        Node(
            package = 'robot', 
            executable = 'odometry_publisher', 
            name = 'odometry_publisher', 
            output = 'screen'
        ), 
        Node(
            package = 'robot',
            executable = 'odometry_subscriber', 
            name = 'odometry_subscriber', 
            output = 'screen'
        )
    ])