import os 
import logging 
import sys

logging_str="[%(asctime)s:%(levelname)s :%(module)s : %(message)s:]"
log-dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exit_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreaHandler(sys.stdout)
    ]
)

logger = loggong.getlogger("textSummarizerLogger")