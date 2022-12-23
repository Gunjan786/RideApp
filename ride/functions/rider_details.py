from fastapi import HTTPException, status
from ride import models, schemas
from sqlalchemy.orm import Session

class Rider:

    valid_travel_medium = ['BUS', 'TRAIN', 'CAR']

    @classmethod
    def create(cls, request: schemas.RiderDetails, db: Session):
        
        if request.travel_medium not in cls.valid_travel_medium:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                    details=f'{request.travel_medium} is not a valid travel medium')

        details = models.RiderDetails(
            from_address=request.from_address,
            to_address=request.to_address,
            flexible_timings=request.flexible_timings,
            date_time=request.date_time,
            travel_medium=request.travel_medium,
            assets_quantity=request.assets_quantity
        )

        db.add(details)
        db.commit()
        db.refresh(details)
        return details