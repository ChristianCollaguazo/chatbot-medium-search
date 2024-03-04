from fastapi import FastAPI
from src.routes.search import router as search_router
from src.utils.load_data import LoadData

print(LoadData().similarity_search('machine learning'))



app = FastAPI()

app.title = "Chat Bot Template"
app.version = "1.0.0"

app.include_router(search_router)


@app.get("/", tags=["greeting"])
def home():
    return "Hola mundo"
