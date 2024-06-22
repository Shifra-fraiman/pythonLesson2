import logging

def my_decorator_log(message):
    def wrraper_logging(func):
        logging.basicConfig(level=logging.INFO)
        logging.info(message)
        file_handler = logging.FileHandler("example.txt")
        logger = logging.getLogger()
        logger.addHandler(file_handler)
        func()
    return wrraper_logging

@my_decorator_log("mmmmm..........")
def my_func():
    print("in my func!")
