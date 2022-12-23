from fastapi import HTTPException, status
from ride import schemas, models
from sqlalchemy.orm import Session


class MatchRides:

    @classmethod
    def get_rides(cls, requester_id: int, db: Session, page: int, limit: int):
        matching_rides = MatchRides.create_matching_rides(requester_id, db)
        offset_page = page - 1
        return matching_rides[offset_page:limit] if limit != -1 else matching_rides

    @classmethod
    def create_matching_rides(cls, requester_id: int, db: Session):
        '''
        Creates record for matched ride in MatchedRide table if records already doesn't exists
        '''
        rides = db.query(models.RiderDetails).all()
        requester = db.query(models.TransportRequest).filter(models.TransportRequest.id==requester_id).first()
        matched_rides = db.query(models.MatchedRides).filter(models.MatchedRides.requester_id==requester_id).all()

        rides_details = []
        # adding already present matched rides's details
        rides_details.extend(matched_rides)
        # adding rider's id to list    
        matched_riders= [matched_ride.rider_id for matched_ride in matched_rides]
        #if requester is valid
        if requester:
            for ride in rides:
                # check if required details matches of rider and requester and it doesn't already exists in table
                if ride.to_address == requester.to_address \
                and ride.from_address == requester.from_address \
                and ride.date_time.date()==requester.date_time.date() \
                and ride.assets_quantity >= requester.assets_quantity \
                and ride.id not in matched_riders:

                    matched_riders.append(ride.id)
                    # create a new record for new match
                    new_match = models.MatchedRides( 
                                    rider_id=ride.id,
                                    from_address=ride.from_address, 
                                    to_address=ride.to_address,
                                    date_time=ride.date_time,
                                    assets_quantity=ride.assets_quantity,
                                    requester_id=requester_id)
                    db.add(new_match)
                    db.commit()
                    rides_details.append(new_match)
        return rides_details