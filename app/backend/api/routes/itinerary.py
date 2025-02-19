from fastapi import APIRouter, HTTPException, Depends
from models.itineraryModel import ItineraryRequest, ItineraryResponse
from services.itinerary_service import generate_itinerary

router = APIRouter()

@router.get("/")
async def get_itinerary():
    return {"message": "This is the default itinerary"}

@router.post("/generate")
async def generate_new_itinerary(request: ItineraryRequest):
    try:
        itinerary_generated = await generate_itinerary(request.destination, request.days)
        return itinerary_generated
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
