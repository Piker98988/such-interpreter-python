import re

from utils.constants import *

from utils.Statements.Definition import Definition
from utils.Statements.Header import Header
from utils.Statements.Statement import Statement

from utils.Types.DataType import DataType



class Interpreter(object):
    @staticmethod
    def interpret(filepath: str) -> None:
        print("="*20 + " CONTENTS " + "="*20)
        contents = Interpreter._read_file(filepath)
        print(contents)
        print()

        print("="*20 + " COMMENTS STRIPPED " + "="*20)
        nocomments_contents = Interpreter._strip_from_comments(contents)
        print(nocomments_contents)
        print()

        print("="*20 + " NO LINE FEED AND CARET RETURN " + "="*20)
        nolf_contents = Interpreter._strip_from_line_endings(nocomments_contents)
        print(nolf_contents)
        print()

        print("="*20 + " STATEMENTS " + "="*20)
        statements: list[str] = Interpreter._separate_into_statements(nolf_contents)
        print(statements)
        print()

        print("="*20 + " PARSED STATEMENTS " + "="*20)
        classified_statements: list[Statement] = Interpreter._classify_statements(statements)
        print(classified_statements)
        print()

        print("="*20 + " PRETTY PRINTED PARSED STATEMENTS " + "="*20)
        print([statement.__repr__() for statement in classified_statements])
        print()

        print("="*20 + " ORGANISED STATEMENTS " + "="*20)
        organised_statements: list[Statement] = Interpreter._organise_statements(classified_statements)
        print(organised_statements)
        print("="*50)



    # ? Step 1: Read the .such file and get the contents
    @staticmethod
    def _read_file(filename: str) -> str:
        info: str = ""
        try:
            with open(filename) as file:
                info = file.read()
        except FileNotFoundError:
            print("File not found")

        return info


    # ? Step 1.5: Detect comments before separating into statements, so they do not mess up parsing.
    @staticmethod
    def _strip_from_comments(contents: str) -> str:
        multi_line_comment_pattern = r""" *<!--[\s\S]*?--> *"""
        single_line_comment_pattern = r""" *\/\/ *[\s\S]*?\n"""

        # ? Replace the occurrences of the patterns with empty strings
        no_ml_comments = re.sub(multi_line_comment_pattern, "", contents)
        no_sl_ml_comments = re.sub(single_line_comment_pattern, "", no_ml_comments)

        return no_sl_ml_comments


    # ? Step 2: Get those nasty caret return and line feed characters out
    @staticmethod
    def _strip_from_line_endings(contents: str) -> str:
        return contents.replace("\r", "").replace("\n", "")


    # ? Step 3: Separate each statement into its own and discard blank lines.
    @staticmethod
    def _separate_into_statements(information: str) -> list[str]:
        statements: list[str] = information.strip("\n").split(";")
        for line in statements:
            if line == "":
                del statements[statements.index(line)]

        return statements


    # ? Step 4: Identify each statement as a header or declaration.
    @staticmethod
    def _classify_statements(statements: list[str]) -> list[Statement]:
        definition_regex_pattern: str = r"""^(?>([A-Z]{3}|NU\?)[ \n]+([\w-]+)[ \n]*=[ \n]*(["'].*["']|\d+|false|true|null|none))$"""
        header_regex_pattern: str = r"""^(VECH|RELH)\{([A-Z]{3,4}(?>\/(?>[A-Z]{3}|NU\?))*)\}[ \n]+([\w-]+(?>::[\w-]+)*)$"""

        root: list[Statement|list] = []

        for statement in statements:
            # ? Check for a definition match
            match = re.match(definition_regex_pattern, statement)
            if match is not None:
                new_definition = Interpreter._interpret_definition(match)
                root.append(new_definition)
                continue

            # ? If not, we will check for a header match; else, we will throw a syntax error.
            match = re.match(header_regex_pattern, statement)
            if match is not None:
                new_header = Interpreter._interpret_header(match)
                root.append(new_header)
                continue
            raise SyntaxError("Could not interpret statement: " + statement)
        return root

    @staticmethod
    def _interpret_header(match) -> Header:
        try:
            subtypes = tuple([ttypes[a] for a in match.group(2).split("/")])
        except KeyError as e:
            if match.group(2) != "VECH" and match.group(2) != "RELH":
                raise SyntaxError(f"Invalid subtype for header: {e}")
            subtypes = [htypes[match.group(2)]]

        new_header = Header(htypes[match.group(1)], subtypes, match.group(3))
        return new_header

    @staticmethod
    def _interpret_definition(match) -> Definition:
        definition_type: Type[DataType] = ttypes[match.group(1)]
        definition_name = match.group(2)
        definition_value = match.group(3)
        return Definition(definition_type, definition_name, definition_value)

    # ? Step 5; Nest statements accordingly
    @staticmethod
    def _organise_statements(parsed_statements: list[Statement]) -> list[Statement]:

        return []
