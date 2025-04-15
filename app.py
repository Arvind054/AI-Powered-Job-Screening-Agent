import streamlit as st
from pdfminer.high_level import extract_text
from components.Resume_Processing import Extract_Email
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
        for file in Resume_Files:
            text = extract_text(file)
            email = Extract_Email(text)
            st.write("Email Sent To: ", email)
        st.write("Process Completed")
