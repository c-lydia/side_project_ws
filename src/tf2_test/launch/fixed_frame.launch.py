import os 

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node 

def generate_launch_description():
    nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('tf2_test'), 'launch'), 
        '/turtle_tf2.launch.py'])
    )

    return LaunchDescription([
        nodes, 
        Node (
            package = 'tf2_test',
            executable = 'fixed_frame_broadcaster',
            name = 'fixed_broadcaster'
        )
    ])