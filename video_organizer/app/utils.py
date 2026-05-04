"""通用工具函数。"""

from datetime import datetime, timezone


def utc_now_iso() -> str:
    """返回 UTC 当前时间的 ISO 字符串。"""
    return datetime.now(timezone.utc).isoformat()
