from datetime import datetime
from typing import List

from app.schemas import (
    Application,
    ApplicationCreate,
)

_db: List[Application] = []
_id = 1


def create_application(payload: ApplicationCreate) -> Application:
    global _id

    app = Application(
        id=_id,
        createdAt=datetime.utcnow().isoformat(),
        status="NEW",
        lot={
            "title": payload.lotTitle,
            "city": payload.lotCity,
            "block": payload.lotBlock,
            "price": payload.lotPrice,
            "tags": payload.lotTags,
        },
        customer={
            "name": payload.customerName,
            "phone": payload.customerPhone,
        },
        contactMethod=payload.contactMethod,
        timeSlot=payload.timeSlot,
        comment=payload.comment,
    )

    _db.append(app)
    _id += 1
    return app


def get_new_applications():
    return [a for a in _db if a.status == "NEW"]


def update_application_status(app_id: int, status: str, manager_id: str, comment: str | None):
    for app in _db:
        if app.id == app_id:
            app.status = status
            app.managerId = manager_id
            app.comment = comment
            return app
    raise ValueError("Application not found")
