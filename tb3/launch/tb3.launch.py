import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    tb3_bringup_pkg_share = get_package_share_directory('turtlebot3_bringup')
    usb_cam_pkg_share = get_package_share_directory('usb_cam')

    tb3_bringup_launch_path = os.path.join(tb3_bringup_pkg_share, 'launch')
    usb_cam_launch_path = os.path.join(usb_cam_pkg_share, 'launch')

    tb3_bringup_launch_path_run = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([tb3_bringup_launch_path, '/robot.launch.py'])
    )

    usb_cam_run = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([usb_cam_launch_path, '/camera.launch.py'])
    )

    tb3_teleop_node = Node(
        package='turtlebot3_teleop',
        executable='teleop_keyboard',
        name='teleop_keyboard',
        output='screen'
    )

    ld = LaunchDescription()

    ld.add_action(tb3_bringup_launch_path_run)
    ld.add_action(usb_cam_run)
    ld.add_action(tb3_teleop_node)

    return ld
