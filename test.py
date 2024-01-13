from flask import Flask, send_file

app = Flask(__name__)

@app.route('/json')
def get_json():
    return send_file('first-names.json', mimetype='application/json')

if __name__ == '__main__':
    app.run()