import os

from fastapi import FastAPI

from .config import get_config
from .routes import register_routes

settings = get_config()


app = FastAPI(title="Fasterific API")
# app.config.from_object(config_by_name[env or "test"])

register_routes(app)
# db.init_app(app)

print(settings)


@app.get("/")
def index():
    return settings.CONFIG_NAME


@app.get("/health")
def health():
    return {"status": "healthy"}

