'''
    Mac Address Generator

    Will output a list of randomized mac addresses per RFC 7042.

    This is used to simulate endpoints, endpoint purge policy testing in ISE, or whatever
'''
import random
import argparse
from colorama import Fore,Style

import random
import argparse
from colorama import Fore, Style

def mac_add_generate(is_random=False, delimiter=""):
    mac = ""
    for i in range(12):
        n = random.randrange(16)
        mac += f"{n:01x}"  # Convert to hexadecimal and append to MAC
        if i % 2 == 1 and i < 11:  # Add delimiter after every two hex digits, except the last
            mac += delimiter
    if is_random:
        mac = make_randomized(mac)
    return mac

def make_randomized(mac):
    rando_char = ["2", "6", "a", "e"]
    rando_index = random.randrange(4)
    mac_list = list(mac)
    mac_list[1] = rando_char[rando_index]
    return ''.join(mac_list)

def validate_delimiter(delimiter):
    return delimiter in [":", "-"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Mac Address Generator",
        description="Generates MAC addresses with specified parameters, including randomized MACs."
    )

    parser.add_argument("-c", "--count", type=int, default=10, help="How many MAC addresses to generate.")
    parser.add_argument("-d", "--delimiter", type=str, help="MAC Address delimiter. Supported delimiters: ':', '-'", required=False)
    parser.add_argument("-r", "--randomized", action="store_true", help="Add if you want randomized MAC addresses")

    args = parser.parse_args()

    if args.delimiter and not validate_delimiter(args.delimiter):
        print(f"{Fore.LIGHTRED_EX}{args.delimiter} is an invalid delimiter. Supported delimiters are ':' or '-'{Style.RESET_ALL}")
        quit()

    delimiter = args.delimiter or ""
    mac_list = [mac_add_generate(args.randomized, delimiter) for _ in range(args.count)]

    for mac in mac_list:
        print(mac)

    mac_type = "randomized" if args.randomized else ""
    print(f"{Fore.LIGHTGREEN_EX}Generated {args.count} {mac_type} mac addresses{Style.RESET_ALL}")
