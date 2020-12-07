import logging

logging.basicConfig(filename="C:/Projects/PythonLogs/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s', #SET the row syntax
                    level=logging.DEBUG,  #setting the logging with the lowest level of DEBUG
                    datefmt='%d/%m/%y %I:%M:%S %p' #set the date and time syntax
                    )
logging.debug("debug messge")
logging.info("INFO messge")


logging.error("This is an error testing message!!!")
logging.critical("critical messge !!!")
logging.warning("warning messge !")