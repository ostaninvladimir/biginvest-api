from fastapi import FastAPI, HTTPException

from schemas import (
    Application,
    ApplicationCreate,
    ApplicationStatusUpdate,
)
import storage

app = FastAPI(title="BIG Invest API")


@app.post("/applications", response_model=Application)
def create_application(payload: ApplicationCreate):
    return storage.create_application(payload)


@app.get("/applications/new", response_model=list[Application])
def get_new_applications():
    return storage.get_new_applications()


@app.post("/applications/{app_id}/status", response_model=Application)
def update_status(app_id: int, payload: ApplicationStatusUpdate):
    try:
        return storage.update_application_status(
            app_id=app_id,
            status=payload.status,
            manager_id=payload.managerId,
            comment=payload.comment,
        )
    except ValueError:
        raise HTTPException(status_code=404, detail="Application not found")
