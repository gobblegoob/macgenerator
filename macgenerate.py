'''
    Mac Address Generator

    Will output a list of randomized mac addresses per RFC 7042.

    This is used to simulate endpoints, endpoint purge policy testing in ISE, or whatever
'''
import random
import argparse
from colorama import Fore,Style

def mac_add_generate(is_random=False, delimiter=""):
    '''
    Generates a standard MAC address - completely random
    :arg: boolean Will create randomized mac addresses if True
    '''
    i = 0
    mac = ""
    if is_random == False:
        # Generate a non-randomized mac address
        while i < 12:
            n = random.randrange(15)
            n = hex(n)
            n = str(n[2:])
            mac = mac + n
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
                mac = mac + delimiter
            i+=1
    
    else:
        # Generate a randomized mac address
        while i < 12:
            n = random.randrange(15)
            n = hex(n)
            n = str(n[2:])
            mac = mac + n
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
                mac = mac + delimiter
            i += 1
        mac = make_randomized(mac)

    return mac


def make_randomized(mac):
    '''
    Will format a mac address as randomized
    '''
    rando_char = ["2", "6", "a", "e"]
    rando_index = random.randrange(3)
    
    mac_list = []
    rando_mac = ""
    for i in mac:
        mac_list.append(i)

    mac_list[1] = rando_char[rando_index]
    for i in mac_list:
        rando_mac = rando_mac + i
    return rando_mac


def validate_delimeter(delimiter):
    '''
    Is this an acceptable delimiter?  
    :arg: str
    :return: boolean
    '''
    if delimiter == ":" or delimiter == "-":
        return True
    else:
        return False


if __name__ == "__main__":

    # List of mac addresses
    mac_list = []

    parser = argparse.ArgumentParser(
        prog= "Mac Address Generator",
        description= "Generates MAC addresses with specified parameters, including randomized MACs."
    )

    parser.add_argument("-c", "--count", type=int, help="How many MAC addresses to generate. Will print 10 if not specified")
    parser.add_argument("-d", "--delimiter", type=str, help="MAC Address delimiter.  Will use None if not specified.  Supported delimiters: \":\", \"-\"", required=False)
    parser.add_argument("-r", "--randomized", action="store_true", help="Add if you want randomized IP addresses", required=False)

    args = parser.parse_args()

    
    if args.delimiter is not None:
        if validate_delimeter(args.delimiter) is True:
            delimiter = args.delimiter
        else: 
            print(f"{Fore.LIGHTRED_EX}{args.delimiter} is an invalid delimiter.  Supported delimiters are \":\" or \"-\"{Style.RESET_ALL}")
            #delimiter = ""
            quit()
    else:
        delimiter = ""

    randomized = False
    if args.randomized is True:
        randomized = True
    
    if args.count is not None:
        i = 0
        count = int(args.count)
        while i < count:
            mac_list.append(mac_add_generate(randomized, delimiter))
            i += 1


    if args.count is None:
        i = 0
        while i < 10:
            mac_list.append(mac_add_generate(randomized, delimiter))
            i += 1


    for i in mac_list:
        print(i)
    if randomized == True:
        print(f"{Fore.LIGHTGREEN_EX}Generated {args.count} randomized mac addresses{Style.RESET_ALL}")
    else:
        print(f"{Fore.LIGHTGREEN_EX}Generated {args.count} mac addresses{Style.RESET_ALL}")
