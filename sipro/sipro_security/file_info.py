from pathlib import Path


class FileInfo:

    @staticmethod
    def size(file_path: str) -> int:

        return Path(file_path).stat().st_size

    @staticmethod
    def filename(file_path: str) -> str:

        return Path(file_path).name
