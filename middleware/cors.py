import os

from fastapi.middleware.cors import CORSMiddleware

_DEFAULT_ORIGINS = "http://localhost:8000, http://localhost:3000, http://127.0.0.1:8000"


def add_cors_middleware(app):
    raw_origins = os.getenv("CORS_ORIGINS", _DEFAULT_ORIGINS)
    origins = [o.strip() for o in raw_origins.split(",") if o.strip()]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization", "Accept"],
    )
