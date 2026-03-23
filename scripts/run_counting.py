import argparse

from src.background_subtraction import AppConfig, run_application


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run background subtraction + object counting")
    parser.add_argument("--video", default="fix.mp4", help="Path to input video")
    parser.add_argument("--background", default="bac2.jpg", help="Path to background image")
    parser.add_argument("--min-area", type=int, default=6000, help="Minimum contour area")
    parser.add_argument("--max-area", type=int, default=11000, help="Maximum contour area")
    parser.add_argument("--threshold", type=int, default=25, help="Binary threshold value")
    parser.add_argument("--distance", type=float, default=50.0, help="Maximum centroid distance for tracking")
    parser.add_argument("--no-ui", action="store_true", help="Disable OpenCV debug windows")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    config = AppConfig(
        video_path=args.video,
        background_image_path=args.background,
        threshold_value=args.threshold,
        min_area=args.min_area,
        max_area=args.max_area,
        tracking_distance=args.distance,
        show_debug_windows=not args.no_ui,
    )
    run_application(config)


if __name__ == "__main__":
    main()
