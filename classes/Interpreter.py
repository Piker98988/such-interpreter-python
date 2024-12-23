from typing import Type
import re

from classes.Statements.Definition import Definition
from classes.Statements.Header import Header
from classes.Statements.Statement import Statement
from classes.Types.Array import ARRAY

from classes.Types.Boolean import BOOLEAN
from classes.Types.DataType import DataType
from classes.Types.Integer import INTEGER
from classes.Types.Keymap import KEYMAP
from classes.Types.NullType import NULL
from classes.Types.String import STRING


# FIXME Rewrite according to the new guidelines; It won't work until then
class Interpreter(object):
    @staticmethod
    def interpret(filepath: str) -> None:
        contents = Interpreter._read_file(filepath)
        print(contents)

        nocomments_contents = Interpreter._strip_from_comments(contents)
        print(nocomments_contents)

        nolf_contents = Interpreter._strip_from_line_endings(nocomments_contents)
        print(nolf_contents)

        statements: list[str] = Interpreter._separate_into_statements(nolf_contents)
        print(statements)

        classified_statements: list[Type[Statement]] = Interpreter._classify_statements(statements)
        print([statement.__str__() for statement in classified_statements])


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

    # ? Step 2: Get those nasty \n out
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
    def _classify_statements(statements: list[str]) -> list[Type[Statement], ...]:
        definition_regex_pattern: str = r"""^(?>([A-Z]{3}|NU\?)[ \n]+([\w-]+)[ \n]*=[ \n]*(["'].*["']|\d+|false|true|null|none))$"""
        header_regex_pattern: str = r"""^(VECH|RELH)\{([A-Z]{3}|VECH|RELH(?>\/(?>[A-Z]{3}|NU\?))*)\}[ \n]+([\w-]+(?>::[\w-]+)*)$"""

        classified_statements: list[Type[Statement], ...] = []

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
        types: dict[str, Type[DataType]] = {
            "RELH": KEYMAP,
            "VECH": ARRAY,
        }
        heading_name = match.group(3).split("::")

        new_header = Header(types[match.group(1)], match.group(2).split("/"), heading_name)

        return new_header


    @staticmethod
    def _interpret_definition(match) -> Definition:
        types: dict[str: Type[DataType]] = {
            "BOO": BOOLEAN,
            "INT": INTEGER,
            "STR": STRING,
            "NU?": NULL,
        }
        definition_type: Type[DataType] = types[match.group(1)]
        definition_name = match.group(2)
        definition_value = match.group(3)
        return Definition(definition_type, definition_name, definition_value)