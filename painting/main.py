import argparse
import importlib

from picture import Picture


if __name__ == '__main__':
    # Handle command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="filename for input data")
    parser.add_argument("algorithm", help="filename for algorithm to use")
    parser.add_argument("-i", "--iterations", help="number of iterations needed for algorithm", type=int)
    parser.add_argument("-d", "--debug", dest='debug', action='store_true')
    args = parser.parse_args()

    # Load input data and algorithm
    picture = Picture.from_file(args.data)
    module = importlib.import_module('algorithms.' + args.algorithm)

    # Get result from the algorithm
    painter = module.algorithm(picture, args)

    if args.debug:
        # Output images and other details
        print(picture)
        print(painter.picture)
        print(len(painter.commands))
        if (picture != painter.picture).any():
            raise Exception("Result image different from target image")
    else:
        # Output commands
        print(painter.get_output())
