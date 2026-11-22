import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.video_routes import router as video_router

load_dotenv()

app = FastAPI(title="VEYRA API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_ORIGIN", "http://localhost:5173")],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(video_router, prefix="/api/video", tags=["video"])


@app.get("/health")
def health():
    return {"status": "ok"}
