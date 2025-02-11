from sqlalchemy import create_engine, Engine

from config.settings import FilesPaths

# engine: Engine = create_engine("sqlite://", echo=True)  # Работа в памяти
engine: Engine = create_engine(f"sqlite:///{FilesPaths.DB_FILE}", echo=True)  # Работа в файле