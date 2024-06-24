from flask import Flask, render_template, request, url_for, redirect, make_response
import os
import base64
import regression_calculator

app = Flask(__name__)

#TODO is this line needed? Could also 
#app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs("uploads/", exist_ok=True)

dependent_var = None
independent_vars = None

@app.route("/")
def home():
    return render_template("upload.html")

#also want the upload to be deleted when the app stops running.
@app.route('/upload', methods=['POST'], endpoint='upload_file')
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request'
    file = request.files['file']
    dependent_var = request.form['dependent-variable']
    dvfile = open('static/dependentvar.txt','w')
    dvfile.write(dependent_var)
    dvfile.close()

    #indepenent_vars = request.form["independent-vars"].split(',')
    independent_vars = request.form["independent-variables"]
    ivfile = open('static/independentvars.txt','w')
    ivfile.write(independent_vars)
    ivfile.close()


    if file:
        filename = file.filename
        file.save(os.path.join("uploads", filename))

        #also write file path to a file in static for ref when performing regression calculation
        csvname = open('static/csvname.txt','w')
        csvname.write(filename)
        csvname.close()

        return render_template('interactive.html', dv=dependent_var, iv=independent_vars)

@app.route('/interactive', methods=['POST', 'GET'], endpoint = 'select_variables')
def select_variables():
    ivs_in_use = [key for key, value in request.form.items() if value == 'on']
    print(ivs_in_use)
    dvfile = open('static/dependentvar.txt','r')
    dependent_var = dvfile.read()
    ivfile = open('static/independentvars.txt','r')
    independent_vars = ivfile.read()
    csvname_file = open('static/csvname.txt','r')
    csvname = csvname_file.read()

    img_base64 = None

    #in the event that no independent variables are selected, display no image instead of crashing
    try:
        buf = regression_calculator.calculate_regression("uploads/" + csvname, dependent_var, ivs_in_use, "linear", True) #TODO - filename instead of dummy.csv
        img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    except: 
        pass

    return render_template('interactive.html', dv=dependent_var, iv=independent_vars, img_data=img_base64, vars = str(ivs_in_use))

#@app.route('/plot.png')
#def plot_png():
#    buf = regression_calculator.calculate_regression("uploads/dummy.csv", dependent_var, ivs_in_use, "linear", True) #TODO - filename instead of dummy.csv
#    return make_response(buf.read(), 200, {'Content-Type': 'image/png'})
    
    
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
