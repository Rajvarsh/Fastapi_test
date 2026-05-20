from fastapi import FastAPI

app=FastAPI()


# Get request

## read or fetch all 
@app.get("/product")
async def all_products(): 
    return {"response":"All Products"}


## read or fetch all 
@app.get("/product")
async def all_products(): 
    return {"response":"All Products"}