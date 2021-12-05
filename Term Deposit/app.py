import streamlit as st
from PIL import Image
import sklearn
import joblib
model=joblib.load("model1")
def Predict(age,contact,duration,education,pdays,poutcome,previous):
#Labels for Education
    if education == "illiterate" or education == "basic.4y" or education == "basic.6y" or education == "basic.9y":
        x = 0
    elif education == "high.school" or education == "unknown":
        x = 1
    elif education == "professional.course":
        x = 2
    else:
        x = 3
    # Labels for contacts
    if contact == "cellular":
        x1 = 0
    else:
        x1 = 1
    # Labels for poutcome
    if poutcome=="nonexistent":
        x2 = 0
    elif poutcome == "failure":
        x2 = 1
    else:
        x2 = 2
    pred = model.predict([[age,x1,duration,x,pdays,x2,previous]])
    return(pred[0])
def start1():
    img1 = Image.open("term.jpg")
    img1 = img1.resize((500, 300))
    st.image(img1, use_column_width=False)
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Term Deposit Prediction ML App </h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.number_input("Age")
    contact= st.radio("contact",("cellular","telephone"))
    duration = st.number_input("Enter call durations in seconds")
    education = st.radio("Select education ",('basic.9y', 'university.degree', 'basic.4y', 'high.school',
    'professional.course', 'unknown', 'basic.6y', 'illiterate'))
    pdays = st.number_input("number of days that passed by after the client was last contacted from a previous campaign")
    poutcome=st.radio("outcome of the previous marketing campaign",('failure','nonexistent','success'))
    previous=st.number_input("number of contacts performed before this campaign and for this client")
    if st.button("Predict"):
        result = Predict(age,contact,duration,education,pdays,poutcome,previous)
        if result == 1:
            st.success("Their is a high possibility that a person will go for term deposit")
        else:
            st.success("Their is a high possibility that a person will not go for term deposit")
start1()
