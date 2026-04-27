# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "blinker>=1.9.0",
#     "certifi>=2026.4.22",
#     "charset-normalizer>=3.4.7",
#     "click>=8.3.3",
#     "colorama>=0.4.6",
#     "flask>=2.3.3",
#     "flask-cors>=4.0.0",
#     "idna>=3.13",
#     "itsdangerous>=2.2.0",
#     "jinja2>=3.1.6",
#     "markupsafe>=3.0.3",
#     "requests>=2.31.0",
#     "werkzeug>=2.3.7",
# ]
# ///
from flask import *
import os, time

app = Flask(__name__)

@app.route('/')
def home():
        root = os.path.dirname(__file__)
        file_path = os.path.join(root, 'index.html')
        with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()

@app.route('/images/<filename>')
def image_fetch(filename):
        return send_from_directory('images', filename, as_attachment=True)

@app.route('/scan/')
def scan():
        os.system('python vision.py')
        root = os.path.dirname(__file__)
        file_path = os.path.join(root, 'index.html')
        with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        

@app.route('/scancustom/<wait>/<piccount>/')
def scanwithargs(wait, piccount):
        os.system(f'python vision.py -w {wait} -c {piccount}')
        root = os.path.dirname(__file__)
        file_path = os.path.join(root, 'index.html')
        with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()

@app.route('/stop/')
def stopplease():
        os.system('pkill -f vision.py')
        time.sleep(0.2)
        os.system('python stop.py')
        root = os.path.dirname(__file__)
        file_path = os.path.join(root, 'index.html')
        with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        
@app.route('/meta/')
def metadata():
        root = os.path.dirname(__file__)
        file_path = os.path.join(root, 'view.html')
        with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()      

@app.route('/<filename>')
def file_fetch(filename):
        return send_from_directory('', filename, as_attachment=True)

@app.route('/attachmetadata/<data>')
def attach_metadata(data):
        metadata[len(metadata)] = data
        return 'Metadata attached successfully'

@app.route('/resetmetadata/')
def reset_metadata():
        metadata.clear()
        return 'Metadata reset successfully'

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=1234, debug=True)
