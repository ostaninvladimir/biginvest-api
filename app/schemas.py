from typing import Optional, List
from pydantic import BaseModel


# -------------------------
# Вложенные модели
# -------------------------

class Lot(BaseModel):
    id: int
    title: str
    city: str
    block: str
    price: str
    slug: str
    tags: List[str]


class Customer(BaseModel):
    name: str
    phone: str


# -------------------------
# Модели для запросов
# -------------------------

class ApplicationCreate(BaseModel):
    lotId: int
    lotTitle: str
    lotCity: str
    lotBlock: str
    lotPrice: str
    lotSlug: str
    lotTags: List[str] = []

    customerName: str
    customerPhone: str

    contactMethod: str
    timeSlot: str
    comment: Optional[str] = None


class ApplicationStatusUpdate(BaseModel):
    status: str
    managerId: str
    comment: Optional[str] = None


# -------------------------
# Модель ответа (как backend реально возвращает!)
# -------------------------

class Application(BaseModel):
    id: str
    status: str
    createdAt: str
    timeSlot: str
    contactMethod: str

    comment: Optional[str] = None
    updatedBy: Optional[str] = None

    customer: Customer
    lot: Lot
