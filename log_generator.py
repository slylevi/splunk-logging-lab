import time
import random
from datetime import datetime

log_levels = ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']
messages = [
	'User login successful',
	'User logout successful',
	'File uploaded',
	'Database connection failed',
	'Permission denied',
	'Unexpected error occurred',
	'Service restarted',
	'Memory usage high'
]

log_file = 'app.log'

while True:
	with open(log_file, 'a') as f:
		log_entry = f"{datetime.now().isoformat()} - {random.choice(log_levels)} - {random.choice(messages)}\n"
		f.write(log_entry)
	time.sleep(2) #Adjust to generate logs faster/slower
	
