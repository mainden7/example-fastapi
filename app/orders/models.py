import dataclasses
import uuid

from app.users.models import User


@dataclasses.dataclass(kw_only=True, frozen=True)
class Order:
    id: uuid.UUID

    _creator: User | None = dataclasses.field(default=None)
    order_lines: list["OrderLine"] = dataclasses.field(default_factory=list)

    @property
    def creator(self) -> User:
        if self._creator is None:
            raise AttributeError("creator is not set")
        return self._creator



@dataclasses.dataclass(kw_only=True, frozen=True)
class OrderLine:
    id: uuid.UUID
