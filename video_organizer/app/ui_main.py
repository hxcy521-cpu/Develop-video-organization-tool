"""主界面模块。"""

from tkinter import BOTH, Tk, ttk


def run_app() -> None:
    """启动一个最小可用 GUI，便于打包后直接运行 EXE。"""
    root = Tk()
    root.title("Video Organizer")
    root.geometry("640x360")

    frame = ttk.Frame(root, padding=24)
    frame.pack(fill=BOTH, expand=True)

    title = ttk.Label(frame, text="视频素材整理工具", font=("Microsoft YaHei UI", 18, "bold"))
    title.pack(pady=(20, 8))

    desc = ttk.Label(
        frame,
        text="应用已启动。后续可在 app/ 模块中继续实现扫描、去重、整理和报表导出逻辑。",
        wraplength=560,
        justify="center",
    )
    desc.pack(pady=(0, 20))

    root.mainloop()
