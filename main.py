from fastapi import FastAPI



<<<<<<< HEAD
app = FastAPI()



@app.get("/health")

def health():
=======
app = FastAPI



@.get("/health")

 health()
>>>>>>> faccc26 (chore: autonomous devops scaffold)

    data = {"status": "ok"}

    return data



@app.get("/")

<<<<<<< HEAD
def root():
=======
 root()
>>>>>>> faccc26 (chore: autonomous devops scaffold)

    return {"message": "Hello"}



if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
