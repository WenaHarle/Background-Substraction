# Background Subtraction Object Counting

A cleaned and structured version of an older computer vision project for simple motion detection and object counting using OpenCV.

## What This Project Does

- Detects moving objects from a static background reference
- Filters noisy contours using area thresholds
- Tracks object centroids frame-to-frame
- Assigns stable IDs to detected objects

## Project Structure

```text
.
|-- docs/
|   `-- PROJECT_STRUCTURE.md
|-- legacy/
|   |-- Background Substraction
|   |-- fix.py
|   |-- menghitung luas.py
|   `-- object tracking.py
|-- scripts/
|   `-- run_counting.py
|-- src/
|   `-- background_subtraction/
|       |-- __init__.py
|       |-- app.py
|       |-- config.py
|       |-- detector.py
|       `-- tracker.py
|-- main.py
`-- requirements.txt
```

## Requirements

- Python 3.9+
- OpenCV
- NumPy

Install dependencies:

```bash
pip install -r requirements.txt
```

## Quick Start

Run with defaults:

```bash
python main.py
```

Run with custom options:

```bash
python scripts/run_counting.py --video fix.mp4 --background bac2.jpg --min-area 5000 --max-area 12000 --threshold 25
```

## Configuration Options

You can tune behavior from CLI options or by editing `AppConfig` in `src/background_subtraction/config.py`:

- `video_path`: input video file
- `background_image_path`: static background image
- `roi`: region of interest `(x1, y1, x2, y2)`
- `threshold_value`: binary threshold for motion mask
- `min_area`, `max_area`: contour area filter
- `tracking_distance`: centroid matching radius between frames

## Legacy Scripts

Original scripts are preserved under `legacy/` for reference and comparison.

## Notes

- Press `Esc` to stop the OpenCV window loop.
- The current tracker is lightweight centroid-based tracking. For crowded scenes or occlusions, consider adding Kalman filtering + Hungarian assignment.
