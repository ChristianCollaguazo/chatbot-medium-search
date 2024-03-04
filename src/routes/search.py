from fastapi import APIRouter, Body
from src.utils.load_data import LoadData
router = APIRouter()


@router.post('/similarity-search', tags=['search'])
def similarity_search(query: str = Body()):
    search = LoadData()
    return search.similarity_search(query)