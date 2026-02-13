from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "KrishiSahay Backend is Running"}

@app.post("/ask")
def ask_question(data: dict):
    question = data.get("question")

    if not question:
        return {"response": "Please ask a valid farming question."}

    # Simple demo logic
    if "rice" in question.lower():
        answer = "For rice crops, maintain proper irrigation and use nitrogen-rich fertilizers."
    elif "wheat" in question.lower():
        answer = "Wheat requires well-drained soil and moderate irrigation."
    elif "pest" in question.lower():
        answer = "For pest control, use recommended organic pesticides and monitor crop health regularly."
    else:
        answer = "Our AI system will analyze your farming query soon."

    return {"response": answer}