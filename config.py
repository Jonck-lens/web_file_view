import configparser
import sys

port = 41040
debug = False
web_language = "zh_cn"
root = "D:\\"
#log_print = True

config_file = "config.ini"
if True:
    """简单的配置文件读取，不存在则创建"""
    config = configparser.ConfigParser()
    default = ["[server]\n",
               "\n",
               "\n",
               "# 设置端口\n",
               "# 接受数字类型，建议 10000-65565\n",
               '#(set a port, Accept number type, suggested 10000-65565)\n',
               "port = 41040\n",
               "\n",
               "# 是否启动debug\n",
               "# 接受 T(True) F(False)\n",
               '#(Whether debug is enabled and accepts T or F)\n',
               "debug = F\n",
               "\n",
               "# web 目录浏览的界面语言\n",
               "# 接受 zh_cn en_us\n",
               '#(web interface language, accepts zh_cn , en_us)\n',
               "web_language = zh_cn\n",
               '\n',
               "# root 根路径\n",
               '# 建议路径最后包含”\“，例如”D:\“, "D:\\me\\",因为可能会发生某些意外\n',
               '#(set root path, It is recommended that the path include "\\" at the end, such as "D:\\ ", "D:\\me\\", because something might happen)\n',
               'root = C:\\users\n',
               '\n',
               '# 设定是否输出日志（这个选项暂时弃用）\n',
               '# 接受 T(True) F(False)',
               '#(Whether to log output, accept T or F)\n',
               '#log_print = T\n',
               '\n\n',
               '# tip: 对于路径，语言选项，不建议建议包括 "" 或 ''\n',
               '# tip: For path, language options, not recommended Recommended include "" or '''
               ]



    try:
        # 尝试读取配置文件
        config.read(config_file)

        # 如果文件不存在，创建默认配置
        if not config.read(config_file):
            print(f"配置文件 {config_file} 不存在，将创建新文件")
            with open(config_file, 'w') as f:
                f.writelines(default)
            print("你需要重启本软件")
            sys.exit(0)

        port = config['server']['port']
        _debug = config['server']['debug']
        web_language = config['server']['web_language']
        root = config['server']['root']

        if _debug == "T":
            debug = True
        else:
            debug = False


    except Exception as e:
        print(f'发生错误{str(e)}')
