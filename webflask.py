#from crypt import methods
from flask import Flask, render_template, request, send_file
from sqlalchemy import true
import convertFile as c
from werkzeug.utils import secure_filename
import os

#UPLOAD_FOLDER = r"C:\Users\Rafid_S\Documents\EVASTORE\Input Folder"
UPLOAD_FOLDER = "/home/pi/EVASTORE/Input Folder"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/output',methods = ["POST","GET"])
def output():
    if request.method == "POST":
        f = request.files["name_f"]
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        
        c.convert(f.filename)
        p = c.outputpath
    
        return send_file(p,as_attachment=True)
        #return render_template("output.html", name = file_name)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = true)



'''
def output():
    output = request.form.to_dict()
    file_name = output["name_f"]
    c.convert(file_name)
    p = c.outputpath
'''