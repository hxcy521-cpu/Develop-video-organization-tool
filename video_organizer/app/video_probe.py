"""视频元数据提取模块（占位）。"""

from pathlib import Path


def probe_video(video_path: Path) -> dict:
    """返回视频元数据（占位实现）。"""
    return {"path": str(video_path), "duration": None, "resolution": None, "codec": None}
