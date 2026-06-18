from abc import ABC, abstractmethod
from sipro_core.entities.installation import Installation


class IInstallationRepository(ABC):

    @abstractmethod
    def create(self, installation: Installation):
        pass

    @abstractmethod
    def get_by_id(self, installation_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, installation: Installation):
        pass
