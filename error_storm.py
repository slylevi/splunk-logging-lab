import time
from datetime import datetime

log_file = 'app.log'

error_message = 'Database connection failed - simulated outage'

for i in range(30): # 30 rapid entries
	with open(log_file, 'a') as f:
		log_entry = f"{datetime.now().isoformat()} - ERROR - {error_message}\n"
		f.write(log_entry)
	time.sleep(0.5) # Adjuest to simulae faster or slower flood
