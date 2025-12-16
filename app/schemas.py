from pydantic import BaseModel
from typing import List, Optional


# -------- INPUT --------
class ApplicationCreate(BaseModel):
    lotId: int
    lotTitle: str
    lotCity: str
    lotBlock: str
    lotPrice: str
    lotSlug: Optional[str] = None
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


# -------- OUTPUT --------
class Lot(BaseModel):
    title: str
    city: str
    block: str
    price: str
    tags: List[str] = []


class Customer(BaseModel):
    name: str
    phone: str


class Application(BaseModel):
    id: int
    createdAt: str
    status: str

    lot: Lot
    customer: Customer

    contactMethod: str
    timeSlot: str
    comment: Optional[str] = None
    managerId: Optional[str] = None
