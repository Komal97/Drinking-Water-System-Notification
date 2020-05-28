import time
from plyer import notification

if __name__ == '__main__':

    # run continously and show window notification after every one hour
    while(True):
        notification.notify(
            title = 'Please drink water now',
            message = 'Drinking Water Helps Maintain the Balance of Body Fluids.\
                    Your body is composed of about 60% water. The functions of these bodily fluids\
                    include digestion, absorption, circulation and maintenance of body temperature.',
            app_icon = None,
            timeout = 10
        )
      # sleep for one hour and again window notification shows up
        time.sleep(60*60) 

# to run this scheduler in background, use command 'pythonw.exe main.py'