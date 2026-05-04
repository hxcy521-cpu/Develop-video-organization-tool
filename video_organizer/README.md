# Video Organizer

这个仓库只保留“视频素材整理工具”项目。

## 目录结构

```text
video_organizer/
  main.py
  requirements.txt
  build_exe.bat
  README.md
  app/
    ui_main.py
    scanner.py
    video_probe.py
    organizer.py
    duplicate_checker.py
    report_exporter.py
    utils.py
```

## 快速开始

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 运行程序：
   ```bash
   python main.py
   ```

## Windows 打包 EXE

在 `video_organizer` 目录下执行：

```bat
build_exe.bat
```

打包成功后输出文件位于：

```text
dist/video_organizer.exe
```

## 模块说明

- `app/ui_main.py`：主界面入口与交互逻辑。
- `app/scanner.py`：扫描视频目录并收集文件信息。
- `app/video_probe.py`：提取视频元数据（时长、分辨率、编码等）。
- `app/organizer.py`：执行分类整理与移动/复制策略。
- `app/duplicate_checker.py`：重复素材检测。
- `app/report_exporter.py`：导出整理结果报表。
- `app/utils.py`：通用工具函数。
