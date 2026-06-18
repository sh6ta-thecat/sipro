from pathlib import Path
from sipro_core.settings import Settings


class DirectoryManager:
    @staticmethod
    def create_structure():
        directories = [
            Settings.BASE_DIR,
            Settings.QUEUE_DIR,
            Settings.PROCESSING_DIR,
            Settings.COMPLETED_DIR,
            Settings.FAILED_DIR,
            Settings.LOG_DIR,
            Settings.DATABASE_DIR,
            Settings.CONFIG_DIR,
            Settings.TEMP_DIR,
            Settings.CACHE_DIR,
            Settings.REPORTS_DIR,
        ]

        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
