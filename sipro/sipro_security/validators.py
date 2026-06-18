from pathlib import Path


class FileValidator:

    ALLOWED_EXTENSIONS = {
        ".exe",
        ".msi",
    }

    BLOCKED_EXTENSIONS = {
        ".bat",
        ".cmd",
        ".ps1",
        ".vbs",
        ".js",
        ".scr",
    }

    @classmethod
    def validate_exists(cls, file_path: str):

        return Path(file_path).exists()

    @classmethod
    def validate_extension(cls, file_path: str):

        ext = Path(file_path).suffix.lower()

        if ext in cls.BLOCKED_EXTENSIONS:
            return False

        return ext in cls.ALLOWED_EXTENSIONS