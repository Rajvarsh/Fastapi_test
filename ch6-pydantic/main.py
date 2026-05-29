from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# # create / insert data
# @app.post("/product")
# async def create_product(new_product: dict):
#     return new_product



#with pydantic 

class product(BaseModel):
    id : int
    name : str
    price : float
    stock: int | None = None
    
    
# @app.post("/product")
# async def create_product(new_product: product):
#     return new_product

# Access Atribute inside function
# @app.post("/product")
# async def create_product(new_product: product):
#     print(new_product.id)
#     print(new_product.name)
#     print(new_product.price)
#     print(new_product.stock)
#     return new_product


# ## new calculated attributes
# @app.post("/product")
# async def create_product(new_product: product):
#     product_dict=new_product.model_dump()
#     price_with_text=new_product.price +(new_product.price*18)/100
#     product_dict.update({"price_with_text":price_with_text})
    
#     return product_dict


## COMBINING REQUEST BODY WITH PARAMETER    
@app.put("/products/{ product_id }")
async def update_product(product_id: int ,new_updated_product:product):
    return {
            "product_id":product_id,
            "new_updated_product":new_updated_product
            }