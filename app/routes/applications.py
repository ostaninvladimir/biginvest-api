from fastapi import APIRouter, HTTPException
from ..schemas import (
    Application,
    ApplicationCreate,
    ApplicationStatusUpdate
)
from ..services import create_application, update_status
from ..storage import get_new_applications, get_application

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.post("/", response_model=Application)
def create(data: ApplicationCreate):
    app = create_application(data)
    return app


@router.get("/new", response_model=list[Application])
def new():
    return get_new_applications()


@router.get("/{app_id}", response_model=Application)
def get(app_id: str):
    app = get_application(app_id)
    if not app:
        raise HTTPException(404, "Application not found")
    return app


@router.post("/{app_id}/status", response_model=Application)
def set_status(app_id: str, update: ApplicationStatusUpdate):
    app = update_status(app_id, update)
    if not app:
        raise HTTPException(404, "Application not found")
    return app
