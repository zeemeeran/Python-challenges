
cmdprev = ''

while True :
    cmd = input("> ").lower()
    
    if cmd == 'help':
        print('start - to start the car \n stop - to stop the car \n quit - to exit \n')
    elif cmd == 'start' :
        if cmdprev == 'start' :
            print("Car already started\n")
        else :
            print('Car started \n')
        cmdprev = 'start'
        continue
    elif cmd == 'stop' :
        if cmdprev == 'stop' :
            print("car already stopped\n")
        else :
            print('car stopped \n')
        cmdprev = 'stop' 
        continue
    elif cmd == 'quit' :
        print('exiting.. \n')
        break
    else :
        print('I dont get it \n')
        continue


