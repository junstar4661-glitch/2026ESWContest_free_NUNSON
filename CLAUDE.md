# CLAUDE.md — 개발 지침

제24회 임베디드SW경진대회 자유공모 출품작 **도와드림(DOWADREAM)** 저장소의 작업 지침입니다.

## 프로젝트
책상 거치형 5축 로봇팔 비서. 요청을 받아 물건을 인식·파지·전달하고, 책상 상태를 상시 감시합니다.
기반 플랫폼의 출처와 이번 대회 개발 범위는 `README.md` 0장을 참고하십시오.

## 환경
- ROS 2 Humble / Ubuntu 22.04, Docker 컨테이너 안에서만 빌드·실행
- 진입: `docker exec -it ros2_humble bash`
- 빌드: `cd /ros2_ws && colcon build --symlink-install && source install/setup.bash`

## 패키지 책임
| 패키지 | 책임 |
| --- | --- |
| `robot_arm_msgs` | 노드 간 메시지 규격 |
| `robot_arm_description` | URDF · 좌표계 · 메시 · 카메라 TF |
| `robot_arm_moveit_config` | MoveIt 설정 |
| `dynamixel_control` | 작업 FSM · 자체 DLS IK · 서보 구동 · 파지 판정 |
| `robot_arm_perception` | YOLOv8-seg 인식 · 3D 좌표 · 마스크 PCA 자세 |
| `robot_arm_gui` | 브라우저 관제 (읽기 전용) |
| `robot_manual_gui` | 수동 조작 · 실기 시험 |
| `pick_test_pkg` | 파지 시퀀스 실기 검증 |
| `robot_vla` | 언어 지시 기반 동작 생성 (설계 단계) |

## 규칙
1. 실서보를 움직이는 변경은 반드시 하드웨어 없는 경로(RViz · fake publisher)에서 먼저 확인한다.
2. FSM을 우회해 `/dynamixel/goal_position`에 직접 발행하는 경로는 벤치 전용이며 대회 launch에 넣지 않는다.
3. 관절 리밋·캘리브레이션 값은 실측 근거 없이 바꾸지 않는다.
4. 외부에서 받은 자산(`vendor/`)은 원본을 수정하지 않고 통합 계층에서 재지정한다.
5. 커밋 전 `colcon test`로 각 패키지 테스트를 통과시킨다.
