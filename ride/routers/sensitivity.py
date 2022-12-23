from fastapi import APIRouter, Depends, status
from ride import database, schemas
from ride.functions import sensitivity
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix='/sensitivity',
    tags=['Sensitivity']
)

get_db = database.get_db

@router.post('', response_model=schemas.Sensitivities, status_code=status.HTTP_201_CREATED)
def create_sens(request : schemas.CreateSensitivities, db : Session = Depends(get_db)):
    return sensitivity.Sensitivity.create(request, db)

@router.get('', response_model=List[schemas.Sensitivities])
def show_sens(db : Session = Depends(get_db)):
    return sensitivity.Sensitivity.show(db)

@router.delete('/{senst}')
def delete_sens(senst: str, db : Session = Depends(get_db)):
    return sensitivity.Sensitivity.delete_sens(senst, db)