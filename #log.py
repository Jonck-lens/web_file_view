import os
from datetime import datetime

import config

output = config.debug

waring = "waring"
error = "error"
info = "info"

class Logger:
    def __init__(self):
        self.log_file = 'log.log'
        self._ensure_log_file_exists()

    def _color(self, log_type):
        a = ""
        if log_type == "waring":
            a = "\033[33m[waring]\033[0m ->"
        elif log_type == "error":
            a = "\033[31m[error] \033[0m ->"
        elif log_type == "info":
            a = "\033[36m[info]  \033[0m ->"
        else:
            a = "\033[38m"
        return a

    def _ensure_log_file_exists(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w'):
                pass


    def log(self, content, log_type):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} [{log_type}] : {content}\n"

        # 写入文件
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

        # 控制台输出
        if output:
            color = self._color(log_type)
            print(f"{timestamp} {color} {content}")
        return True



# 外部调用接口
def write_log(content, log_type='info'):
    logger = Logger()
    return logger.log(content, log_type)
