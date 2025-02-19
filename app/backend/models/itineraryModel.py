from pydantic import BaseModel

class ItineraryRequest(BaseModel):
    destination: str
    days: int

class ItineraryResponse(BaseModel):
    destination: str
    days: int
    details: str
