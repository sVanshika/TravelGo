import requests
from models.itineraryModel import ItineraryResponse
from core.config import settings

async def generate_itinerary(destination, days):
    return f"Generated Itinerary for {destination} and {days} days"