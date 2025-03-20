import uuid

from pydantic import BaseModel


class OrderLineGET(BaseModel):
    id: uuid.UUID
    # ... some other data


class OrderLinePOST(BaseModel): ...


class OrderGET(BaseModel):
    id: uuid.UUID
    order_lines: list[OrderLineGET]


class OrderPOST(BaseModel):
    order_lines: list[OrderLinePOST]
