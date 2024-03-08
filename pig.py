import argparse
import string, random

print("********************************")
print("*                              *")
print("*      Python ID Generator     *")
print("*              by              *")
print("*         Jeff Davies          *")
print("*                              *")
print("* Example:                     *")
print("*  python pig.py -m UC -n 10   *")
print("********************************")

def generate(total, mfg_id):
    for x in range(total):
        id = ''.join(random.SystemRandom().choice(string.digits) for _ in range(6))
        lot = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(3))
        trailer = ''.join(random.SystemRandom().choice(string.digits) for _ in range(2))
        print("%s-%s-%s-%s" %(mfg_id, id, lot, trailer))

    print("Generated", total, "values")

def help_message():
    print("help message here")

# Get arguments
parser = argparse.ArgumentParser("pig")
parser.add_argument("--mfg", "-m",
    help="The manufacturer ID, usually 2 - 3 characters", 
    type=str)

parser.add_argument("-n","--num", 
    help="The number of IDs to generate. Default is 10", 
    type=int)

args = parser.parse_args()

# Ensure all argumants are valid
# if args.mfg == None:
#     print("-mfg is None!")
# else:
#     print("-mfg is", args.mfg)

# if args.num == None:
#     print("-num is None!")
# else:
#     print("-num is", args.num)

if args.num != None and args.mfg != None:
    # Do the work
    generate(args.num, args.mfg)
else:
    # Error message
    print("No usable args given. Exiting.")
