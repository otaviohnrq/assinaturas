from sqlmodel import Field, SQLModel, create_engine
from typing import Optional
from datetime import date
from decimal import Decimal

class Subscription(SQLModel, table=True):
    id: int = Field(primary_key=True)
    empresa: str 
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal


