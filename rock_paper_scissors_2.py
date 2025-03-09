from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/button_click', methods = ['POST'])
def button_click():
    print("Button pressed on server")
    return jsonify ({"message": "Button click received"})

if __name__ == '__main__':
    app.run(debug=True)