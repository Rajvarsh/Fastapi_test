from fastapi import FastAPI,Query,Path
from typing import Annotated
from pydantic import AfterValidator

app=FastAPI()

# PRODUCTS=[
#     {
#      "Id":1,
#      "title":"ravan facepack",
#      "price":109,
#      "description":"perfect for everyday use and forest walks."
#      },
#     {
#      "Id":2,
#      "title":"bindu biscuit",
#      "price":200,
#      "description":"perfect for everyday use ."
#      },
#     {
#      "Id":2,
#      "title":"riti chai",
#      "price":109,
#      "description":"perfect for everyday tea use picnic."
#      }
# ]

# # basic query
# @app.get("/products")
# async def get_products(search:str |None =None):
#     if search:
#         search_lower=search.lower()
#         filter_products= []
#         for product in PRODUCTS:
#             if search_lower in product['title'].lower():
#                 filter_products.append(product)
#         return filter_products
#     return PRODUCTS



# # validation without annotated
# @app.get("/products")
# async def get_products(
#     search: str | None = Query(default=None, max_length=5)
# ):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []

#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)

#         return filtered_products

#     return PRODUCTS


# # validation with annotated
# @app.get("/products")
# async def get_products(
#     search: Annotated[str | None ,Query (max_length=5)]=None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []

#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)

#         return filtered_products

#     return PRODUCTS


# # validation with annotated , regular expresion
# @app.get("/products")
# async def get_products(
#     search: Annotated[str | None ,Query ( max_length=5,pattern="^[a-z]+$" )]=None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []

#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)

#         return filtered_products

#     return PRODUCTS
          
          
          
          
# # multiple search term (list)
# @app.get("/products")
# async def get_products(
#     search: Annotated[list[str] | None , Query()]=None ):
#     if search:
#         filtered_products = []

#         for product in PRODUCTS:
#            for s in search:
#                if s.lower() in product["title"].lower():
#                    filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS 


# # alias
# @app.get("/products")
# async def get_product(search: Annotated[list[str] | None, Query(alias="q")]=None):
#     if search:
#         filter_products=[]
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product['title'].lower():
#                     filter_products.append(product)
#         return filter_products
#     return PRODUCTS


# # adding metadata 
# @app.get("/products")
# async def get_product(search: Annotated[list[str] | None, Query(alias="q",title="search products",description="search by products")]=None):
#     if search:
#         filter_products=[]
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product['title'].lower():
#                     filter_products.append(product)
#         return filter_products
#     return PRODUCTS        
        
        
## deprecating parameter
# @app.get("/products")
# async def get_product(search: Annotated[list[str] | None, Query(deprecated=True)]=None):
#     if search:
#         filter_products=[]
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product['title'].lower():
#                     filter_products.append(product)
#         return filter_products
#     return PRODUCTS    


# #custom validation
# @app.get("/products")
# async def get_product(search: Annotated[list[str] | None, Query(deprecated=True)]=None):
#     if search:
#         filter_products=[]
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product['title'].lower():
#                     filter_products.append(product)
#         return filter_products
#     return PRODUCTS   



# def check_valid_id(id: str):
#     if not id.startswith("prod-"):
#         raise ValueError("id must start with 'prod-'")
#     return id

# @app.get("/products/")
# async def get_products(
#     id: Annotated[str | None, AfterValidator(check_valid_id)] = None
# ):
#     if id:
#         return {"id": id, "message": "valid product id"}

#     return {"message": "no id provided"} 


PRODUCTS = [
    {"id": 1, "title": "Laptop", "price": 50000},
    {"id": 2, "title": "Mobile", "price": 20000},
    {"id": 3, "title": "Mouse", "price": 500},
]



@app.get("/products/{product_id}")
async def get_product(
    product_id: Annotated[int, Path(ge=1,le=3)]
):
    for product in PRODUCTS:
        if product.get("id") == product_id:
            return product

    return {"error": "product not found"}

