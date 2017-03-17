#!/usr/bin/python3
import logging
import argparse
import os


if __name__ == '__main__':
    LOGFMT = ("%(asctime)-15s [%(levelname)-5s] %(filename)-10s:%(lineno)-5d "
              "%(message)s")
    logging.basicConfig(level=logging.INFO, format=LOGFMT)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--left", required=False,
        help="Left Hand Side File", default = "data/json01a")
    parser.add_argument("-r", "--right", required=False,
        help="Right Hand Side File", default = "data/json01b")
    
    logging.info("start")
