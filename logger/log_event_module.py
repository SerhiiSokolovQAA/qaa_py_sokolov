import logging

LOG_FILE = "login_system.log"


logger = logging.getLogger("log_event")
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE, mode='a')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def log_event(username: str, status: str):

    log_message = f"Login event - Username: {username}, Status: {status}"

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

if __name__ == "__main__":
    log_event("admin", "success")
    log_event("admin", "expired")
    log_event("admin", "failed")
    log_event("admin", "unknown")
    print(f"Created Log file: {LOG_FILE}")