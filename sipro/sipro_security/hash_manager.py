import hashlib
from pathlib import Path


class HashManager:

    CHUNK_SIZE = 8192

    @classmethod
    def sha256(cls, file_path: str) -> str:

        path = Path(file_path)

        sha = hashlib.sha256()

        with open(path, "rb") as file:

            while chunk := file.read(cls.CHUNK_SIZE):
                sha.update(chunk)

        return sha.hexdigest()