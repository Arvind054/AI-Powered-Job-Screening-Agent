from sklearn.metrics.pairwise import cosine_similarity
def Calculate_Score(Job_Description_Vector, Current_Vector):
    similarity = cosine_similarity([Job_Description_Vector], [Current_Vector])
    similarity_score = similarity[0][0]*100
    return similarity_score