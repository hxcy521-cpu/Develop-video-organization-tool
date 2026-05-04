"""视频目录扫描模块。"""

from pathlib import Path


def scan_videos(root: Path) -> list[Path]:
    """递归扫描常见视频文件。"""
    exts = {".mp4", ".mov", ".mkv", ".avi", ".mxf"}
    return [p for p in root.rglob("*") if p.suffix.lower() in exts]
