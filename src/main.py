import uvicorn
from fastapi import Depends, FastAPI

from .config import Config, get_config
from .routes import items

app = FastAPI(
    title="news",
    description="News Client",
)

app.include_router(items.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/app_name")
def read_settings(settings: Config = Depends(get_config)):
    return settings.app_name

if __name__ == "__main__":
    print("Swagger page launched at http://127.0.0.1:57765/docs")
    uvicorn.run(app, host="127.0.0.1", port=57765)
