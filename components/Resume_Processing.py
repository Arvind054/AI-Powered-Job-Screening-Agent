import re
from pdfminer.high_level import extract_text
import streamlit as st
from components.Generate_Embedding import GetEmbedding
from components.Calculate_Resume_Score import Calculate_Score
def Extract_Email(text):
    Email_Regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(Email_Regex, text)
    if match.group(0):
        return match.group(0)
    return "Not Found"

def Process_Resume(Job_Description,Matching_Percentage,Resume_Files):
    Job_Description_vector = GetEmbedding(text=Job_Description)
    for file in Resume_Files:
        text = extract_text(file)
        Current_Vector_Embedding = GetEmbedding(text=text)
        score = Calculate_Score(Job_Description_Vector= Job_Description_vector, Current_Vector=Current_Vector_Embedding)
        email = Extract_Email(text)
        st.write(email, "-->", score)
        if int(score) >= int(Matching_Percentage):
            st.write("Email Sent To: ", email)

     