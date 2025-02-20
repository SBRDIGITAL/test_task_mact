import logging

# Настройка логирования
logging.basicConfig(
    encoding='utf-8',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("backend.log"),  # Логи в файл
        logging.StreamHandler(),  # Логи в консоль
    ],
)
logger = logging.getLogger(__name__)
