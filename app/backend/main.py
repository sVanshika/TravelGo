from fastapi import FastAPI
from api.routes.itinerary import router

app = FastAPI(title="Travel Go: AI Agentic Travel Planner")

app.include_router(router, prefix='/itinerary')