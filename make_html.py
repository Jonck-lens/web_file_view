from jinja2 import Environment, FileSystemLoader

import config
import file

# 创建模板环境
env = Environment(
    loader=FileSystemLoader("templates"),  # 模板目录
    autoescape=True,  # 自动HTML转义
    trim_blocks=True,  # 去除块首尾空白
    lstrip_blocks=True  # 去除块左侧空白
)


if config.web_language == "zh_cn":
    with open('templates\\zh_ch_moban.html', 'r', encoding='utf-8') as files:
        template = files.read()
else:
    with open('templates\\en_us_moban.html', 'r', encoding='utf-8') as files:
        template = files.read()


def make_file(file_list, requests_url):
    c = []
    d = 0
    for item in file_list:
        name = item["name"]
        name = f'<a href="{requests_url}/{name}">{name}</a>'

        if item['type'] == "<file>":
            types = " "
        else:
            types = "dir"

        size = item['size']

        if d == 0 or d % 2 == 0:
            a = '<tr style="background: #D0D0D0"><td>' + types + "</td><td>" + name +"</td><td>"+ str(size) + "</td><td>" + item['create_time'] + "</td></tr>"
        else:
            a = '<tr><td>' + types + "</td><td>" + name +"</td><td>"+ str(size) + "</td><td>" + item['create_time'] + "</td></tr>"
        c.append(a)
        d += 1

    b = "".join(c)
    return b


def make(p, url, time, server_p):
    get_p = file.get_file_list(p)

    if get_p == 1:
        return 1
    if get_p == 2:
        return 2

    if server_p is None:
        server_p = "root\\"
    else:
        server_p = "root/ " + server_p

    files = make_file(get_p, url)

    data = {
        "{h3}": url,
        "{time}": time,
        "{file_var}": str(len(get_p)),
        "{server_path}": "" + server_p,
        "{file}": files
    }

    # 执行替换
    modified_html = template
    for placeholder, value in data.items():
        modified_html = modified_html.replace(placeholder, value)

    # 输出结果
    return modified_html
