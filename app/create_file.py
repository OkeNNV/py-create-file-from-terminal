import argparse
import datetime
import os


def create_file() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-d", nargs="+")
    argument_parser.add_argument("-f")
    parsed_args = argument_parser.parse_args()

    if parsed_args.d:
        os.makedirs(os.path.join(*parsed_args.d), exist_ok=True)

    if parsed_args.f:
        target_file_path = parsed_args.f
        if parsed_args.d:
            target_file_path = os.path.join(*parsed_args.d, target_file_path)
        write_lines(target_file_path)


def write_lines(file_path_to_write: str) -> None:
    line_counter = 0
    formatted_lines = []

    with open(file_path_to_write, "a") as destination_file:
        if destination_file.tell() > 0:
            destination_file.write("\n")

        destination_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )

        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            line_counter += 1
            formatted_lines.append(f"{line_counter} {user_input}\n")

        destination_file.writelines(formatted_lines)


create_file()