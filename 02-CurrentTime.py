# Adapted from https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python

from datetime import datetime
#Gets current Timestamp from datetime library and the format it by the format specified in the string
print (datetime.now().strftime('%H:%M:%S %d-%m-%Y'))