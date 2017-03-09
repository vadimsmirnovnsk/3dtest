#!/usr/bin/env python
import os
import logging
import argparse

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

def main():
    parser = create_parser()
    args = parser.parse_args()
    logging.info("I'm not a mothafucka pidor!")
    logging.info("Passed arguments: {}".format(args))

def create_parser():
    parser = argparse.ArgumentParser(description="Generating v4iOS module..")
    parser.add_argument("--echo", "-e",
        help="Echo param",
        default="")
    return parser

if __name__ == "__main__":
    main()
