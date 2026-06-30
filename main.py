from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag_pipeline import load_rag_chain

app = FastAPI()
qa = load_rag_chain() 


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    question = data.get("question", "")

    if not question:
        return {"error": "No question provided."}

    response = qa.invoke(question)
    return {"answer": response['result']}
