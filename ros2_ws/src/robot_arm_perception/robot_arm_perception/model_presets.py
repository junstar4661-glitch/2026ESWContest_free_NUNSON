"""YOLO 모델 preset (perception_node 전용).

model_path/classes/pick_classes/task 를 한 묶음으로 관리해, perception_node 를
model_name 하나만 바꿔 launch할 수 있게 한다. 새 대상 물체용 모델을 추가할 때는
이 dict에 항목만 추가하면 된다(gripper_presets.py와 동일한 패턴).

`task`는 YOLO(model, task=...) 생성자에 그대로 전달된다(perception_node 참고) — 2026-07-22
TensorRT 백엔드(backend='trt') 실측으로 발견: .engine 파일은 task 메타데이터를 보존하지
않아 ultralytics가 자동으로 'detect'로 잘못 추정하고, seg 모델(box)이면 이때 r0.masks가
조용히 None이 돼 markerless pose(translation/PCA orientation)가 깨진다(에러 없이 그냥
빈 값). task를 preset에 박아 명시적으로 넘기면 .pt/.engine 둘 다 안전하다 — 새 preset
추가 시 반드시 이 필드도 채울 것.
"""

MODEL_PRESETS = {
    "box": {
        # seg 모델(1클래스 box-segmentation) → markerless pose(translation + PCA yaw) 전체 활성.
        "model_path": "src/robot_arm_perception/models/best.pt",
        "classes": "box-segmentation",
        "pick_classes": "box-segmentation",
        "task": "segment",
    },
}

DEFAULT_MODEL = "box"


def get_preset(model_name, logger=None):
    preset = MODEL_PRESETS.get(model_name)
    if preset is None:
        if logger is not None:
            logger.warn(
                f"Unknown model_name '{model_name}', falling back to '{DEFAULT_MODEL}'"
            )
        preset = MODEL_PRESETS[DEFAULT_MODEL]
    return preset
