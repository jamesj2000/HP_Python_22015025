import time 

def count_down(time_set):

    try:

        time_set = int(time_set)

        if time_set < 1:

            print("Warning: Time set is less than 1 minute.")

            return

    except:

        print("Error: Only integer data type is allowed as input.")

        return   

    t = time_set * 60

    while t:

        mins, secs = divmod(t, 60)

        timer = '{:02d}:{:02d}'.format(mins, secs)

        print(timer, end="\r")

        time.sleep(1)

        t -= 1

        

        if t == time_set*60*0.2:

            print("Warning: Almost finished line!")

        

    print("Completed!")

    

count_down(input("Enter time in minute ors: "))
