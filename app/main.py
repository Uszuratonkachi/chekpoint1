from fastapi import FastAPI


app = FastAPI()


@app.get("/hotels")
def get_hotels():
    return "Hotel Bridge Resort 5 stars"