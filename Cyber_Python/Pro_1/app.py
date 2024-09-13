from flask import Flask, request, jsonify, render_template
from caesar import caesar_encrypt, caesar_decrypt
from vigenere import vigenere_encrypt, vigenere_decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/caesar', methods=['POST'])
def caesar_cipher():
    data = request.get_json()
    text = data['text']
    shift = data['shift']
    mode = data['mode']
    
    if mode == 'encode':
        result, steps = caesar_encrypt(text, shift)
    else:
        result, steps = caesar_decrypt(text, shift)
    
    return jsonify({'result': result, 'steps': steps})

@app.route('/vigenere_encrypt', methods=['POST'])
def vigenere_cipher_encrypt():
    data = request.get_json()
    text = data['text']
    key = data['key']
    
    result, steps = vigenere_encrypt(text, key)
    
    return jsonify({'result': result, 'steps': steps})

@app.route('/vigenere_decrypt', methods=['POST'])
def vigenere_cipher_decrypt():
    data = request.get_json()
    text = data['text']
    key = data['key']
    
    result, steps = vigenere_decrypt(text, key)
    
    return jsonify({'result': result, 'steps': steps})

if __name__ == '__main__':
    app.run(debug=True)
