from flask import Flask, render_template
import label_image as lb
app = Flask(__name__)

n = lb.label(saved_path)
@app.route("/")
def template_test():
    return render_template('safe.html', lb(saved_path))


if __name__ == '__main__':
    app.run(debug=True)
