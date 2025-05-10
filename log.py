import os
from datetime import datetime

output = True


class Logger:
    def __init__(self):
        self.log_file = 'log.log'
        self._ensure_log_file_exists()

    def _ensure_log_file_exists(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w'): pass

    def _get_color_code(self, log_type):
        colors = {
            'info  ': '\033[36m',  # 蓝色
            'waring': '\033[33m',  # 黄色
            'error ': '\033[31m'  # 红色
        }
        return colors.get(log_type, '\033[0m')

    def log(self, content, log_type='info'):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} [{log_type}] : {content}\n"

        # 写入文件
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

        # 控制台输出
        if output:
            color = self._get_color_code(log_type)
            reset = '\033[0m'
            print(f"{timestamp} {color}[{log_type}] {content}")  #  <<< ------------------------------
        return True


# 外部调用接口
def write_log(content, log_type='info'):
    logger = Logger()
    return logger.log(content, log_type)


write_log('ddddasdaw')
write_log('waddddddddd', 'waring')
write_log('awdaaaaaargtsssssssss', 'error')
