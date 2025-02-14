from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def redirect_to_scarletta():
    return RedirectResponse("https://giffy-lake-three.vercel.app/api/image.py")

