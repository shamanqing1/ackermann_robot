from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():
    print(os.environ["GAZEBO_MODEL_PATH"])
    ld = LaunchDescription()

    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'display.launch.py']),
        launch_arguments={
            'urdf_package': 'ackermann_robot_description',
            'urdf_package_path': PathJoinSubstitution(['urdf', 'ackermann_robot.urdf.xacro'])}.items()
    ))
    return ld