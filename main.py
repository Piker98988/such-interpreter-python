""""Such." declarative JSON-derived language interpreter for Python."""
from utils.Interpreter import Interpreter

def main():
    """
    ? First, let's define how we want our language to look in the "foo.such" file.
    * Extension: .such
    * This language will have headers, which will not have an equals. May these be the keys, of which their level is defined by the double colons:

    * 1. To do something like this, we will need to at least parse a file line by line, so, let's start with that. Reading from a file. Then we'll get with the parsing.
    * 2. Now we have read information from the file, let's divide it into statements
    * 3. Once divided into statements, let's start parsing the statements and associating them.
    * 4. After parsing
    """

    fullFilePath: str = "./data/such/foo.such"
    semiFilePath: str = "./data/such/baz.such"
    reducedFilePath: str = "./data/such/bar.such"

    print(f"Reading from {reducedFilePath}...:")
    print(f"\n=============================\n```such\n{Interpreter.interpret(reducedFilePath)}\n```")

    print(f"Reading from {semiFilePath}...:")
    print(f"\n=============================\n```such\n{Interpreter.interpret(semiFilePath)}\n```")

    # ! Comments and headers, which are present in this file, have not been given support yet. Expect errors.
    print(f"Reading from {fullFilePath}...:")
    print(f"\n=============================\n```such\n{Interpreter.interpret(fullFilePath)}\n```\n\n")


if __name__ == '__main__':
    main()
