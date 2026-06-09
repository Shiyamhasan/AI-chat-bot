import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyBBH2n2pe3dxJQ3B5j-rqP10Bz7bY9OOsw")
model=genai.GenerativeModel("gemini-2.5-flash")
qns=st.text_input("Enter the code:")
res=model.generate_content(qns+"you have to give me the corrected answer of gk question")
st.write(res.text)