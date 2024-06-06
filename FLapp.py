from flask import Flask, render_template, request, url_for, flash, redirect
from .team import team
from .organization import organization
from dotenv import load_dotenv
import os



app = Flask(__name__)

load_dotenv()
secret_key = os.getenv('API_SECRET')

app.config['SECRET_KEY'] = secret_key

org1 = organization()

messages = [{"employee": "Gather",
             "employeeID": "0003",
             "organization": org1.getOrganizationName()},
             {"employee":"Sally",
              "employeeID": "0022",
              "organization":org1.getOrganizationName()},
              {"employee": "Roberto",
               "employeeID": "0027",
             "organization": org1.getOrganizationName()},
             {"employee":"Kelsey",
              "employeeID": "0041",
              "organization":org1.getOrganizationName()},
              {"employee": "Shep",
               "employeeID": "0165",
             "organization": org1.getOrganizationName()},
             {"employee":"Cal",
              "employeeID": "0133",
              "organization":org1.getOrganizationName()}
             ]

@app.route("/")
def index():
    global org1    
    return render_template('index.html', messages=messages, orgMaster=org1.getOrganizationName())

@app.route('/create/', methods=('GET', 'POST'))
def create():
    global org1
    if request.method == 'POST':
        employee = request.form['employee']
        organization = org1.getOrganizationName()
        employeeID = request.form['employeeID']

        if not employee:
            flash('Employee name is required!')
        elif not employeeID:
            flash('Employee ID is required!')
        else:
            messages.append({'employee': employee, 'employeeID': employeeID, 'organization': org1.getOrganizationName()})
            return redirect(url_for('index'))
        
    return render_template('create.html')

@app.route('/setup/', methods=('GET', 'POST'))
def setup():
    global org1
    if request.method == 'POST':
        hold = request.form['organizationName']

        org1.setOrganizationName(hold)

        print(org1.getOrganizationName())

        if not org1.getOrganizationName():
            flash('organization name is required!')
        else:
            return redirect(url_for('index'))
    return render_template('setup.html')