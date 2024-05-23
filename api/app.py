from fastapi import FastAPI

from api.routes import router
from fastapi.middleware.cors import CORSMiddleware


def get_app() -> FastAPI:
    app = FastAPI(title="Toy Robot", version="0.0.1") # Create FastAPI class
    app.include_router(router) # Add routes

    # Add CORS middleware to allow frontend to communicate to API
    app.add_middleware(
        CORSMiddleware, 
        allow_origins="http://localhost:5173", # replace with frontend origin URL
        allow_methods=["*"], 
        allow_headers=["*"]
    )

    return app


app = get_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
