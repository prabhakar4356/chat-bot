import google.generativeai as genai
api_key = "AIzaSyA2X6PgXZsYnJV4czh-bQQ5QCDDPHYZMWg"
genai.configure(api_key=api_key)
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
