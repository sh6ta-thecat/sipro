from pathlib import Path


class Settings:
    BASE_DIR = Path(r"C:\ProgramData\SIPRO")
    QUEUE_DIR = BASE_DIR / "En cola"
    PROCESSING_DIR = BASE_DIR / "Procesando"
    COMPLETED_DIR = BASE_DIR / "Completados"
    FAILED_DIR = BASE_DIR / "Fallidos"

    LOG_DIR = BASE_DIR / "Logs"
    DATABASE_DIR = BASE_DIR / "Database"
    CONFIG_DIR = BASE_DIR / "Config"
    TEMP_DIR = BASE_DIR / "Temp"
    CACHE_DIR = BASE_DIR / "Cache"
    REPORTS_DIR = BASE_DIR / "Reports"

    DATABASE_FILE = DATABASE_DIR / "sipro.db"

    SYSTEM_LOG = LOG_DIR / "system.log"
    INSTALL_LOG = LOG_DIR / "installation.log"
    ERROR_LOG = LOG_DIR / "error.log"
    SECURITY_LOG = LOG_DIR / "security.log"

    APP_NAME = "SIPRO"
    VERSION = "1.0.0"

    HASH_ALGORITHM = "sha256"

    MAX_PARALLEL_INSTALLATIONS = 1
