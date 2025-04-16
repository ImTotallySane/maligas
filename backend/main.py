from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.items import router as items_router
from backend.routes.analytics import router as analytics_router
from backend.routes.quiz import router as quiz_router
from backend.routes.users import router as users_router

app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins including file:// protocol
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(items_router, prefix="/items", tags=["Items"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
app.include_router(quiz_router, prefix="/quiz", tags=["Quiz"])
app.include_router(users_router, prefix="/users", tags=["Users"])

@app.get("/home")
async def get_home():
    return {"message": "Welcome to the Multi-Page FastAPI App!"}
