
from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class LicenseRequest(BaseModel):
    asset_type: str
    intended_use: str
    legal_preferences: str

@app.post("/generate-license")
def generate_license(req: LicenseRequest):
    prompt = f"""
    Create a licensing agreement based on:
    - Asset: {req.asset_type}
    - Use: {req.intended_use}
    - Preferences: {req.legal_preferences}
    
    Include relevant clauses and a pricing tier recommendation.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a legal expert helping creators write smart license agreements."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"license_template": response['choices'][0]['message']['content']}
