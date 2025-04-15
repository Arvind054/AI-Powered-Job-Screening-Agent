import streamlit as st
from components.Resume_Processing import Extract_Email
from components.Resume_Processing import Process_Resume

st.title("AI Job Screening Agent")
Resume_Files = st.file_uploader(
    "Select Files only PDF",
    type=['pdf'],
    accept_multiple_files=True
)
Job_Description = st.text_input(
    "Enter Job Description"
)
Matching_Percentage = st.number_input("Enter Threshold matching Percentage")

if(st.button("Start")):
    if not Resume_Files or not Job_Description or not Matching_Percentage:
        st.write("Please Fill All the required Details")
    else:
        st.write("Process Started, Please Wait Until we Process")
        Process_Resume(Job_Description=Job_Description,Matching_Percentage = Matching_Percentage, Resume_Files=Resume_Files)
        st.write("Process Completed")
        