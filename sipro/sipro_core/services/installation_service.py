import getpass
import socket

from sipro_core.entities.installation import Installation
from sipro_core.constants import InstallationStatus

from sipro_security.hash_manager import HashManager
from sipro_security.validators import FileValidator
from sipro_security.file_info import FileInfo


class InstallationService:

    def create_request(
        self,
        file_path: str,
    ) -> Installation:

        if not FileValidator.validate_exists(file_path):
            raise FileNotFoundError(
                f"Archivo no encontrado: {file_path}"
            )

        if not FileValidator.validate_extension(file_path):
            raise ValueError(
                "Extensión no permitida"
            )

        return Installation(
            id=None,
            username=getpass.getuser(),
            computer_name=socket.gethostname(),
            filename=FileInfo.filename(file_path),
            full_path=file_path,
            sha256=HashManager.sha256(file_path),
            status=InstallationStatus.PENDING.value,
            file_size=FileInfo.size(file_path),
        )