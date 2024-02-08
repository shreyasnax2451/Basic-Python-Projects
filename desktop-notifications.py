# from notifypy import Notify
# import time

# notification = Notify()
# notification.title = "Reminder"
# notification.message = "It's been 2 hours since you drank water. Please Drink!"


# while (notification_count := input('Did You Drink Shreyas? ')) != 'Yes':
#     notification.send()
#     time.sleep(5)

import os
import time 

REPEAT_INTERVAL = 5 # Repeat frequency in seconds

while True:
#   command = "osascript -e \'say \"Hey shreyas drink water\"\'; osascript -e \'display alert \"Hey shreyas Drink Water!\"\'"
  command = "osascript -e 'display alert \"Hello Shreyas Drink Water!\" message \"Poyi Nillu Taagu ra unga !\"'"
  os.system(command)
  time.sleep(REPEAT_INTERVAL)