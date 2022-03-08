from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import pickle
from datetime import datetime
import ipdb


app = Flask(__name__)
model = pickle.load(open("C:\\Users\\Ram Sudheer\\Prob_of_default\\pred_default_xgb.pkl", "rb"))



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["POST"])

def predict():
      
       income = int(request.form["income"])
       if income <= 500000:
           Income_0_5L = 1
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 500000 and income <= 1000000:
           Income_0_5L = 0
           Income_5_5L = 1
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 1000000 and income <= 1500000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 1
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 1500000 and income <= 2000000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 1
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 2000000 and income <= 2500000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 1
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
           
       elif income > 2500000 and income <= 3000000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 1
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 3000000 and income <= 3500000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 1
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 3500000 and income <= 4000000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 1
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 4000000 and income <= 4500000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 1
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 4500000 and income <= 5000000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 1
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 5000000 and income <= 5500000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 1
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 5500000 and income <= 6000000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 1
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 6000000 and income <= 6500000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 1
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 6500000 and income <= 7000000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 1
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 7000000 and income <= 7500000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 1
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 7500000 and income <= 8000000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 1
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 8000000 and income <= 8500000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 1
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 8500000 and income <= 9000000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 1
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 9000000 and income <= 9500000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 1
           Income_95_100L = 0
           Income_100_200L = 0
       elif income > 9500000 and income <= 10000000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 1
           Income_100_200L = 0
       elif income > 10000000:
           Income_0_5L = 0
           Income_5_5L = 0
           Income_10_15L = 0
           Income_15_20L = 0
           Income_20_25L = 0
           Income_25_30L = 0
           Income_30_35L = 0
           Income_35_40L = 0
           Income_40_45L = 0
           Income_45_50L = 0
           Income_50_55L = 0
           Income_55_60L = 0
           Income_60_65L = 0
           Income_65_70L = 0
           Income_70_75L = 0
           Income_75_80L = 0
           Income_80_85L = 0
           Income_85_90L = 0
           Income_90_95L = 0
           Income_95_100L = 0
           Income_100_200L = 1
           
       age = int(request.form["age"])
       if age<=30:
           Age_20_30 = 1
           Age_30_40 = 0
           Age_40_50 = 0
           Age_50_60 = 0
           Age_60_70 = 0
           Age_70_80 = 0
           Age_80_90 = 0
       elif age > 30 and age  <=40:
           Age_20_30 = 0
           Age_30_40 = 1
           Age_40_50 = 0
           Age_50_60 = 0
           Age_60_70 = 0
           Age_70_80 = 0
           Age_80_90 = 0
       elif age > 40 and age  <=50:
           Age_20_30 = 0
           Age_30_40 = 0
           Age_40_50 = 1
           Age_50_60 = 0
           Age_60_70 = 0
           Age_70_80 = 0
           Age_80_90 = 0
       elif age > 50 and age  <=60:
           Age_20_30 = 0
           Age_30_40 = 0
           Age_40_50 = 0
           Age_50_60 = 1
           Age_60_70 = 0
           Age_70_80 = 0
           Age_80_90 = 0
       elif age > 60 and age  <=70:
           Age_20_30 = 0
           Age_30_40 = 0
           Age_40_50 = 0
           Age_50_60 = 0
           Age_60_70 = 1
           Age_70_80 = 0
           Age_80_90 = 0
       elif age > 70 and age  <=80:
           Age_20_30 = 0
           Age_30_40 = 0
           Age_40_50 = 0
           Age_50_60 = 0
           Age_60_70 = 0
           Age_70_80 = 1
           Age_80_90 = 0
       elif age > 80:
           Age_20_30 = 0
           Age_30_40 = 0
           Age_40_50 = 0
           Age_50_60 = 0
           Age_60_70 = 0
           Age_70_80 = 0
           Age_80_90 = 1
           
       experience = int(request.form["experience"])
       if experience<=5:
           Experience_0_5 = 1
           Experience_6_10 = 0
           Experience_11_15 = 0
           Experience_16_20 = 0
       elif experience>5 and experience<=10:
           Experience_0_5 = 0
           Experience_6_10 = 1
           Experience_11_15 = 0
           Experience_16_20 = 0
           
       elif experience>10 and experience<=15:
           Experience_0_5 = 0
           Experience_6_10 = 0
           Experience_11_15 = 1
           Experience_16_20 = 0
       elif experience>15:
           Experience_0_5 = 0
           Experience_6_10 = 0
           Experience_11_15 = 0
           Experience_16_20 = 1
       marital_status = request.form["marital_status"]
       if(marital_status == "single"):
           single = 1
           married =0
       else:
           single =0
           married =1
       house_ownership = request.form["house_ownership"]
       if house_ownership == "Own":
           House_Ownership_owned = 1
           House_Ownership_rented = 0
       else:
           House_Ownership_owned =1
           House_Ownership_rented =0
           
       car_ownership = request.form["car_ownership"]
       if(car_ownership == "Yes"):
           Car_Ownership_no = 0
           Car_Ownership_yes = 1
       else:
           Car_Ownership_no = 1
           Car_Ownership_yes = 0
       prof = request.form["profession"]
       if prof == "ENGINEER":
               PROFESSION_TYPE_ARTS = 0
               PROFESSION_TYPE_ENGINEER = 1
               PROFESSION_TYPE_FINANCE = 0
               PROFESSION_TYPE_GOVT = 0
               PROFESSION_TYPE_MEDICAL = 0
               PROFESSION_TYPE_OTHER = 0
       elif prof == "FINANCE":
               PROFESSION_TYPE_ARTS = 0
               PROFESSION_TYPE_ENGINEER = 0
               PROFESSION_TYPE_FINANCE = 1
               PROFESSION_TYPE_GOVT = 0
               PROFESSION_TYPE_MEDICAL = 0
               PROFESSION_TYPE_OTHER = 0
       elif prof == "ARTS":
               PROFESSION_TYPE_ARTS = 1
               PROFESSION_TYPE_ENGINEER = 0
               PROFESSION_TYPE_FINANCE = 0
               PROFESSION_TYPE_GOVT = 0
               PROFESSION_TYPE_MEDICAL = 0
               PROFESSION_TYPE_OTHER = 0
       elif prof == "GOVT":
               PROFESSION_TYPE_ARTS = 0
               PROFESSION_TYPE_ENGINEER = 0
               PROFESSION_TYPE_FINANCE = 0
               PROFESSION_TYPE_GOVT = 1
               PROFESSION_TYPE_MEDICAL = 0
               PROFESSION_TYPE_OTHER = 0
       elif prof == "MEDICAL":
               PROFESSION_TYPE_ARTS = 0
               PROFESSION_TYPE_ENGINEER = 0
               PROFESSION_TYPE_FINANCE = 0
               PROFESSION_TYPE_GOVT = 0
               PROFESSION_TYPE_MEDICAL = 1
               PROFESSION_TYPE_OTHER = 0
       else:
               PROFESSION_TYPE_ARTS = 0
               PROFESSION_TYPE_ENGINEER = 0
               PROFESSION_TYPE_FINANCE = 0
               PROFESSION_TYPE_GOVT = 0
               PROFESSION_TYPE_MEDICAL = 0
               PROFESSION_TYPE_OTHER = 1
          
       state = request.form["state"]       
       if (state == "Manipur" or state == "Mizoram" or state == "Tripura" or state == "Sikkim" or state == "Assam" or state == "West_Bengal" or state == "Odisha" or state == "Bihar" or state == "Jharkhand"):
                STATE_TYPE_EAST = 1
                STATE_TYPE_NORTH = 0
                STATE_TYPE_SOUTH = 0
                STATE_TYPE_WEST = 0
       if state == "Maharashtra" or state == "Gujarat" or state == "Chhattisgarh" or state == "Madhya_Pradesh": 
                STATE_TYPE_EAST = 0
                STATE_TYPE_NORTH = 0
                STATE_TYPE_SOUTH = 0
                STATE_TYPE_WEST = 1
       if state == "Chandigarh" or state == "Uttar_Pradesh" or state == "Jammu_and_Kashmir" or state == "Delhi" or state == "Punjab" or state == "Haryana" or state == "Himachal_Pradesh" or state == "Rajasthan" or state == "Uttarakhand":
                STATE_TYPE_EAST = 0
                STATE_TYPE_NORTH = 1
                STATE_TYPE_SOUTH = 0
                STATE_TYPE_WEST = 0
       if state == "Andhra_Pradesh" or state == "Tamil_Nadu" or state == "Telangana" or state == "Karnataka" or state == "Kerala" or state == "Puducherry":
                STATE_TYPE_EAST = 1
                STATE_TYPE_NORTH = 0
                STATE_TYPE_SOUTH = 0
                STATE_TYPE_WEST = 0
                      
       house_ownership_norent_noown = 0
       current_job_years = int(request.form["current_job_years"])
       if current_job_years <=5:
          current_job_yrs_0_5 = 1
          current_job_yrs_5_10 = 0
          current_job_yrs_10_15 = 0
       elif current_job_years >5 and current_job_years <=10:
           current_job_yrs_0_5 = 0
           current_job_yrs_5_10 = 1
           current_job_yrs_10_15 = 0
       elif current_job_years >10:
           current_job_yrs_0_5 = 0
           current_job_yrs_5_10 = 0
           current_job_yrs_10_15 = 1
          
       current_house_years = int(request.form["current_house_years"])
       lst = [[current_house_years,
                Age_20_30,
                Age_30_40,
                Age_40_50,
                Age_50_60,
                Age_60_70,
                Age_70_80,
                Age_80_90,
                Experience_0_5,
                Experience_6_10,
                Experience_11_15,
                Experience_16_20,
                Income_0_5L,
                Income_5_5L,
                Income_10_15L,
                Income_15_20L,
                Income_20_25L,
                Income_25_30L,
                Income_30_35L,
                Income_35_40L,
                Income_40_45L,
                Income_45_50L,
                Income_50_55L,
                Income_55_60L,
                Income_60_65L,
                Income_65_70L,
                Income_70_75L,
                Income_75_80L,
                Income_80_85L,
                Income_85_90L,
                Income_90_95L,
                Income_95_100L,
                Income_100_200L,
                current_job_yrs_0_5,
                current_job_yrs_5_10,
                current_job_yrs_10_15,
                married,
                single,
                house_ownership_norent_noown,
                House_Ownership_owned,
                House_Ownership_rented,
                Car_Ownership_no,
                Car_Ownership_yes,
                STATE_TYPE_EAST,
                STATE_TYPE_NORTH,
                STATE_TYPE_SOUTH,
                STATE_TYPE_WEST,
                PROFESSION_TYPE_ARTS,
                PROFESSION_TYPE_ENGINEER,
                PROFESSION_TYPE_FINANCE,
                PROFESSION_TYPE_GOVT,
                PROFESSION_TYPE_MEDICAL,
                PROFESSION_TYPE_OTHER]]
       df=pd.DataFrame(lst,columns=
                       ['CURRENT_HOUSE_YRS','Age:20-30','Age:30-40','Age:40-50','Age:50-60','Age:60-70','Age:70-80','Age:80-90','Experience:0-5','Experience:6-10','Experience:11-15','Experience:16-20','Income:0-5L','Income:5-5L','Income:10-15L','Income:15-20L','Income:20-25L','Income:25-30L','Income:30-35L','Income:35-40L','Income:40-45L','Income:45-50L','Income:50-55L','Income:55-60L','Income:60-65L','Income:65-70L','Income:70-75L','Income:75-80L','Income:80-85L','Income:85-90L','Income:90-95L','Income:95-100L','Income:100-200','CURRENT_JOB_YRS:0-5','CURRENT_JOB_YRS:5-10','CURRENT_JOB_YRS:10-15','Married/Single_married','Married/Single_single','House_Ownership_norent_noown','House_Ownership_owned','House_Ownership_rented','Car_Ownership_no','Car_Ownership_yes','STATE_TYPE_EAST','STATE_TYPE_NORTH','STATE_TYPE_SOUTH','STATE_TYPE_WEST','PROFESSION_TYPE_ARTS','PROFESSION_TYPE_ENGINEER','PROFESSION_TYPE_FINANCE','PROFESSION_TYPE_GOVT','PROFESSION_TYPE_MEDICAL','PROFESSION_TYPE_OTHER'])
       prediction=model.predict(df)
      
       default ="Default"
       ndefault = "Non-Default"
       #print(prediction)
       if prediction == 1:
            return render_template('home.html',prediction_text="Default prediction of the customer  is {}".format(default))
       else:
            return render_template('home.html',prediction_text="Default prediction of the customer  is {}".format(ndefault))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    app.run(debug=True)
