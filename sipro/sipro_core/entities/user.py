from dataclasses import dataclass


@dataclass(slots=True)
class User:
    id: int | None
    username: str
    total_installations: int = 0
    successful_installations: int = 0
    failed_installations: int = 0
