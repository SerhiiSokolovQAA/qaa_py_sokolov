
from flask import Flask, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'image_url': f'http://127.0.0.1:8080/uploads/{filename}'}), 201

@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    content_type = request.headers.get('Content-Type', '')
    if 'text' in content_type:
        return jsonify({'image_url': f'http://127.0.0.1:8080/uploads/{filename}'})
    else:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_image(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(path):
        os.remove(path)
        return jsonify({'image_url': f'http://127.0.0.1:8080/uploads/{filename}'})
    else:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(port=8080)
