from fastapi import FastAPI
from api.routes.itinerary import router
from api.routes.auth import router as auth_router

app = FastAPI(title="Travel Go: AI Agentic Travel Planner", docs_url="/docs")
app.include_router(router, prefix='/itinerary')

# Include Authentication Routes
app.include_router(auth_router, prefix='/auth')