from fastapi import HTTPException, status
from ride import models
from sqlalchemy.orm import Session

class ApplyRide:
    
    @classmethod
    def apply_ride(cls, requester_id: int, ride_id: int, db: Session):
        '''
        Apply for rides
        '''

        request = {'booking_status' : 'APPLIED'}

        # get the matched ride for given request and rider id
        matched_ride = db.query(models.MatchedRides).filter(
            models.MatchedRides.requester_id==requester_id).filter(
            models.MatchedRides.rider_id==ride_id)

        if not matched_ride.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Matched Ride not found for requester id : {requester_id} and rider id : {ride_id}')
        # update value to applied for the ride
        matched_ride.update(request)
        db.commit()
        return 'applied successfully for ride_id : {}'.format(ride_id)