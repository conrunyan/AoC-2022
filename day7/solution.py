def parse_input():
    with open("input.txt") as FH:
        return FH.readlines()


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{str(self.size)} {self.name}"


class Dir:
    def __init__(self, name: str, parent=None):
        self.parent = parent
        self.sub_dirs = {}
        self.files = []
        self.name = name

    def __repr__(self):
        return f"dir {self.name}"

    def add_sub_dir(self, name: str) -> "Dir":
        print(f"Adding '{name}' to {self}")
        self.sub_dirs[name] = Dir(name, self)
        return self.sub_dirs[name]

    def add_file(self, name, size):
        print(f"Adding file '{size} {name}' to {self}")
        self.files.append(File(name, size))

    def get_dir_size(self):
        file_sizes = [f.size for f in self.files]
        dir_sizes = [d.get_dir_size() for d in self.sub_dirs.values()]
        return sum([*file_sizes, *dir_sizes])


class Command:
    def __init__(self, cmd: str):
        self.cmd = cmd
        self.results = []

    def __repr__(self):
        return f"{self.cmd} - {self.results}"

    def add_result(self, line: str):
        self.results.append(line)


class CommandUtils:
    @classmethod
    def parse_commands(self, input_lines: list[str]) -> list[Command]:
        all_cmds = []
        cmd = Command(input_lines[0][2:])
        for line in input_lines[1:]:
            if line.startswith("$"):
                print(f"New command {line} found")
                all_cmds.append(cmd)
                cmd = Command(line[2:])
            else:
                cmd.add_result(line)

        all_cmds.append(cmd)

        return all_cmds


class Terminal:
    def __init__(self):
        self.root = Dir("/")
        self.cur_dir = self.root

    def cd(self, name: str):
        print(f"Moving from {self.cur_dir} to {name}")
        self.cur_dir = self.cur_dir[name]

    def load_ls_results(self, cur_dir: Dir, ls_results: list[str]):
        dirs = [res for res in ls_results if res.startswith("dir")]
        files = [res for res in ls_results if not res.startswith("dir")]
        cur_dir = self.load_files(cur_dir, files)
        cur_dir = self.load_dirs(cur_dir, dirs)
        return cur_dir

    def load_files(self, cur_dir: Dir, files: list[str]) -> Dir:
        for file in files:
            file_size, file_name = file.split()
            cur_dir.add_file(file_name, int(file_size))
        return cur_dir

    def load_dirs(self, cur_dir: Dir, dirs: list[str]) -> Dir:
        for sub_dir in dirs:
            name = sub_dir.split()[1]
            cur_dir.add_sub_dir(name)
        return cur_dir

    def execute_commands(self, commands: list[Command]):
        for command in commands:
            if command.cmd.startswith("cd"):
                _, target_dir = command.cmd.split()
                if target_dir == "..":
                    self.cur_dir = self.cur_dir.parent
                elif target_dir == "/":
                    self.cur_dir = self.root
                # TODO: Add code to handle ..
                else:
                    self.cur_dir = self.cur_dir.sub_dirs[target_dir]
            elif command.cmd.startswith("ls"):
                self.cur_dir = self.load_ls_results(self.cur_dir, command.results)
            else:
                print(f"WTF? Unknown command {command}")


def part_1(input_data):
    pass


def part_2(input_data):
    pass


def main():
    input_data = parse_input()


if __name__ == "__main__":
    main()
