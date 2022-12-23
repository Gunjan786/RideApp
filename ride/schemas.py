from typing import Optional, List, Generic, TypeVar
from pydantic import BaseModel
from datetime import datetime
from pydantic.generics import GenericModel

T = TypeVar('T')

class CreateAssetTypes(BaseModel):
    asset_type : str

class CreateSensitivities(BaseModel):
    sensitivity : str

class AssetTypes(CreateAssetTypes):
    class Config():
        orm_mode = True

class Sensitivities(CreateSensitivities):
    class Config():
        orm_mode = True

class CreateTravelMedium(BaseModel):
    travel_medium : str

class TravelMedium(CreateTravelMedium):
    class Config():
        orm_mode = True 

class MetaData(BaseModel):
    from_address : str 
    to_address : str
    flexible_timings : bool = False
    date_time : Optional[datetime] = datetime.min

class AssetTransport(MetaData):
    no_of_assets : int
    asset_type : str
    asset_sensitivity : str
    whom_to_deliever : str

class AssetTransportResponse(AssetTransport):
    class Config():
        orm_mode = True

class RiderDetails(MetaData):
    travel_medium : str
    assets_quantity : int

class RiderDetailsResponse(RiderDetails):
    class Config():
        orm_mode = True

class PageResponse(GenericModel, Generic[T]):
    """ The response for a pagination query. """

    page_number: int
    page_size: int
    content: List[T]

class MatchedRidesResponse(MetaData):
    rider_id : int
    assets_quantity : int
    booking_status : str = 'NOT APPLIED'
    class Config():
        orm_mode = True

