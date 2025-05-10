import file


def make(path, requests_url, time, server_p):
    get_p = file.get_file_list(path)

    if get_p == 1:
        return 1
    if get_p == 2:
        return 2

    if server_p is None:
        server_p = "root\\"
    else:
        server_p = "root/" + server_p

    b = {
        "file": get_p,
        "time": time,
        "server_path": server_p,
        "requests_url": requests_url
    }

    return b