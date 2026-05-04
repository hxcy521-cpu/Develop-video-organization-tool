"""整理报告导出模块。"""

from pathlib import Path


def export_report(report_text: str, output_file: Path) -> Path:
    """导出文本报告。"""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(report_text, encoding="utf-8")
    return output_file
