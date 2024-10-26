import subprocess
import os
import glob
import argparse

def create_all(count):
    file_list = glob.glob("bin/*.py")
    for file_name in file_list:
        subprocess.run(["python", file_name, str(count)])

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description="Script to generater random address in all us states at once times")
    parser.add_argument("-c", type=int, help="Number of addresses to generate for each state")
    args = parser.parse_args()

    if args.c:
        create_all(args.c)
    else:
        parser.print_help()