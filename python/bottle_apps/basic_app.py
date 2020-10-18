from bottle import Bottle, route, run, template

app = Bottle()

@app.route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>', name=name)

run(app, host='localhost', port=8000)