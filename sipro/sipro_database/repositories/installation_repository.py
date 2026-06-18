from sqlalchemy.orm import Session

from sipro_database.models import Installation as InstallationModel

from sipro_core.entities.installation import Installation

from sipro_core.interfaces.installation_repository import (
    IInstallationRepository,
)


class InstallationRepository(IInstallationRepository):

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        installation: Installation,
    ):

        model = InstallationModel(
            username=installation.username,
            computer_name=installation.computer_name,
            filename=installation.filename,
            full_path=installation.full_path,
            sha256=installation.sha256,
            status=installation.status,
            file_size=installation.file_size,
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model.id

    def get_by_id(
        self,
        installation_id: int,
    ):
        return (
            self.db.query(InstallationModel)
            .filter(InstallationModel.id == installation_id)
            .first()
        )

    def get_all(self):
        return self.db.query(InstallationModel).all()
