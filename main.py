""""Such." declarative JSON-derived language interpreter for Python."""
from classes.Interpreter import Interpreter

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
    fullFile: str = "foo.such"
    reducedFile: str = "bar.such"

    print(f"Reading from {reducedFile}...:")
    print(f"\n=============================\n```such\n{Interpreter.interpret(reducedFile)}\n```")

    # ! Comments, which present themselves in this file, have not been added support yet. Expect errors.
    print(f"Reading from {fullFile}...:")
    print(f"\n=============================\n```such\n{Interpreter.interpret(fullFile)}\n```\n\n")


if __name__ == '__main__':
    main()
