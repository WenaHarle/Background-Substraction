from __future__ import annotations

import math
from typing import Dict, Iterable, Tuple

Point = Tuple[int, int]


class CentroidTracker:
    def __init__(self, max_distance: float = 50.0) -> None:
        self.max_distance = max_distance
        self.objects: Dict[int, Point] = {}
        self.next_id = 0

    def update(self, centroids: Iterable[Point]) -> Dict[int, Point]:
        remaining = list(centroids)

        previous_objects = dict(self.objects)
        for object_id, previous_centroid in previous_objects.items():
            nearest_idx = -1
            nearest_distance = float("inf")

            for idx, centroid in enumerate(remaining):
                distance = math.hypot(previous_centroid[0] - centroid[0], previous_centroid[1] - centroid[1])
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_idx = idx

            if nearest_idx >= 0 and nearest_distance < self.max_distance:
                self.objects[object_id] = remaining.pop(nearest_idx)
            else:
                self.objects.pop(object_id, None)

        for centroid in remaining:
            self.objects[self.next_id] = centroid
            self.next_id += 1

        return dict(self.objects)
