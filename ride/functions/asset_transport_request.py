from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from ride import models, schemas
from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.sql import select

class Requester:
    @classmethod
    def create(cls, request: schemas.AssetTransport, db: Session):

        valid_assets = [record.asset_type for record in db.query(models.AssetType).all()]
        valid_sensitivities = [record.sensitivity for record in db.query(models.Sensitivity).all()]
        
        if request.asset_type not in valid_assets or request.asset_sensitivity not in valid_sensitivities:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f'either of asset_type or asset_sensitivity is not valid')

        new_order_request = models.TransportRequest(
            from_address=request.from_address,
            to_address=request.to_address,
            flexible_timings=request.flexible_timings,
            date_time=request.date_time,
            no_of_assets=request.no_of_assets,
            asset_type=request.asset_type,
            asset_sensitivity=request.asset_sensitivity,
            whom_to_deliever=request.whom_to_deliever
            )

        db.add(new_order_request)
        db.commit()
        db.refresh(new_order_request)

        return new_order_request

    @classmethod
    def get_all_requests(cls, db: Session,
        page: int,
        limit: int,
        sort: str,
        filter: str):

        query = select(from_obj=models.TransportRequest, columns="*")
        
        # select filter on any column like status, asset_type
        if filter is not None and filter != "null":
            # we need filter format data like this  --> {'status': 'abc','asset_type':'abc'}
            criteria = dict(x.split("*") for x in filter.split('-'))

            query = query.filter_by(**criteria)

        # select sort based on date_time
        # if we want to sort on some other columns we can replace the if condition with the following condition
        # if sort is not None and sort != "null"
        if sort == 'date_time':
            # we need sort format data like this --> ['datetime',]
            query = query.order_by(text(Requester.convert_sort(sort)))


        offset_page = page - 1
        # pagination
        if limit != -1:
            query = (query.offset(offset_page * limit).limit(limit))

        #execute final query
        result = (db.execute(query)).fetchall()
        return schemas.PageResponse(
            page_number=page,
            page_size=limit,
            content=result
        )

    @staticmethod
    def convert_sort(sort):
        """
        separate string using split('-')
        join to list with ','
        """
        return ','.join(sort.split('-'))
