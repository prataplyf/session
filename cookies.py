from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/set')
def setcookies():
    resp = make_response('setting cookies')
    resp.set_cookie('language','python')
    return resp

@app.route('/get')
def getcookies():
    language = request.cookies.get('language')
    return 'selected language ' + language

if __name__ == "__main__":
    app.run(debug=True)