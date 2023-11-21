from fastapi import HTTPException
from src.utils.loadBlobVectors import load_data_into_vectorstore
from src.utils.chainData_ import get_response
from src.utils.vectorSearch import search
from src.utils.documentLayoutOcr import document_to_ocr
from src.utils.saveVector import save_vector
from src.utils.formatDoc import order_doc


def get_message():
    return {"Hello": "World"}


def get_specific_message():
    return {"Specific": "Message"}


def post_generate_vectors():
    load_data_into_vectorstore()
    return {"Generate": "Vectors"}


async def post_create_vector(url, company):
    if url:
        ocr = document_to_ocr(url)
        doc = order_doc(ocr)
        response = save_vector(doc, url, company)
        return response
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    

async def post_create_vector_text(text, url, company):
    if text:
        response = save_vector(text, url, company)
        return response
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    

async def post_get_response(request):
    if request:
        response = get_response(request)
        return response
    else:
        raise HTTPException(status_code=404, detail="Item not found")


async def post_get_vector(request):
    if request:
        response = search(request)
        return response
    else:
        raise HTTPException(status_code=404, detail="Item not found")
