import re

def Extract_Email(text):
    Email_Regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(Email_Regex, text)
    if match.group(0):
        return match.group(0)
    return "Not Found"



     