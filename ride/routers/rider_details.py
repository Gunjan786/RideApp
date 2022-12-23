from fastapi import APIRouter, Depends, status
from ride import database, models, schemas
from sqlalchemy.orm import Session
from ride.functions import rider_details

router = APIRouter(
    prefix='/rider_details',
    tags=['Rider Details']
)

get_db = database.get_db

@router.post('', response_model=schemas.RiderDetailsResponse, status_code=status.HTTP_201_CREATED)
def create(request: schemas.RiderDetails, db: Session = Depends(get_db)):
    return rider_details.Rider.create(request, db)