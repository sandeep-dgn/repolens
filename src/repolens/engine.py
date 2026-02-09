import os
from groq import Groq
from dotenv import load_dotenv
# Relative import: 'from .crawler' means 'look in the same folder'
from .crawler import scan_repository, get_code_context 

load_dotenv()

def analyze_repo():
    print("✅ Step 1: Engine loaded.")
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    files = scan_repository()
    print(f"✅ Step 2: Crawler found {len(files)} files.")
    
    context = get_code_context(files)
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a coding assistant."},
                {"role": "user", "content": f"Summarize this project structure:\n{context}"}
            ]
        )
        print("🚀 Step 3: AI Analysis Complete!")
        print(completion.choices[0].message.content)
    except Exception as e:
        print(f"❌ AI Error: {e}")