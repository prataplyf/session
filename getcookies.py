from flask import Flask, request, make_response
from datetime import datetime
import logging
# import webapp2

app = Flask(__name__)

@app.route('/')
def home():
    time = request.cookies.get('time', datetime.now())
    count = int(request.cookies.get('visit-count', 0))
    print(request.cookies)
    count += 1
    msg = "you have visited this page " + str(count) + ' times at time: ' + str(time) + '.'
    logging.info(msg)
    # make_response
    resp = make_response(msg)
    resp.set_cookie('visit-count', str(count), 'time', str(time))
    return resp

if __name__ == "__main__":
    app.run(debug=True)

# app = webapp2.WSGIApplication([('/', home)], debug=True)