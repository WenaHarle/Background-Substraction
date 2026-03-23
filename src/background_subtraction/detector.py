from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple

import cv2
import numpy as np

BoundingBox = Tuple[int, int, int, int]


@dataclass
class DetectionResult:
    mask: np.ndarray
    boxes: List[BoundingBox]
    centroids: List[Tuple[int, int]]


class MotionDetector:
    def __init__(
        self,
        reference_frame: np.ndarray,
        blur_kernel: Tuple[int, int] = (5, 5),
        threshold_value: int = 25,
        min_area: int = 6000,
        max_area: Optional[int] = None,
    ) -> None:
        self.blur_kernel = blur_kernel
        self.threshold_value = threshold_value
        self.min_area = min_area
        self.max_area = max_area
        self.reference_gray = self._preprocess(reference_frame)

    def _preprocess(self, frame: np.ndarray) -> np.ndarray:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.GaussianBlur(frame_gray, self.blur_kernel, 0)

    def detect(self, frame: np.ndarray) -> DetectionResult:
        frame_gray = self._preprocess(frame)
        difference = cv2.absdiff(self.reference_gray, frame_gray)
        _, mask = cv2.threshold(difference, self.threshold_value, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        boxes: List[BoundingBox] = []
        centroids: List[Tuple[int, int]] = []

        for contour in contours:
            area = cv2.contourArea(contour)
            if area < self.min_area:
                continue
            if self.max_area is not None and area > self.max_area:
                continue

            x, y, w, h = cv2.boundingRect(contour)
            boxes.append((x, y, w, h))
            centroids.append((x + w // 2, y + h // 2))

        return DetectionResult(mask=mask, boxes=boxes, centroids=centroids)
