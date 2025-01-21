from typing import Union

from fastapi import APIRouter, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from user.router import user_router
from organization.router import organization_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def http_exception_handler(request, exc: Exception):
    #log exception
    print(request, exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=dict(detail=dict(message="Internal Server Error")),
    )

@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(user_router)
app.include_router(organization_router)
