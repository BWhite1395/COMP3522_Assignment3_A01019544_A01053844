from facade import PokeDexSearcher
from request import Request
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

Pargs = parser.parse_args()
if not Pargs.inputfile and not Pargs.inputdata:
    print("Must use --inputdata or --inputfile")
    exit()

class Pokedex:

    def create_request(self, args):
        r = Request(args)
        return r


def main():
    print("The mode: " + str(Pargs.mode))
    if Pargs.inputfile:
        print("Inputfile name: " + str(Pargs.inputfile))
    if Pargs.inputdata:
        print("Inputdata: " + str(Pargs.inputdata))
    print(Pargs.expanded)
    if Pargs.output:
        print(Pargs.output)
    else:
        print("No output")

    dex = Pokedex()
    request = dex.create_request(Pargs)
    myPokedex = PokeDexSearcher()
    myPokedex.execute_request(request)

if __name__ == '__main__':
    main()

