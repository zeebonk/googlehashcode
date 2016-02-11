from simulator import Simulator


def algorithm(simulator, args):
    for drone in simulator.free_drones[:]:
    	simulator.wait(drone, 1000)
