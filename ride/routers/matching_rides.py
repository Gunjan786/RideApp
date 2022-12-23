from fastapi import APIRouter, Depends
from ride import schemas, database
from sqlalchemy.orm import Session
from ride.functions import matching_rides
from typing import List

router = APIRouter(prefix='/matching_rides',
        tags=['Matching_Rides'])
    
get_db = database.get_db

@router.get('/{id}', response_model=List[schemas.MatchedRidesResponse])
def get_matching_rides(requester_id: int, db: Session = Depends(get_db), page: int = 1, limit: int = -1):
    return matching_rides.MatchRides.get_rides(requester_id, db, page, limit)