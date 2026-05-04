"""视频整理模块。"""

from pathlib import Path


def organize_files(files: list[Path], output_dir: Path) -> list[Path]:
    """按规则整理文件（占位实现，当前不移动文件）。"""
    output_dir.mkdir(parents=True, exist_ok=True)
    return files
