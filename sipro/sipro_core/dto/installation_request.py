from pydantic import BaseModel


class InstallationRequest(BaseModel):
    username: str
    computer_name: str
    filename: str
    full_path: str
    sha256: str
    file_size: int
