# persona_groq.py
import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def build_prompt(username, comments):
    joined = "\n\n".join(comments)
    return f"""
You are a personality analyst.

Based on the following Reddit comments made by user '{username}', generate a user persona in the format below.

---
**Name**: (Fictional, if unknown)  
**Age**:  
**Occupation**:  
**Status**:  
**Location**:  
**Tier**:  
**Archetype**:  

**Traits**: Practical / Adaptable / etc.  
**Motivations**:  
- Convenience
- Wellness
- Speed
- Comfort
- Dietary needs

**Personality**:
- Introvert/Extrovert
- Sensing/Intuition
- Feeling/Thinking
- Perceiving/Judging

**Behaviour & Habits**:
(List 3–5 bullet points)

**Frustrations**:
(List 3–5 bullet points)

**Goals & Needs**:
(List 3–5 bullet points)

Reddit Comments:
{joined}
---
"""

def call_groq(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",  
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(GROQ_API_URL, json=payload, headers=headers)

    if response.status_code != 200:
        print("❌ Groq API Error:", response.status_code)
        print(response.text)  
        return None

    return response.json().get("choices", [{}])[0].get("message", {}).get("content")

def clean_persona_output(raw):
    lines = raw.splitlines()
    if "based on" in lines[0].lower():
        lines = lines[1:]
    
    cleaned = [line.replace("**", "") for line in lines]
    return "\n".join(cleaned)


    response = requests.post(GROQ_API_URL, json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Groq API error: {response.text}")


    
    return response.json()["choices"][0]["message"]["content"]
