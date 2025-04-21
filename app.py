import streamlit as st
from components.Process_Resume import resume_processing
st.title("AI Job Screening Agent🕵️")
Resume_Files = st.file_uploader(
    "Select Files only PDF",
    type=['pdf'],
    accept_multiple_files=True
)
Job_Description = st.text_input(
    "Enter Job Description"
)
if(st.button("Start")):
    if not Resume_Files or not Job_Description:
        st.write("Please Fill All the required Details")
    else:
        st.write("Process Started, Please Wait Until we Process")
        docs = resume_processing(resume_files=Resume_Files, JobDescriptiom=Job_Description)
        for doc in docs:
            st.write(doc[0], doc[1], doc[2], doc[3])
        st.write("Process Completed")
        