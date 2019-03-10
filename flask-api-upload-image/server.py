from flask import Flask, url_for, send_from_directory, request, render_template
import logging, os
from PIL import Image, ImageFilter
from werkzeug import secure_filename
import label_image as lb

app = Flask(__name__)
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


@app.route('/', methods = ['POST'])
def api_root():
    app.logger.info(PROJECT_HOME)
    if request.method == 'POST' and request.files['image']:
    	app.logger.info(app.config['UPLOAD_FOLDER'])
    	img = request.files['image']
    	img_name = secure_filename(img.filename)
    	create_new_folder(app.config['UPLOAD_FOLDER'])
    	saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
    	app.logger.info("saving {}".format(saved_path))
    	img.save(saved_path)
        im = Image.open(saved_path)
        print("do")
        n = lb.label(saved_path)
    	return render_template('safe.html', n=n)
    else:
    	return "Where is the image?"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
