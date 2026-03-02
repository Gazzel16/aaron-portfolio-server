from fastapi import FastAPI
from middleware.cors import add_cors_middleware

from routes.role_route import router as role_router

app = FastAPI()
add_cors_middleware(app)


app.include_router(role_router, prefix="/api/role")

@app.get("/")
def read_root():
    return {"status": "Server is running"}