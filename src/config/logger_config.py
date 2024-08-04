import logging
import os
from datetime import datetime

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)

current_date = datetime.now().strftime('%Y-%m-%d')
log_filename = os.path.join(log_dir, f'{current_date}.log')


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger(__name__)
