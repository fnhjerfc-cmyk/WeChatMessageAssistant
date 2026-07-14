from pathlib import Path
from datetime import datetime


class LoggerService:
    def __init__(self):
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        self.log_file = log_dir / "app.log"

    def _write(self, level, message):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = f"[{now}] [{level}] {message}"

        # 输出到终端
        print(text)

        # 写入日志文件
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(text + "\n")

    def info(self, message):
        self._write("INFO", message)

    def warning(self, message):
        self._write("WARNING", message)

    def error(self, message):
        self._write("ERROR", message)