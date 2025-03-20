import uuid

from sqlalchemy import Column, UUID, func, MetaData
from sqlalchemy.orm import registry

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

def some_common_columns_factory() -> list[Column]:
    return [
        Column(
            "id",
            UUID(),
            nullable=False,
            primary_key=True,
            default=uuid.uuid4,
            server_default=func.gen_random_uuid(),
        ),
        # ... other common cols like created_at, updated_at, created_by_id, updated_by_id, deleted_at, etc
    ]