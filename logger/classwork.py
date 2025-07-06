import logging

from log_event_module import file_handler

#1
logging.basicConfig(
    level=logging.DEBUG,

    format="%(asctime)s - %(levelname)s - %(message)s"

)

def add(a=0, b=0):
    logging.info("Функція запущена")
    if a == 0 or b == 0:
        logging.warning("Використовуються дефолтні значення!")
    if isinstance(a,int) and isinstance(b, int):
        logging.info("Функція отримала числа!")
    elif isinstance(a,str) and isinstance(b, str):
        logging.info("Функція отримала рядки!")
    elif (isinstance(a,str) and isinstance(b, int)) or (isinstance(a,int) and isinstance(b, str)):
        logging.error("Різний формат даних")
        return None
    else:
        logging.fatal("Усьо невірно")
        return None
    result = a + b
    logging.info(f"Отримали результат {result}")
    return result

add(2, 0)






# logging.debug("Дебаг працює")
# logging.info("Програма запущена")
# logging.warning("Щось пішло не так")
# logging.error("Критична помилка")
# logging.fatal("Пропало всьо!")




#2
# Створюємо логер
logger = logging.getLogger("lecture_logger")


# Створюємо хендлер (консоль)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("class_log.log", mode='w')

console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.WARNING)

# %(asctime)s   — Час логування
# %(levelname)s — Рівень логування (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# %(message)s   — Основне повідомлення
# %(name)s      — Імʼя логера (що передається у getLogger)
# %(filename)s  — Назва файлу, з якого пішов лог
# %(lineno)d    — Номер рядка у вихідному файлі
# %(funcName)s  — Назва функції, в якій виконується лог


# Форматер
console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s -  %(filename)s")
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Додаємо хендлер до логера
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# def add(a=0, b=0):
#     logger.debug("Функція запущена")
#     if a == 0 or b == 0:
#         logger.warning("Використовуються дефолтні значення!")
#     if isinstance(a,int) and isinstance(b, int):
#         logger.info("Функція отримала числа!")
#     elif isinstance(a,str) and isinstance(b, str):
#         logger.info("Функція отримала рядки!")
#     elif (isinstance(a,str) and isinstance(b, int)) or (isinstance(a,int) and isinstance(b, str)):
#         logger.error("Різний формат даних")
#         return None
#     else:
#         logger.fatal("Усьо невірно")
#         return None
#     result = a + b
#     logger.debug(f"Отримали результат {result}")
#     return result
#
# add(2, 0)


def add(a, b):
    try:
        return a + b
    except Exception as e:
        logger.error(f"Сталася помилка: {e}. Були використані аргументи: {a}, {b}")

add(1, "2")




#3
# Глобальний логер
logger = logging.getLogger("multi_handler_logger")
logger.setLevel(logging.DEBUG)

logger_error  = logging.getLogger("Error Logger")
logger.setLevel(logging.ERROR)

logger_info  = logging.getLogger("Info Logger")
logger.setLevel(logging.INFO)

# Хендлер у консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Хендлер у файл
file_handler = logging.FileHandler("app.log", mode="a")
file_handler.setLevel(logging.DEBUG)

# Форматер
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Додаємо хендлери
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Приклад логування
logger.info("Інформація відображається і в консоль, і в файл")
logger.debug("Це debug — тільки у файл")

