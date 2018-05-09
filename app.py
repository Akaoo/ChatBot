from flask import Flask
import Test
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hi"


if __name__ == '__main__':
    app.run()
