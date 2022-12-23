from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ride import database, schemas
from ride.functions import asset_transport_request
from typing import List

router = APIRouter(
    prefix='/asset_transport_request',
    tags=['Asset Transport Request']
)

get_db = database.get_db

@router.post('', response_model=schemas.AssetTransportResponse, status_code=status.HTTP_201_CREATED)
def place_asset_transport_request(request: schemas.AssetTransport, db: Session = Depends(get_db)):
    return asset_transport_request.Requester.create(request, db)

@router.get('', response_model=schemas.PageResponse)
def get_asset_transport_requests(db: Session = Depends(get_db), 
    page: int = 1,
    limit: int = 10,
    sort: str = None,
    filter: str = None):
    return asset_transport_request.Requester.get_all_requests(db, page, limit, sort, filter)
