import unittest
# noinspection PyUnresolvedReferences
from such_interpreter import Such

READ_REDUCED: str = "./examples/read_examples/bar.such"
READ_SEMI: str = "./examples/read_examples/baz.such"
READ_FULL: str = "./examples/read_examples/foo.such"
READ_FINAL: str = "./examples/read_examples/bas.such"

# JSON files from which to read and test, never to write. Each object is child of root and has about 10 properties with
# different types each property.
JSON_REDUCED: str = "./examples/write_examples/json/reduced.json" # 5 objects
JSON_SEMI: str = "./examples/write_examples/json/semi_reduced.json" # 50 objects
JSON_FULL: str = "./examples/write_examples/json/full.json" # 500 objects
JSON_FINAL: str = "./examples/write_examples/json/full_final.json" # 50 000 objects

OUTPUT_REDUCED: str = "./examples/write_examples/such/reduced.such"
OUTPUT_SEMI: str = "./examples/write_examples/such/semi.such"
OUTPUT_FULL: str = "./examples/write_examples/such/full.such"
OUTPUT_FINAL: str = "./examples/write_examples/such/final.such"


class TestMainClass(unittest.TestCase):
    def test_reduced_file_case(self):
        print("\ntest_reduced_file_case")
        contents = Such.from_file(READ_REDUCED)
        print(contents)

    def test_semi_reduced_file_case(self):
        print("\ntest_semi_reduced_file_case")
        contents = Such.from_file(READ_SEMI)
        print(contents)

    def test_full_file_case(self):
        print("\ntest_full_file_case")
        contents = Such.from_file(READ_FULL)
        print(contents)

    def test_final_file_case(self):
        print("\ntest_final_file_case")
        contents = Such.from_file(READ_FINAL)
        print(contents)

    def test_reduced_string_case(self):
        print("\ntest_reduced_string_case")
        with open(READ_REDUCED, "r") as f:
            contents = f.read()
            such = Such.from_string(contents)
        print(such)

    def test_semi_reduced_string_case(self):
        print("\ntest_semi_reduced_string_case")
        with open(READ_SEMI, "r") as f:
            contents = f.read()
            such = Such.from_string(contents)
        print(such)

    def test_full_string_case(self):
        print("\ntest_full_string_case")
        with open(READ_FULL, "r") as f:
            contents = f.read()
            such = Such.from_string(contents)
        print(such)

    def test_full_final_string_case(self):
        print("\ntest_final_string_case")
        with open(READ_FINAL, "r") as f:
            contents = f.read()
            such = Such.from_string(contents)
        print(such)

    def test_reduced_to_file(self):
        print("\ntest_reduced_to_file")
        such_info = Such.from_file(READ_REDUCED)
        Such.to_file(such_info, OUTPUT_REDUCED)

    def test_semi_reduced_to_file(self):
        print("\ntest_semi_reduced_to_file")
        such_info = Such.from_file(READ_SEMI)
        Such.to_file(such_info, OUTPUT_SEMI)

    def test_full_to_file(self):
        print("\ntest_full_to_file")
        such_info = Such.from_file(READ_FULL)
        Such.to_file(such_info, OUTPUT_FULL)

    def test_full_final_to_file(self):
        print("\ntest_full_final_to_file")
        such_info = Such.from_file(READ_FINAL)
        Such.to_file(such_info, OUTPUT_FINAL)

    def test_reduced_from_json(self):
        print("\ntest_reduced_from_json")
        Such.from_json(JSON_REDUCED, OUTPUT_REDUCED)

    def test_semi_reduced_from_json(self):
        print("\ntest_semi_reduced_from_json")
        Such.from_json(JSON_SEMI, OUTPUT_SEMI)

    def test_full_from_json(self):
        """I expect this one to translate in the reasonable amount of 30 seconds"""
        print("\ntest_full_from_json")
        Such.from_json(JSON_FULL, OUTPUT_FULL)

    def test_final_from_json(self):
        """The ultimate test, read 50 000 json objects, translate them, and then dump to a file. I do not expect this test to be completed"""
        print("\ntest_final_from_json")
        Such.from_json(JSON_FINAL, OUTPUT_FINAL)
