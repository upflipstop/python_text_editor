import logging
from pathlib import Path
from datetime import datetime

def setup_logger(name: str) -> logging.Logger:
    """
    Настройка логгера для приложения
    
    Args:
        name: Имя логгера
        
    Returns:
        logging.Logger: Настроенный логгер
    """
    # Создаем директорию для логов если её нет
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    # Формируем имя файла лога с текущей датой
    log_file = log_dir / f"{datetime.now().strftime('%Y-%m-%d')}.log"
    
    # Настраиваем форматирование
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Настраиваем обработчик файла
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    # Настраиваем обработчик консоли
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Создаем и настраиваем логгер
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger 