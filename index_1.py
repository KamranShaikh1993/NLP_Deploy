import streamlit as st


import pickle
file1 = open("model.pkl",'rb') 
file2 = open("CountVector.pkl",'rb')
model = pickle.load(file1)  
cv = pickle.load(file2)  

msg = 'It was amazing. I liked it a lot'

def predict_review(msg):   
    msg_cv = cv.transform([msg])
    result = model.predict(msg_cv)[0]
    return result



st.write("# Sentiment Analysis ")
message = st.text_area("Message (eg:- Food was good/ Restaurent was Great)")

if st.button("Predict"):
    result = predict_review(message)
    st.write(result)
