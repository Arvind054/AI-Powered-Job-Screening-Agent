from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
def GetEmbedding(text):
    Current_Vector = embedding_function.embed_query(text=text)
    return Current_Vector