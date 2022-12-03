from flask import Flask

app=Flask(__name__, template_folder='./views/templates/')

@app.route('/home')
def home():
    return "Hello rijenth"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)