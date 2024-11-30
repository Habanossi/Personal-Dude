import time

def main():
    seconds_from_start = 0
    while(True):
        print("(" + str(seconds_from_start) + ") " + "Waiting for commands...")
        seconds_from_start += 1
        time.sleep(1)

main()

