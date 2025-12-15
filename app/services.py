from datetime import datetime
from .storage import save_application, update_application, get_application


def create_application(data):
    app_id = f"A-{int(datetime.utcnow().timestamp())}"

    app = {
        "id": app_id,
        "status": "NEW",
        "managerId": None,
        "comment": None,

        "lotId": data.lotId,
        "lotTitle": data.lotTitle,
        "lotCity": data.lotCity,
        "lotBlock": data.lotBlock,
        "lotPrice": data.lotPrice,
        "lotSlug": data.lotSlug,
        "lotTags": data.lotTags,

        "customerName": data.customerName,
        "customerPhone": data.customerPhone,
        "contactMethod": data.contactMethod,
        "timeSlot": data.timeSlot,

        "createdAt": datetime.utcnow().isoformat(),
        "updatedAt": None,
    }

    return save_application(app)


def update_status(app_id, update):
    if not get_application(app_id):
        return None

    return update_application(app_id, {
        "status": update.status,
        "managerId": update.managerId,
        "comment": update.comment
    })
