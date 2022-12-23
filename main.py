from fastapi import FastAPI
from ride import models
import uvicorn
import cron_job
from ride.database import engine
from ride.routers import (
                        asset_types, 
                        sensitivity,
                        asset_transport_request,
                        rider_details,
                        matching_rides, 
                        apply_for_rides
                        )
from fastapi_utils.tasks import repeat_every



app = FastAPI()

models.Base.metadata.create_all(engine)


# this job is to update records which are expired 
# it runs on startup of application and also
# runs every hour to check if any record is expired for requester and change its status to expired.
@app.on_event('startup')
@repeat_every(seconds=3600)
async def update_expired_requests():
    cron_job.update_expired_dates()

app.include_router(asset_types.router)
app.include_router(sensitivity.router)
app.include_router(asset_transport_request.router)
app.include_router(rider_details.router)
app.include_router(matching_rides.router)
app.include_router(apply_for_rides.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)