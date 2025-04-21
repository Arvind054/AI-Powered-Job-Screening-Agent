from pdfminer.high_level import extract_text
from components.GetResume_Details import AnalyseResume


def resume_processing(resume_files, JobDescriptiom):
    docs = []
    for file in resume_files:
        text = extract_text(file)
        result = AnalyseResume(text=text, JobDescription=JobDescriptiom)
        data = result.split(',')
        docs.append(data)
        return docs