import logging

from logging.handlers import RotatingFileHandler

from sipro_core.settings import Settings


class LoggerFactory:

    @staticmethod
    def create_logger(name: str, file_path):

        logger = logging.getLogger(name)

        logger.setLevel(logging.INFO)

        if logger.handlers:
            return logger

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        handler = RotatingFileHandler(
            file_path,
            maxBytes=5 * 1024 * 1024,
            backupCount=10,
            encoding="utf-8",
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

        return logger


system_logger = LoggerFactory.create_logger(
    "SISTEMA",
    Settings.SYSTEM_LOG,
)

error_logger = LoggerFactory.create_logger(
    "ERROR",
    Settings.ERROR_LOG,
)

security_logger = LoggerFactory.create_logger(
    "SEGURIDAD",
    Settings.SECURITY_LOG,
)

installation_logger = LoggerFactory.create_logger(
    "INSTALACION",
    Settings.INSTALL_LOG,
)