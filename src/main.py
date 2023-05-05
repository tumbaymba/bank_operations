from utils import *

FILE_URL = "../json_files/operations.json"


def main():
    operations_list = load_file(FILE_URL)
    operations = make_operations(operations_list)
    print(get_executed_five(operations))


if __name__ == "__main__":
    main()
