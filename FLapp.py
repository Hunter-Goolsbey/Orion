from flask import Flask, render_template, request, url_for, flash, redirect
from .team import team
from .organization import organization
from dotenv import load_dotenv
import os
import json



app = Flask(__name__)

load_dotenv()
secret_key = os.getenv('API_SECRET')

app.config['SECRET_KEY'] = secret_key

org1 = organization()
rsalesFile = open("salesEE.txt")
rsalesFile1= rsalesFile.readlines()

if len(rsalesFile1) > 0:
    #messages = []
    for i in rsalesFile1:
        i = i.replace("\'", "\"")
        #print(i)
        messages = json.loads(i)
        #print(messages)

else:
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
    file = open("DB.txt")
    file1= file.readlines()
    developer_id=""

    for lines in file1:                                                                                      
        developer_id = lines.split(":")[-1].strip()
    file.close()                                                                     

    if  len(file1) > 0:
        return render_template('index.html', messages=messages, orgMaster=org1.getOrganizationName())
    else:
        return redirect(url_for('setup'))

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
            with open("salesEE.txt", "w") as wsalesFile:
                wsalesFile.write(str(messages))
            return redirect(url_for('index'))
        
    return render_template('create.html')

@app.route('/setup/', methods=('GET', 'POST'))
def setup():
    global org1
    file = open("DB.txt", "w")
    
    if request.method == 'POST':
        hold = request.form['organizationName']

        org1.setOrganizationName(hold)

        print(org1.getOrganizationName())

        if not org1.getOrganizationName():
            flash('organization name is required!')
        else:
            file.write("1")
            file.close()
            return redirect(url_for('index'))
    file.write("1")
    file.close()
    return render_template('setup.html')