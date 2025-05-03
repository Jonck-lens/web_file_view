from datetime import datetime

from flask import Flask, render_template, request, send_file, jsonify
import make_html
import return_api

app = Flask(__name__)

root = "D:\\"

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/web/<path:subpath>")
@app.route('/web')
@app.route('/web/')
def webs(subpath=None):
    request_time = datetime.now()
    formatted_time = request_time.strftime('%Y-%m-%d %H:%M:%S')

    if (subpath is None) or (subpath == "serviceworker.js"):
        p = root
    else:
        if root[-1] == "\\" or "/":
            p = root + subpath
        else:
            p = root + "\\" + subpath

    request_url = request.path
    return_p = make_html.make(p, request_url, formatted_time, subpath)

    if return_p == 1:
        return send_file(p, as_attachment=True)
    if return_p == 2:
        return render_template("error.html")

    return return_p

@app.route("/api/<path:subpath>")
@app.route('/api')
@app.route('/api/')
def api(subpath=None):
    request_time = datetime.now()
    formatted_time = request_time.strftime('%Y-%m-%d %H:%M:%S')


    if (subpath is None) or (subpath == "serviceworker.js"):
        p = root
    else:
        if root[-1] == "\\":
            p = root + subpath
        else:
            p = root + "\\" + subpath

    request_url = request.path
    return_p = return_api.make(p, request_url, formatted_time, subpath)

    if return_p == 1:
        return send_file(p)
    if return_p == 2:
        return render_template("error.html")

    return jsonify(return_p)

if __name__ == '__main__':
    app.run(debug=True, port=41040)
