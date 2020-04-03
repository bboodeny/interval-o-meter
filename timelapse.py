

def main():
    print("Interval in seconds after which a shot is taken.")
    print("Length of video in seconds produced based on interval, and/or amount of time.")
    print("Amount of time in minutes to take pictures for.")
    print("")
    print("Leave length of vid and/or period of time as 0 if unspecified")
    print("")
    
    tryagain = getinput()
    while (tryagain):
        tryagain = getinput()

def getinput():
    tryagain = False

    interval =0
    vidlen =0
    amttime =0
    fps = 0
    
    interval = eval(input("Enter interval (in s): "))
    vidlen = eval(input("Enter length of video produced (in s): "))
    if vidlen != 0:
        fps = eval(input("Enter fps: "))
    amttime = eval(input("Enter period of time (in mins) to take pictures: "))
    
    tryagain = estimates(interval, vidlen, amttime, fps)
    return tryagain

def estimates(interval, vidlen, amttime, fps):
	
    if interval == 0 and vidlen != 0 and fps != 0 and amttime != 0:
        amtpic = vidlen*fps
        interval = (amttime*60)/amtpic
        print("For a", vidlen, "second timelapse video taken over", amttime, "minutes,", amtpic, "pictures will be taken at", interval, "s intervals")
        #shutterrelease(interval, amtpic)
        tryagain = False
            
    elif interval != 0 and vidlen == 0 and amttime != 0:
        amtpic = round((amttime*60)/interval)
        vidlen = amtpic/60 #for a 60fps video
        print(amtpic, "pictures will be taken over", amttime, "minutes to produce a", vidlen, "second video")
        #shutterrelease(interval, amtpic)
        tryagain = False
        
    elif interval != 0 and vidlen != 0 and fps!=0 and amttime == 0:
        amtpic = fps*vidlen
        amttime = (amtpic*interval)/60
        print(amtpic ,"pictures will be taken to generate a", vidlen, "second video and will take ", amttime, "minutes to complete.")
        #shutterrelease(interval, amtpic)
        tryagain = False
        
    else:
        print("\nInvalid input. Try again!\n")
        return True

    while (not tryagain):
        txt = input("Release shutter? y/n")
        if txt == 'y' or txt == 'Y':
            shutterrelease(interval, amtpic)
            tryagain = True
            return False
        else:
            tryagain = False
        txt = input("Start over? y/n")
        if txt == 'y' or txt == 'Y':
            return True
    
        
def shutterrelease(interval, amtpic):
    for i in range(0,amtpic):
        print("pressed shutter", i+1, "times")
        #wait for interval seconds
    

main()
