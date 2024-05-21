from fastapi import FastAPI

from api.routes import router


def get_app() -> FastAPI:
    app = FastAPI(title="Toy Robot", version="0.0.1")
    app.include_router(router)

    return app


app = get_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
