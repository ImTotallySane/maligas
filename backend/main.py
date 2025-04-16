from fastapi import FastAPI

# ✅ Use absolute imports assuming you run from the project root (maligas/)
from backend.routes.items import router as items_router
from backend.routes.analytics import router as analytics_router
from backend.routes.quiz import router as quiz_router
from backend.routes.users import router as users_router  # ✅ You were missing users

app = FastAPI()

# ✅ Register all routers with appropriate prefixes
app.include_router(items_router, prefix="/items", tags=["Items"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
app.include_router(quiz_router, prefix="/quiz", tags=["Quiz"])
app.include_router(users_router, prefix="/users", tags=["Users"])

# ✅ Optional home route for health check or basic welcome message
@app.get("/home")
async def get_home():
    return {"message": "Welcome to the Multi-Page FastAPI App!"}

