from fastapi import APIRouter, Depends, status
from typing import List
from ride import database, schemas
from sqlalchemy.orm import Session
from ride.functions import asset_type

router = APIRouter(
    prefix='/asset_types',
    tags=['AssetTypes']
    )

get_db = database.get_db

@router.post('', response_model=schemas.AssetTypes, status_code=status.HTTP_201_CREATED)
def create_asset_type(request: schemas.CreateAssetTypes, db : Session = Depends(get_db)):
    return asset_type.AssetTypes.create(request, db)

@router.get('', response_model=List[schemas.AssetTypes])
def get_asset_types(db : Session = Depends(get_db)):
    return asset_type.AssetTypes.show_asset_types(db)

@router.delete('/{asset_tp}')
def delete_asset_type(asset_tp: str, db : Session = Depends(get_db)):
    return asset_type.AssetTypes.delete_asset_type(asset_tp, db)
