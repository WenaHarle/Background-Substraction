from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class AppConfig:
    video_path: str = "fix.mp4"
    background_image_path: Optional[str] = "bac2.jpg"
    roi: Optional[Tuple[int, int, int, int]] = (60, 40, 280, 540)
    blur_kernel: Tuple[int, int] = (5, 5)
    threshold_value: int = 25
    min_area: int = 6000
    max_area: Optional[int] = 11000
    tracking_distance: float = 50.0
    frame_delay_ms: int = 30
    show_debug_windows: bool = True
