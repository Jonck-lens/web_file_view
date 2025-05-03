from jinja2 import Environment, FileSystemLoader

from file import file

# 创建模板环境
env = Environment(
    loader=FileSystemLoader("templates"),  # 模板目录
    autoescape=True,  # 自动HTML转义
    trim_blocks=True,  # 去除块首尾空白
    lstrip_blocks=True  # 去除块左侧空白
)

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

    with open('templates\\zh_ch_moban.html', 'r', encoding='utf-8') as files:
        template = files.read()

    files = make_file(get_p, url)

    # 定义替换数据
    data = {
        "{h3}": "当前路径： "+url,
        "{time}": "请求开始时间： "+time,
        "{file_var}": "文件（夹）数量： " + str(len(get_p)),
        "{server_path}": "服务器内部路径： " + server_p,
        "{file}": files
    }

    # 执行替换
    modified_html = template
    for placeholder, value in data.items():
        modified_html = modified_html.replace(placeholder, value)

    # 输出结果
    return modified_html
