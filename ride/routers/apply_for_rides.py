from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ride import database, schemas, models
from ride.functions import apply_for_ride

get_db = database.get_db
router = APIRouter(prefix='/apply_for_rides',
            tags=['Apply_for_Rides'])

@router.post('', status_code=status.HTTP_201_CREATED)
def apply_for_rides(requester_id: int, rider_id: int, db: Session = Depends(get_db)):
    return apply_for_ride.ApplyRide.apply_ride(requester_id, rider_id, db)