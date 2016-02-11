import argparse
import importlib

from foo import Foo


if __name__ == '__main__':
    # Handle command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="filename for input data")
    parser.add_argument("algorithm", help="filename for algorithm to use")
    parser.add_argument("-i", "--iterations", help="number of iterations needed for algorithm", type=int)
    parser.add_argument("-d", "--debug", dest='debug', action='store_true')
    args = parser.parse_args()

    # Load input data and algorithm
    foo = Foo(args.data)
    module = importlib.import_module('algorithms.' + args.algorithm)

    # Get result from the algorithm
    result = module.algorithm(foo, args)

    if args.debug:
        # Output images and other details
        print(foo)
        print(result)
        if (foo != result).any():
            raise Exception("Result image different from target image")
    else:
        # Output commands
        print(result)
