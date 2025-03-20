import dataclasses
import uuid


@dataclasses.dataclass(kw_only=True, frozen=True)
class User:
    id: uuid.UUID
    email: str