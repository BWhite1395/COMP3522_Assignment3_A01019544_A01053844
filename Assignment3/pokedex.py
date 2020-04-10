import argparse
parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["pokemon","ability","move"]
                    , help="The mode of the program[Pokemon/Ability/Move]")

io = parser.add_mutually_exclusive_group()
io.add_argument("--inputfile", help="The name of the inputfile.txt")
io.add_argument("--inputdata", help="Name or id of the specified mode")

parser.add_argument("--expanded", action="store_true",
                    help="Optional mode to expand output")
parser.add_argument("--output", help="Optional file.txt to write output")

args = parser.parse_args()
if args.mode != "pokemon" and args.mode != "move" and args.mode != "ability":
    raise TypeError


class Pokedex:
    pass


def main():
    print("The mode: " + str(args.mode))
    if args.inputfile:
        print("Inputfile name: " + str(args.inputfile))
    if args.inputdata:
        print("Inputdata: " + str(args.inputdata))
    print(args.expanded)
    if args.output:
        print(args.output)
    else:
        print("No output")


if __name__ == '__main__':
    main()
