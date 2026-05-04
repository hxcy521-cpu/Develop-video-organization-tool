"""重复视频检测模块。"""

from pathlib import Path


def find_duplicates(files: list[Path]) -> dict[str, list[Path]]:
    """按文件名分组检查重复（占位实现）。"""
    groups: dict[str, list[Path]] = {}
    for file in files:
        groups.setdefault(file.name, []).append(file)
    return {name: paths for name, paths in groups.items() if len(paths) > 1}
