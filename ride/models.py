from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
from ride.database import Base
from sqlalchemy.orm import relationship

class AssetType(Base):
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True, index=True)
    asset_type = Column(String, unique=True, index=True)
    

class Sensitivity(Base):
    __tablename__ = 'sensitivities'

    id = Column(Integer, primary_key=True, index=True)
    sensitivity = Column(String, unique=True, index=True)

class TransportRequest(Base):
    __tablename__ = 'transport_requests'

    id = Column(Integer, primary_key=True, index=True)
    from_address = Column(String) 
    to_address = Column(String)
    flexible_timings = Column(Boolean)
    date_time = Column(DateTime)
    no_of_assets = Column(Integer)
    asset_type = Column(String)
    asset_sensitivity = Column(String)
    whom_to_deliever = Column(String)
    status = Column(String, default='pending')

class RiderDetails(Base):
    __tablename__ = 'rider_details'

    id = Column(Integer, primary_key=True, index=True)
    from_address = Column(String) 
    to_address = Column(String)
    flexible_timings = Column(Boolean)
    date_time = Column(DateTime)
    travel_medium = Column(String)
    assets_quantity = Column(Integer)

class MatchedRides(Base):

    __tablename__ = 'matched_rides'
    matched_id = Column(Integer, primary_key=True, index=True)
    rider_id = Column(Integer, ForeignKey('rider_details.id'))
    from_address = Column(String) 
    to_address = Column(String)
    date_time = Column(DateTime)
    assets_quantity = Column(Integer)
    requester_id = Column(Integer, ForeignKey('transport_requests.id'))
    booking_status = Column(String, default='NOT APPLIED')

    
    