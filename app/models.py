from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class Lot(BaseModel):
    id: int
    title: str
    city: str
    block: str
    price: str
    slug: str
    tags: List[str] = []

class Customer(BaseModel):
    name: str
    phone: str

class ApplicationModel(BaseModel):
    id: str
    createdAt: str
    status: str
    customer: Customer
    contactMethod: str
    timeSlot: str
    comment: Optional[str]
    lot: Lot
    updatedBy: Optional[str] = None
