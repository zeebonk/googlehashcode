import argparse
import importlib

from simulator import Simulator


if __name__ == '__main__':
    # Handle command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="filename for input data")
    parser.add_argument("algorithm", help="filename for algorithm to use")
    parser.add_argument("-i", "--iterations", help="number of iterations needed for algorithm", type=int)
    parser.add_argument("-d", "--debug", dest='debug', action='store_true')
    args = parser.parse_args()

    # Load input data and algorithm
    module = importlib.import_module('algorithms.' + args.algorithm)
    simulator = Simulator(args.data, module.algorithm)

    # Get result from the algorithm
    result = simulator.simulate(args)

    if args.debug:
        # Output all debug information
        print(simulator)
        print(result)
        if foo != result:
            raise Exception("Result image different from target image")
    else:
        # Output
        print(result)
