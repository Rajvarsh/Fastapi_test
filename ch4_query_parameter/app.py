from fastapi import FastAPI
from typing import Optional

app=FastAPI()

# # single query parameter
# @app.get("/product")
# async def product(category:str):
#     return {"status": "ok","category":category}

# # multiple query parameter
# @app.get("/product")
# async def product(category:str,limit:int):
#     return {"status": "ok","category":category,"limit":limit}


# # default query parameter
# @app.get("/product")
# async def product(category:str,limit:int=10):
#     return {"status": "ok","category":category,"limit":limit}

# optional query parameter
@app.get("/product")
async def product(
    limit: int = 10,
    category: str |None = None
):
    return {
        "status": "ok",
        "category": category,
        "limit": limit
    }