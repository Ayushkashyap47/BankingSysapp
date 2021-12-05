import streamlit as st
from PIL import Image
import joblib
import sklearn


model1 = joblib.load("model")
def Prediction(age, ed, employ, debtinc, creddebt,othdebt):
    pred = model1.predict_proba([[age, ed, employ, debtinc, creddebt,othdebt]])
    pred_default=pred[0][1]
    return(pred_default)

def start1():
    img1 = Image.open('bans.jpg')
    img1 = img1.resize((500, 300))
    st.image(img1, use_column_width=False)
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Bank Loan Prediction ML App </h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.number_input("Age")
    ed = st.number_input(" Years of education")
    employ = st.number_input("Employed for how many years")
    debtinc = st.number_input("Debt to income ratio")
    creddebt = st.number_input("Credit debt")
    othdebt = st.number_input("Other debt")
    if st.button("Predict"):
        result=Prediction(age, ed, employ, debtinc, creddebt,othdebt)
        if result> 0.2476080913770519:
            st.success("The person will Default its our recommendation not to give this person loan")
        else:
            st.success("The person will not Default its our recommendation to give this person loan")
start1()
