from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def caesar_cipher(text, shift, mode='encode'):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isalpha():
            shift_char = 65 if char.isupper() else 97
            if mode == 'encode':
                result += chr((ord(char) - shift_char + shift) % 26 + shift_char)
            else:
                result += chr((ord(char) - shift_char - shift) % 26 + shift_char)
        else:
            result += char
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/caesar', methods=['POST'])
def caesar():
    data = request.get_json()
    text = data['text']
    shift = data['shift']
    mode = data['mode']
    result = caesar_cipher(text, shift, mode)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
