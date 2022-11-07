import pickle
import streamlit as st
st.title("Heart Disease Prediction")
st.title("Author Nitish")
st_age 		= st.slider('Age',0,100,20)
st_sex 		= st.slider('Sex: Male=1, Female=0',0,1,1)
st_cp  		= st.slider("Chest pain:",0,3,1)
st_trestbps = st.slider("Resting Bp in mm Hg:",100,400,50)
st_chol		= st.slider("Cholesterol in mg/dl:",100,400,50)
st_fbs		= st.slider("Fasting blood sugar > 120 mg/dl: True=1,False=0",0,1,0)
st_restecg  = st.slider("Resting ECG results:",0,2,1)
st_thalach  = st.slider("Maximum heart rate:",60,200,30)
st_exang    = st.slider("Exercize induced angina Yes=1,No=0:",0,1,0)
st_old      = st.slider("Oldpeak,ST depression induced by exercise relative to rest:",0,10,5)
st_slope 	= st.slider("Slope of peak exercise ST segment, 1= unsloping 2= flat 3= downsloping:",1,3,2)
st_ca       = st.slider("No. of major vessels(0-3):",0,3,2)
st_thal     = st.slider("Thal normal=1,fixed defect=2,reversable defect=3",1,3,2)
st_target   = ['Less chance of heart attack','More chance of heart attack']

new = pickle.load(open('test','rb'))
y_pred = new.predict([[st_age,st_sex,st_cp,st_trestbps,st_chol,st_fbs,st_restecg,st_thalach,st_exang,st_old,st_slope,st_ca,st_thal]])
y_pred = st_target[y_pred[0]]
clicked = st.button("Test")
if(clicked):
	if(y_pred):
		st.success('Prediction Successful')
		y_pred
	else:
		st.error('Error running analysis')

#streamlit run app.py

