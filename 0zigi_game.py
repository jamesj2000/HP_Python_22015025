import time

import sys

def ziggigame(str):

    count = 0

    while True:

        try:

            print(" " * count + str)

            time.sleep(0.1)

            count += 1

            if count == 20:

                while count > 0:

                    print(" " * count + str)

                    time.sleep(0.5)

                    count -= 1

        except KeyboardInterrupt:

            sys.exit()

ziggigame("**********")
