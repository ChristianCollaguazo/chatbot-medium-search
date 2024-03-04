from fastapi import APIRouter, Body
from src.utils.load_data import LoadData

router = APIRouter()

vector_db = LoadData()


@router.post("/similarity-search", tags=["search"])
def similarity_search(query: str = Body()):
    return vector_db.similarity_search(query)
