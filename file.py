import os
import time
from typing import Any



def get_file_list(dir_path: str) -> None | list[dict[str, str | int | None | Any] | dict[str, str | int]] | list[
    Any] | int:
    """
    获取目录内容列表（包含文件/文件夹信息）
    返回格式: [
        {
            'name': 名称,
            'type': '<dir>'或'<file>',
            'size': 文件大小(字节)，文件夹为None,
            'create_time': 创建时间
        },
        ...
    ]
    """
    try:
        if os.path.isfile(dir_path):
            return 1

        if not os.path.exists(dir_path):
            raise FileNotFoundError(f"路径不存在: {dir_path}")

        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"不是有效目录: {dir_path}")

        print(dir_path)

        items = []
        for item in os.listdir(dir_path):
            full_path = os.path.join(dir_path, item)
            stat = os.stat(full_path)

            if os.path.isdir(full_path):
                items.append({
                    'name': item,
                    'type': '<dir>',
                    'size': '-',
                    'create_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_ctime))
                })
            else:
                items.append({
                    'name': item,
                    'type': '<file>',
                    'size': stat.st_size,
                    'create_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_ctime))
                })

        return items if items else []

    except Exception as e:
        print(f"错误: {str(e)}")
        return 2

"""
result = get_file_list("D:\\")
if result:
    for item in result:
        size = "-" if item['type'] == '<dir>' else f"{item['size']} bytes"
        print(f"{item['type']:^6} | {item['name']:>30} | {size:>20} | {item['create_time']}")

"""