import sys
from tubes.functional_start import TFL

TUBES = [tube for tube in sys.argv[1:]]

if __name__ == "__main__":
    TFL(TUBES).print_status()
    #print(TUBES)