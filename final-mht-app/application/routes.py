from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy as np
import pandas as pd
import pickle
model = pickle.load(open('model.pkl','rb'))
#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/disorderPredict", methods=['GET', 'POST'])
def disorderPredict():

    #extract form inputs
    tech_comp_flag = request.form.get("tech_comp_flag")
    mh_coverage_flag= request.form.get("mh_coverage_flag")
    mh_resources_provided = request.form.get("mh_resources_provided")
    mh_medical_leave = request.form.get("mh_medical_leave")
    sex = request.form.get("sex")
    tech_flag = request.form.get("tech_flag")
    mh_disorder_past = request.form.get("mh_disorder_past")
    mh_sought_proffes_treatm = request.form.get("mh_sought_proffes_treatm")
    mh_eff_treat_impact_on_work = request.form.get("mh_eff_treat_impact_on_work")


    array1 = np.array([tech_comp_flag,mh_coverage_flag,mh_resources_provided,mh_medical_leave,sex,tech_flag,mh_disorder_past,mh_sought_proffes_treatm,mh_eff_treat_impact_on_work])
    #extract data from json
    pred = model.predict([array1])

    if(pred ==0):
        result = "Yes"
    elif(pred==1):
        result = "No"
    elif(pred==2):
        result = "May be"
        

    # output = {
    #     "tech_comp_flag": tech_comp_flag, 
    #     "mh_coverage_flag": mh_coverage_flag, 
    #     "mh_resources_provided": mh_resources_provided, 
    #     "mh_medical_leave": mh_medical_leave, 
    #     "sex": sex, 
    #     "tech_flag": tech_flag, 
    #     "mh_disorder_past": mh_disorder_past, 
    #     "mh_sought_proffes_treatm": mh_sought_proffes_treatm, 
    #     "mh_eff_treat_impact_on_work": mh_eff_treat_impact_on_work,
    #     "data":pred[0]
    # }
    #url for car classification api
    #url = "http://localhost:5000/api"
    #url = "https://dsm-car-model.herokuapp.com/api"

 
    #post data to url
    #results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    return render_template("index.html", tech_comp_flag = tech_comp_flag, mh_coverage_flag = mh_coverage_flag, mh_resources_provided = mh_resources_provided, mh_medical_leave = mh_medical_leave, sex = sex,tech_flag = tech_flag,  mh_disorder_past = mh_disorder_past,mh_sought_proffes_treatm = mh_sought_proffes_treatm, mh_eff_treat_impact_on_work = mh_eff_treat_impact_on_work ,data = result)
    #return render_template("index.html", data = output)
