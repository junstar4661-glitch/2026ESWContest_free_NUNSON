#!/bin/bash
# 대상 물체 파지용 인식 노드 실행.
ros2 run robot_arm_perception perception_node --ros-args -p model_name:=box -p camera_mode:=realsense -p pick_min_conf:=0.5 -p require_depth:=true
