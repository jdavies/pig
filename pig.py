import argparse
import string, random
from svg import svg

print("*********************************************")
print("*                                           *")
print("*             Python ID Generator           *")
print("*                      by                   *")
print("*                 Jeff Davies               *")
print("*                                           *")
print("* Example:                                  *")
print("*  python pig.py -m UC -n 10 -o output.svg  *")
print("*********************************************")

def generate(total, mfg_id, output, title):
    if title != None:
        print("Generating " + title)
        
    if output != None:
        print("output = " + output + " at the start")
        if output.endswith(".svg"):
            svg_file = svg(output)
        else:
            output = output + ".svg"
            svg_file = svg(output)
        print("output = " + output + " at the end")

    for x in range(total):
        id = ''.join(random.SystemRandom().choice(string.digits) for _ in range(6))
        lot = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(3))
        trailer = ''.join(random.SystemRandom().choice(string.digits) for _ in range(2))
        containerID = "%s-%s-%s-%s" %(mfg_id, id, lot, trailer)
        print("%s-%s-%s-%s" %(mfg_id, id, lot, trailer))
        #print("Container ID = " + containerID)
        if output != None:
            svg_file.createPage(x, containerID, title)

    if output != None:
        svg_file.close()

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

parser.add_argument("-t","--title", 
    help="The title of the decal Default is T_Decal", 
    default="T_Decal",
    type=str)

parser.add_argument("-o","--output", 
    help="The name of the svg file to create", 
    type=str)

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
    generate(args.num, args.mfg, args.output, args.title)
else:
    # Error message
    print("No usable args given. Exiting.")
