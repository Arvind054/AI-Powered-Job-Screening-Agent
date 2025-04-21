from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(
    model='gemini-1.5-pro')

def AnalyseResume(text, JobDescription):
    prompt = f"""
    This is the parsed text of the resume:
    {text}

    Based on the following Job Description:
    {JobDescription}

    Provide a score out of 100 for how well the resume matches the job.
    Output the result as a string with each item seaprated by ',' only value format including: name, email, phone number, and score.
    If any field is not available, leave it empty.
    """

    result = model.invoke(prompt)
    data = result.content
    return data
