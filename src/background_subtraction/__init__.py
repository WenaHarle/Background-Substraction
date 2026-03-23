"""Background subtraction and lightweight object counting package."""

from .app import run_application
from .config import AppConfig

__all__ = ["AppConfig", "run_application"]
