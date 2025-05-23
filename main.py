from datetime import datetime
import config


from flask import Flask, render_template, request, send_file, jsonify, abort
import make_html
import return_api


app = Flask(__name__)
application = app
root = config.root



@app.route('/')
def home():
    return render_template("index.html")


@app.route("/web/<path:subpath>")
@app.route('/web')
@app.route('/web/')
def webs(subpath=None):
    request_time = datetime.now()
    formatted_time = request_time.strftime('%Y-%m-%d %H:%M:%S')
    if subpath == "serviceworker.js":
        abort(404)

    if subpath is None:
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
    if subpath == "serviceworker.js":
        abort(404)

    if subpath is None:
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
    app.run(debug=config.debug, port=config.port)

