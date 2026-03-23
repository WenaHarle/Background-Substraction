from __future__ import annotations

from typing import Tuple

import cv2

from .config import AppConfig
from .detector import MotionDetector
from .tracker import CentroidTracker


def _safe_crop(frame, roi: Tuple[int, int, int, int]):
    x1, y1, x2, y2 = roi
    return frame[y1:y2, x1:x2]


def _draw_overlays(frame, boxes, tracked_objects):
    for x, y, w, h in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 225), 2)
        cv2.putText(frame, f"area={w * h}", (x, y - 8), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 255, 0), 1)

    for object_id, (cx, cy) in tracked_objects.items():
        cv2.circle(frame, (cx, cy), 4, (255, 255, 0), -1)
        cv2.putText(frame, str(object_id), (cx + 6, cy + 8), cv2.FONT_HERSHEY_PLAIN, 1.2, (255, 255, 0), 1)


def run_application(config: AppConfig) -> None:
    cap = cv2.VideoCapture(config.video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Failed to open video file: {config.video_path}")

    detector = None
    tracker = CentroidTracker(max_distance=config.tracking_distance)

    if config.background_image_path:
        bg_image = cv2.imread(config.background_image_path)
        if bg_image is None:
            raise RuntimeError(f"Failed to read background image: {config.background_image_path}")
        reference_frame = _safe_crop(bg_image, config.roi) if config.roi else bg_image
        detector = MotionDetector(
            reference_frame=reference_frame,
            blur_kernel=config.blur_kernel,
            threshold_value=config.threshold_value,
            min_area=config.min_area,
            max_area=config.max_area,
        )

    while True:
        ok, frame = cap.read()
        if not ok or frame is None:
            break

        working_frame = _safe_crop(frame, config.roi) if config.roi else frame

        if detector is None:
            detector = MotionDetector(
                reference_frame=working_frame,
                blur_kernel=config.blur_kernel,
                threshold_value=config.threshold_value,
                min_area=config.min_area,
                max_area=config.max_area,
            )

        result = detector.detect(working_frame)
        tracked = tracker.update(result.centroids)

        _draw_overlays(working_frame, result.boxes, tracked)

        if config.show_debug_windows:
            cv2.imshow("frame", frame)
            cv2.imshow("roi", working_frame)
            cv2.imshow("mask", result.mask)

        key = cv2.waitKey(config.frame_delay_ms)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
