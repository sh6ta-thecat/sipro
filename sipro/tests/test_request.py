import sys
import os

# Agrega la carpeta raíz 'sipro' al sistema de rutas de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sipro_core.services.installation_service import (InstallationService,)
from sipro_database.session_manager import (get_session,)
from sipro_database.repositories.installation_repository import (InstallationRepository,)


def main():

    file_path = r"C:\Temp\chrome.exe"

    service = InstallationService()

    request = service.create_request(
        file_path
    )

    print("\nSolicitud creada:")
    print(request)

    with get_session() as db:

        repo = InstallationRepository(db)

        installation_id = repo.create(
            request
        )

        print(
            f"\nInstalación registrada con ID: {installation_id}"
        )


if __name__ == "__main__":
    main()