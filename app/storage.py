from datetime import datetime

# Хранилище заявок (вместо базы данных)
applications = {}


def save_application(app):
    applications[app["id"]] = app
    return app


def get_application(app_id: str):
    return applications.get(app_id)


def get_new_applications():
    return [
        app for app in applications.values()
        if app["status"] == "NEW"
    ]


def update_application(app_id: str, fields: dict):
    app = applications.get(app_id)
    if not app:
        return None

    for key, value in fields.items():
        app[key] = value

    app["updatedAt"] = datetime.utcnow().isoformat()

    applications[app_id] = app
    return app
