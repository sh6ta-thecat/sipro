from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Installation:
    id: int | None
    username: str
    computer_name: str
    filename: str
    full_path: str
    status: str
    file_size: int
    start_time: datetime | None = None
    end_time: datetime | None = None
    duration_seconds: int | None = None
    exit_code: int | None = None
    created_at: datetime | None = None
