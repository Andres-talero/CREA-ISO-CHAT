"""OPENAI ROUTER"""

# FastAPI
from fastapi import APIRouter

# Controllers
from src.api.internal.openai import get_message, post_generate_vectors, post_create_vector, post_create_vector_text, post_get_response, post_get_vector

router = APIRouter()


@router.get("/")
def openai_route():
    return get_message()


@router.post("/generate-vectors")
def generate_vectors():
    return post_generate_vectors()


@router.post("/create-vector")
async def create_vector(url, company):
    return await post_create_vector(url, company)

@router.post("/create-vector-text")
async def create_vector_text(text, url, company):
    return await post_create_vector_text(text, url, company)

@router.post("/get-response")
async def get_response(request):
    return await post_get_response(request)


@router.post("/get-vector")
async def get_vector(request):
    return await post_get_vector(request)
