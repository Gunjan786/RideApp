from sqlalchemy.orm import Session
from ride import schemas, models
from fastapi import HTTPException, status

class AssetTypes:

    @classmethod
    def create(cls, request: schemas.CreateAssetTypes, db: Session):
        '''
        creates asset_types i.e 
        1. LAPTOP
        2. TRAVEL BAG
        3. PACKAGE
        we can create other asset_types according to need
        '''
        new_asset_type = models.AssetType(asset_type=request.asset_type)

        db.add(new_asset_type)
        db.commit()
        db.refresh(new_asset_type)

        return new_asset_type

    @classmethod
    def show_asset_types(cls, db:Session):
        asset_types =  db.query(models.AssetType).all()
        return asset_types
    
    @classmethod
    def delete_asset_type(cls, asset_type: str, db: Session):
        asset = db.query(models.AssetType).filter(models.AssetType.asset_type == asset_type)

        if not asset.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Asset not found")

        asset.delete(synchronize_session=False)
        db.commit()
        return 'done'