from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'ля красиво'

@app.route('/records')
def records():
  return 'Our records'

if __name__ == '__main__':
  app.run(debug=True)
  