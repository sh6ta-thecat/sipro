from sipro_core.directories import DirectoryManager
from sipro_database.models import Base
from sipro_database.database import engine

def initialize():
    DirectoryManager.create_structure()
    Base.metadata.create_all(bind=engine)
    print("SIPRO inicializado correctamente")

if __name__ == "__main__":
    initialize()