#! /usr/bin/python

import argparse, sys
from planet import MassStore, Planet

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the weight of a mass on a stream of planets.')

    parser.add_argument('-i', '--input', action='store', default=None, dest='input', help='Input file to use.  If not provided, uses stdin.')
    parser.add_argument('-o', '--output', action='store', default=None, dest='output', help='Output file to use.  If not provided, uses stdin.')

    args = parser.parse_args()

    with (open(args.input) if args.input is not None else sys.stdin) as infile:
        with (open(args.output, 'w') if args.output is not None else sys.stdout) as outfile:
            mass = MassStore.parse(infile)
            for planet in mass.planets:
                outfile.write("{0}: {1:.3f}\n".format(planet.name, planet.calculate_object_weight(mass.mass, planet.radius)))
