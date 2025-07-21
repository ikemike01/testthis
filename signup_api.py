from fastapi import FastAPI, HTTPException, Form

app = FastAPI()

@app.post("/signup")
async def signup(username: str = Form(...), password: str = Form(...), email: str = Form(...)):
    # Simulate saving user data to a database
    if username == "" or password == "" or email == "":
        raise HTTPException(status_code=400, detail="All fields are required")

    # Simulate success response
    return {"message": "User signed up successfully", "username": username, "email": email}
