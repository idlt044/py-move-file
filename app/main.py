import os


def move_file(command: str) -> None:
    list_command = command.split()

    if (
        len(list_command) != 3
        or list_command[0] != "mv"
        or list_command[1] == list_command[2]
    ):
        return

    source = list_command[1]
    destination = list_command[2]

    if destination.endswith("/"):
        filename = os.path.basename(source)
        destination = os.path.join(destination, filename)

    directory = os.path.dirname(destination)

    if directory != "":
        os.makedirs(directory, exist_ok=True)

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
