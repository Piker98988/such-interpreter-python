from classes import *
import re


class Interpreter(object):
    @staticmethod
    def interpret(filepath: str) -> None:
        contents = Interpreter._read_file(filepath)
        print(contents)

        stripped_contents = Interpreter._strip_from_line_endings(contents)
        print(stripped_contents)

        statements: list[str] = Interpreter._separate_into_statements(stripped_contents)
        print(statements)

        such_statements: list[str] = Interpreter._check_for_such_file(statements)
        print(such_statements)

        classified_statements: list[Definition|Header] = Interpreter._classify_statements(statements)
        print([statement.__str__() for statement in classified_statements])


    # ? Step 1: Read what the file contains
    @staticmethod
    def _read_file(filename: str) -> str:
        info: str = ""
        try:
            with open(filename) as file:
                info = file.read()
        except FileNotFoundError:
            print("File not found")

        return info


    # ? Step 1.5: Get those nasty \n and spaces out
    @staticmethod
    def _strip_from_line_endings(contents: str) -> str:
        return contents.replace("\r", "").replace("\n", "")


    # ? Step 2: Separate each statement into its own and discard blank lines.
    @staticmethod
    def _separate_into_statements(information: str) -> list[str]:
        statements: list[str] = information.strip("\n").split(";")
        for line in statements:
            if line == "":
                del statements[statements.index(line)]

        return statements

    # ? Step 3: Once we have each statement read, check for the presence of the "Such." language identifier.
    @staticmethod
    def _check_for_such_file(statements) -> list[str]:
        if statements[0].__contains__("#! such."):
            pass
        else:
            raise FileNotFoundError("That file is not a such file. Try using the \"Such.\" identifier in the first line: `#! such.`")
        statements[0] = statements[0].removeprefix("#! such.")

        return statements


    # ? Step 4: Identify each statement as a header or declaration.
    @staticmethod
    def _classify_statements(statements: list[str]) -> list[Header|Definition]:
        definition_regex_pattern: str = r"""(?>([A-Z]{3})[ \n]+([\w-]+)[ \n]*=[ \n]*(["'][\w -]*["']|\d+|false|true))"""
        header_regex_pattern: str = r"""KYV\{([A-Z]{3}(?>\/(?>[A-Z]{3}|NU\?))*)\}[ \n]+([\w-]+(?>::[\w-]+)*)"""

        classified_statements: list[Header|Definition] = []
        last_header_level = 0

        for statement in statements:
            # ? Check for a definition match
            match = re.match(definition_regex_pattern, statement)
            if match is not None:
                new_definition = Interpreter._interpret_definition(match)
                classified_statements.append(new_definition)
                continue

            # ? If not, we will check for a header match; else, we will throw a syntax error.
            match = re.match(header_regex_pattern, statement)
            if match is not None:
                new_header, last_header_level = Interpreter._interpret_header(match)
                classified_statements.append(new_header)
                continue

            raise SyntaxError("Could not interpret statement: " + statement)

        return classified_statements



    @staticmethod
    def _interpret_header(match) -> tuple[Header, int]:
        heading_name = match.group(2).split("::")[-1]
        heading_level = match.group(2).split("::").__len__()

        new_header = Header(match.group(1).split("/"), heading_name, [])

        return new_header, heading_level


    @staticmethod
    def _interpret_definition(match) -> Definition:
        definition_type = match.group(1)
        definition_name = match.group(2)
        definition_value = match.group(3)
        return Definition(definition_type, definition_name, definition_value)