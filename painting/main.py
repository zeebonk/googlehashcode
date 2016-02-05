import argparse
import importlib

from picture import Picture


if __name__ == '__main__':
    # Handle command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="filename for input data")
    parser.add_argument("algorithm", help="filename for algorithm to use")
    parser.add_argument("-i", "--iterations", help="number of iterations needed for algorithm", type=int)
    args = parser.parse_args()

    # Load input data and algorithm
    picture = Picture(args.data)
    module = importlib.import_module('algorithms.' + args.algorithm)

    # Get result from the algorithm
    result = module.algorithm(picture, args)
    
    # TODO: print/submit output file? print/submit score?
    # ...

