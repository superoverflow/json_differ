#!/usr/bin/python3
import logging
import argparse
import json
import os

def read_json_from_file(file):
    
    with open(file) as f:
        lines = f.readlines()
        js_out = json.loads("".join(lines))
    
    return js_out

def compare_json(json1, json2):
    keys1 = json1.keys()
    keys2 = json2.keys()
    
    logging.debug("looking for common keys between keys1 and keys2")
    logging.debug("looking for extra keys: keys1")
    logging.debug("looking for extra keys: keys2")    
    return True
    
def compare_two_list(list1, list2):
    pass
    

if __name__ == '__main__':
    LOGFMT = ("%(asctime)-15s [%(levelname)-5s] %(filename)-10s:%(lineno)-3d "
              "%(message)s")
    logging.basicConfig(level=logging.DEBUG, format=LOGFMT)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--left", required=False,
        help="Left Hand Side File", default = "data/json01a")
    parser.add_argument("-r", "--right", required=False,
        help="Right Hand Side File", default = "data/json01b")
    
    args = parser.parse_args()
    left = args.left
    right = args.right
    
    logging.info("start comparing files [%(left)s] vs [%(right)s]"  
        % {'left': left, 'right' : right} )
        
    json_left = read_json_from_file(left) 
    json_right = read_json_from_file(right)
    compare_json(json_left, json_right)