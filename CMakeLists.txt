cmake_minimum_required(VERSION 2.8.3)
project(udevadm_monitor)

find_package(catkin REQUIRED COMPONENTS
  rospy
  message_generation
  std_msgs
)

catkin_python_setup()

add_message_files(FILES Event.msg)

generate_messages(DEPENDENCIES std_msgs)
