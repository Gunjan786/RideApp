from sqlalchemy.orm import Session
from ride import models, schemas
from fastapi import HTTPException, status

class Sensitivity:

    @classmethod
    def create(cls, request : schemas.CreateSensitivities, db : Session):
        '''
        creates sensitivities i.e 
        1. NORMAL
        2. SENSITIVE
        3. HIGHLY_SENSITIVE
        we can create other sensitivities according to need
        '''
        new_sens = models.Sensitivity(sensitivity=request.sensitivity)

        db.add(new_sens)
        db.commit()
        db.refresh(new_sens)
        return new_sens

    @classmethod
    def show(cls, db:Session):
        sensitivities = db.query(models.Sensitivity).all()
        return sensitivities

    @classmethod
    def delete_sens(cls, senst: str, db: Session):
        sensitivity = db.query(models.Sensitivity).filter(models.Sensitivity.sensitivity==senst)
        
        if not sensitivity.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensitivity not found")
        
        sensitivity.delete(synchronize_session=False)
        db.commit()
        return "done"