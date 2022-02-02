import sys, getopt
from tracemalloc import start

def get_start_and_end_dates():
    start_date = None
    end_date = None

    # use sys to get passed in args
    # first arg is the name of script
    argv = sys.argv[1:]

    try:
        # get args using getopt.getopt()
        # returns list of tuples
        opts, args = getopt.getopt(argv, "s:e:", ['start_date', 'end_date'])
    # catch errors if args weren't passed in correctly
    except getopt.GetoptError as e:
        print(e)
        opts = []


    for opt, arg in opts:
        if opt in ['-s', 'start_date']:
            start_date = arg
        elif opt in ['-e', 'end_date']:
            end_date = arg

    print(f"start_date: {start_date}")
    print(f"end_date: {end_date}")

get_start_and_end_dates()