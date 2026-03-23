# Project Structure Notes

## Why This Refactor

The previous code was written as multiple standalone scripts with repeated logic. This refactor separates responsibilities into modules so the project is easier to maintain and extend.

## Modules

- `config.py`: central runtime parameters with dataclass defaults.
- `detector.py`: frame preprocessing, background subtraction, contour extraction.
- `tracker.py`: centroid-based object ID assignment between frames.
- `app.py`: end-to-end execution loop, rendering, key handling, and resource cleanup.

## Entry Points

- `main.py`: simplest default entry point.
- `scripts/run_counting.py`: CLI entry point for quick experiments and parameter tuning.

## Legacy Folder

All original scripts are kept in `legacy/` untouched, so behavior and ideas from old versions can still be reviewed.
