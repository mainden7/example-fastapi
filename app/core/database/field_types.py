from typing import Any

from sqlalchemy import Dialect, String, TypeDecorator

from app.core.utils import aes_decrypt, aes_encrypt


class EncryptedType(TypeDecorator):
    impl = String
    cache_ok = False

    def __init__(self, key: bytes, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self._key = key

    def process_bind_param(self, value: Any, dialect: Dialect) -> str | None:
        if not value:
            return None
        return aes_encrypt(value, self._key).decode()

    def process_result_value(self, value: Any, dialect: Dialect) -> str | None:
        if not value:
            return None
        return aes_decrypt(value, self._key)


class LowercaseText(TypeDecorator):
    impl = String
    cache_ok = False

    def process_bind_param(self, value: Any, dialect: Dialect) -> str:
        return value.lower()
