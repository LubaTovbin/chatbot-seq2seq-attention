from flask import Flask, render_template, request
from flask import jsonify
from MyTest.execute import Test

app = Flask(__name__,static_url_path="/static")
test = Test()
#############
# Routing
#
@app.route('/message', methods=['POST'])
def reply():
    return jsonify({'text': test.decode_line(request.form['msg'])})

@app.route("/")
def index():
    return render_template("index.html")
#############
'''
Init seq2seq model
    1. Call main from execute.py
    2. Create decode_line function that takes message as input
'''
#_________________________________________________________________
import sys
import os.path

print(os.getcwd())
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#_________________________________________________________________

# start app
if (__name__ == "__main__"):
    app.run(port = 5000)
