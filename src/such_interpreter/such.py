import re
import sys
from types import NoneType

import json

from typing import Type, final

from .utils.Functions.set_to_tuple_with_priorities import ordered_set_to_tuple
from .utils.Types.Array import ARRAY
from .utils.Types.Keymap import KEYMAP

from .utils.Constants.constants import ttypes, htypes, py_htypes, py_ttypes

from .utils.Statements.Header import Header
from .utils.Statements.Definition import Definition
from .utils.Statements.Statement import Statement

from .utils.Types.DataType import DataType

@final
class Such(object):
    """
    **Such.** Json-like language to store data in a type-safe way with semicolons at the end of lines.
    Main class which houses the static methods callable to get the information from the such declaration syntax.
    """
    @staticmethod
    def from_file(filepath: str) -> str | dict:
        """
        Read the contents from a .such file and return

        :param filepath: the path to the .such file from which to read the contents and parse them.
        :return contents: the contents of the file in a python dictionary.
        """
        contents = Such._read_file(filepath)
        #logger.debug(f"===== file =======\n{contents}\n\n")

        nocomments_contents = Such._strip_from_comments(contents)
        #logger.debug(f"===== stripped contents =======\n{nocomments_contents}\n\n")

        nolf_contents = Such._strip_from_line_endings(nocomments_contents)
        #logger.debug(f"===== no line feed =======\n{nolf_contents}\n\n")

        statements: list[str] = Such._separate_into_statements(nolf_contents)
        #logger.debug(f"===== statements as strs =======\n{statements}\n\n")

        classified_statements: list[Statement] = Such._classify_statements(statements)
        #logger.debug(f"===== statements as objs =======\n{classified_statements}\n")
        #logger.debug(f"===== pretty printed as objs =======\n{[statement.__str__() for statement in classified_statements]}\n\n")

        organised_statements: list[Statement] = Such._organise_statements(classified_statements)
        #logger.debug(f"===== organised in tree =======\n{organised_statements}\n")
        #logger.debug(f"===== pretty printed tree =======\n{[statement.__str__() for statement in organised_statements]}\n\n")


        python_translated: dict = Such._translate_to_python(organised_statements)
        #logger.debug(f"===== python translated =======\n{python_translated}\n\n")

        return python_translated

    @staticmethod
    def from_string(string: str) -> str|dict:
        contents = string
        #logger.debug(f"===== string =======\n{contents}\n\n")

        nocomments_contents = Such._strip_from_comments(contents)
        #logger.debug(f"===== stripped contents =======\n{nocomments_contents}\n\n")

        nolf_contents = Such._strip_from_line_endings(nocomments_contents)
        #logger.debug(f"===== no line feed =======\n{nolf_contents}\n\n")

        statements: list[str] = Such._separate_into_statements(nolf_contents)
        #logger.debug(f"===== statements as strs =======\n{statements}\n\n")

        classified_statements: list[Statement] = Such._classify_statements(statements)
        #logger.debug(f"===== statements as objs =======\n{classified_statements}\n")
        #logger.debug(f"===== pretty printed as objs =======\n{[statement.__str__() for statement in classified_statements]}\n\n")

        organised_statements: list[Statement] = Such._organise_statements(classified_statements)
        #logger.debug(f"===== organised in tree =======\n{organised_statements}\n")
        #logger.debug(f"===== pretty printed tree =======\n{[statement.__str__() for statement in organised_statements]}\n\n")


        python_translated: dict = Such._translate_to_python(organised_statements)
        #logger.debug(f"===== python translated =======\n{python_translated}\n\n")

        return python_translated

    @staticmethod
    def from_json(json_file: str, output_file: str, indent: int=3):
        """Creates a copy of any JSON file translated to Such. Take in account many JSON features are not yet supported."""
        if not json_file.endswith(".json"):
            raise FileNotFoundError("That is not a json file!")
        if not output_file.endswith(".such"):
            raise FileNotFoundError("That is not a such file!")

        with open(json_file, "r") as f:
            json_data = json.load(f)
        with open(output_file, "w") as f:
            f.write(Such._from_python_to_such(json_data, indent))

    @staticmethod
    def to_file(data: dict, file: str, indent: int=0):
        """From a dictionary to a Such. file"""
        datas = Such._from_python_to_such(data, indent)
        with open(file, "w") as f:
            f.write(datas)

    @staticmethod
    def to_string(data: dict) -> str:
        """From dict data to a string with Such. format."""
        return Such._from_python_to_such(data)

    @staticmethod
    def _from_python_to_such(data: dict, indent:int=0, _parent_stack=None) -> str:
        """Take any dictionary and translate it into Such. Expect bugs"""
        if _parent_stack is None:
            _parent_stack = []
        if isinstance(data, dict):
            result = ""
            for key, value in data.items():
                if isinstance(value, dict):
                    value: dict
                    subtypes = set()
                    for child in value.values():
                        try:
                            subtypes.add(py_ttypes[type(child)].__repr__())
                        except KeyError:
                            subtypes.add(py_htypes[type(child)].__repr__())

                    formatted_subtypes = "{" + "/".join(ordered_set_to_tuple(subtypes, ["RELH"])) + "}"

                    _parent_stack.append(key)
                    result += f"RELH{formatted_subtypes.replace("'", "").replace("[", "").replace("]", "")} {"::".join(_parent_stack)};\n"
                    result = " " * indent + result
                    result += Such._from_python_to_such(value, indent + 3, _parent_stack)
                    _parent_stack.pop()
                    result += "\n"
                else:
                    if isinstance(value, bool):
                        result += " " * indent + f"BOO {key} = {str(value).lower()};\n"
                    elif isinstance(value, int):
                        result += " " * indent + f"INT {key} = {value};\n"
                    elif isinstance(value, str):
                        result += " " * indent + f"STR {key} = \"{value.replace("\n", "\\n").replace("\t", "\\t")}\";\n"
                    elif isinstance(value, NoneType):
                        result += " " * indent + f"NU? {key} = none;\n"
                    else:
                        raise SyntaxError("Arrays are not supported. (yet)")
            result += " "
            return result
        elif isinstance(data, list):
            raise SyntaxError("Root object cannot be a vector, try using a keymap instead.")


    @staticmethod
    def _to_file(data: list[str], file: str):
        if not file.endswith(".such"):
            raise FileNotFoundError("Write only to .such files. Try passing in a file with the .such extension.")

        with open(file, "w") as f:
            f.write("\n// Data dumped from Such.to_file()\n")
            for statement in data:
                f.write(f"{statement}\n")

    @staticmethod
    def _to_str(data: list[str]):
        pass

    @staticmethod
    def _read_file(filename: str) -> str:
        info: str = ""
        try:
            with open(filename, "r") as file:
                info = file.read()
        except FileNotFoundError:
            print("File not found")
        return info

    @staticmethod
    def _strip_from_comments(contents: str) -> str:
        multi_line_comment_pattern = r""" *<!--[\s\S]*?--> *"""
        single_line_comment_pattern = r""" *\/\/ *[\s\S]*?\n"""

        # ? Replace the occurrences of the patterns with empty strings
        no_ml_comments = re.sub(multi_line_comment_pattern, "", contents)
        no_sl_ml_comments = re.sub(single_line_comment_pattern, "", no_ml_comments)

        return no_sl_ml_comments

    @staticmethod
    def _strip_from_line_endings(contents: str) -> str:
        return contents.replace("\r", "").replace("\n", "")

    @staticmethod
    def _separate_into_statements(information: str) -> list[str]:
        statements: list[str] = information.strip("\n").split(";")
        root = []
        for line in statements:
            if line == "":
                continue
            line = line.strip("\t").strip()
            root.append(line)

        return root

    @staticmethod
    def _classify_statements(statements: list[str]) -> list[Statement|Header]:
        definition_regex_pattern: str = r"""^(?>([A-Z]{3}|NU\?)[ \n]+([\w-]+)[ \n]*=[ \n]*(["'].*["']|\d+|false|true|null|none))$"""
        header_regex_pattern: str = r"""^(VECH|RELH)\{([A-Z\?]{3,4}(?>\/(?>[A-Z]{3}|NU\?))*)\}[ \n]+([\w-]+(?>::[\w-]+)*)$"""

        root: list[Statement|Header] = []

        for statement in statements:
            # ? Check for a definition match
            match = re.match(definition_regex_pattern, statement)
            if match is not None:
                new_definition = Such._interpret_definition(match)
                root.append(new_definition)
                continue

            # ? If not, we will check for a header match; else, we will throw a syntax error.
            match = re.match(header_regex_pattern, statement)
            if match is not None:
                new_header = Such._interpret_header(match)
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

    @staticmethod
    def _organise_statements(parsed_statements: list[Statement]) -> list[Statement]:
        """
        Take the already parsed statements and organize them into the tree-like structure that characterizes JSON-like languages.

        :param parsed_statements: List of statements already parsed to organize
        :return:
        :rtype list[Statement]:
        """
        index = 0 # Keep track of where we are in the statements
        total_statements = len(parsed_statements) # Keep track of the number of statements in the file

        stack: list[Header] = []    # The stack in which we will be popping and pushing the headers for nesting
        root: list[Statement] = []  # The main returning JSON-like object

        for statement in parsed_statements:
            if type(statement) == Header:
                statement: Header
                if len(stack) == 0:             # * Stack is empty
                    new_header = statement      # Create reference
                    stack.append(new_header)    # ? Push reference to stack
                    root.append(statement)      # ? Push object to root
                    index += 1                  # Keep track of statements parsed
                    continue
                # stack is not empty
                if statement.nesting == len(stack):
                    # Header is a child of last header
                    new_header = statement              # Create reference
                    stack[-1].add_child(statement)      # ? PUSH object to last header using the reference in stack
                    stack.append(new_header)            # ? PUSH reference to stack
                    index += 1
                    continue
                elif statement.nesting > len(stack) + 1:
                    raise SyntaxError("Unexpected nesting at statement: " + str(statement) + " with index: " + str(index))
                while len(stack) > statement.nesting:   # * READ Go through stack until we find the parent of new_header
                    stack.pop()                         # ! POP from stack
                new_header = statement                  # Create reference
                try:
                    stack[-1].add_child(statement)      # ? PUSH to parent if parent is not root
                except IndexError:
                    root.append(statement)              # ? PUSH to ROOT if there is no parent header
                stack.append(new_header)                # ? PUSH to stack the reference
                index += 1
                continue
            statement: Definition
            if len(stack) == 0: # A header does not exist
                root.append(statement)
                index += 1
                continue
            stack[-1].add_child(statement)              # ? Push definition to last stack reference
            index += 1

        if index < total_statements:
            print(f"Less statements than expected have been parsed:\n\t- Stack: {stack}\n\t- \
            Statements parsed: {index}\n\t- Statements found: {total_statements}")
        return root

    @staticmethod
    def _translate_to_python(root_obj: list[Statement]) -> dict:
        root: dict = {}
        for obj in root_obj:
            if isinstance(obj.child, ARRAY):
                # If it is an array we will make it completely anonymous, discarding the keys and keeping the values
                asd = list(Such._translate_to_python(obj.child.value).values())

            elif obj.datatype is KEYMAP:
                asd = Such._translate_to_python(obj.child.value)
            else:
                asd = obj.child.value

            root[
                obj.reference if obj.datatype is not ARRAY and obj.datatype is not KEYMAP else obj.real_reference
            ] = asd
        return root
