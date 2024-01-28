from decimal import Decimal
from typing import Union

from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    name: str
    description: str
    category: str
    price: Decimal
    quantity: int
