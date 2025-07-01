from fastapi import FastAPI





app = FastAPI(titile="RagBot")





@app.get("/test")
async def test():
    return {"message":"Testing sucessful...."}