# Import Flask framework.
from flask import Flask
app = Flask(__name__)

# Import custom TCP Server framework.
import tcp_server


@app.route('/')
def hello_world():
    return 'Hello World!'

# Run the arduino communciation server.
if __name__ == '__main__':
  app.run(debug = True)