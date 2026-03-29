from fastapi import FastAPI
import uvicorn

# Create FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is running!"}

def main():
    """
    Entry point for the server.
    Runs FastAPI using uvicorn.
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Ensure main() is callable when run directly
if __name__ == "__main__":
    main()
