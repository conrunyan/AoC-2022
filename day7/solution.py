from uuid import uuid4


def parse_input():
    with open("input.txt") as FH:
        return FH.readlines()


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name} (file, size={str(self.size)})"


class Dir:
    def __init__(self, name: str, parent=None):
        self.parent = parent
        self.sub_dirs = {}
        self.files = []
        self.name = name

    def __repr__(self):
        return f"{self.name} (dir)"

    def add_sub_dir(self, name: str) -> "Dir":
        print(f"Adding '{name}' to {self}")
        self.sub_dirs[name] = Dir(name, self)
        return self.sub_dirs[name]

    def add_file(self, name, size):
        print(f"Adding file '{size} {name}' to {self}")
        self.files.append(File(name, size))

    def get_dir_size(self) -> int:
        file_sizes = [f.size for f in self.files]
        dir_sizes = [d.get_dir_size() for d in self.sub_dirs.values()]
        return sum([*file_sizes, *dir_sizes])

    def print_files(self, indent: str = "", prefix: str = "- "):
        for fl in self.files:
            print(f"{indent}  {prefix}{fl}")

    def print_dirs(self):
        def _print_dirs(cur_dir: "Dir", indent: str = "", tab_size=2, prefix="- "):
            print(f"{indent}{prefix}{cur_dir}")
            cur_dir.print_files(indent, prefix)
            indent += " " * tab_size
            for sub_dir in cur_dir.sub_dirs.values():
                _print_dirs(sub_dir, indent)

        _print_dirs(self)


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
        if name == "..":
            self.cur_dir = self.cur_dir.parent
        elif name == "/":
            self.cur_dir = self.root
        else:
            self.cur_dir = self.cur_dir.sub_dirs[name]
        print(f"PWD: {self.cur_dir}")

    def list_dir_sizes(self, target_dir: Dir) -> dict[str, int]:
        dirs = {}

        # No more dirs to search. Get size and stop here.
        if not target_dir.sub_dirs:
            dir_key = f"{target_dir.parent.name}-{target_dir.name}-{str(uuid4())}"
            solo_dir = {dir_key: target_dir.get_dir_size()}
            return solo_dir

        for dir in target_dir.sub_dirs.values():
            sub_sizes = self.list_dir_sizes(dir)
            if dir.sub_dirs:
                cur_size = dir.get_dir_size()
                dir_key = f"{dir.parent.name}-{dir.name}-{str(uuid4())}"
                dirs[dir_key] = cur_size
            dirs = {**dirs, **sub_sizes}
        return dirs

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

            # Handling directory movement
            if command.cmd.startswith("cd"):
                _, target_dir = command.cmd.split()
                self.cd(target_dir)

            # Handling output of ls (technically just creates the directory and its content)
            elif command.cmd.startswith("ls"):
                self.cur_dir = self.load_ls_results(self.cur_dir, command.results)

            else:
                print(f"WTF? Unknown command {command}")


def part_1(input_data):
    commands = CommandUtils.parse_commands(input_data)
    term = Terminal()
    term.execute_commands(commands)

    # Get desired dirs total size
    max_size = 100000
    sizes = term.list_dir_sizes(term.root)
    desired_sizes = [{k: s} for k, s in sizes.items() if s <= max_size]
    total_size = sum([list(s.values())[0] for s in desired_sizes])
    print("PART 1:", total_size)


def part_2(input_data):
    commands = CommandUtils.parse_commands(input_data)
    term = Terminal()
    term.execute_commands(commands)

    max_space = 70000000
    needed_space = 30000000
    total_used_space = term.root.get_dir_size()
    space_left = max_space - total_used_space
    space_to_free = needed_space - space_left

    sizes = term.list_dir_sizes(term.root)
    sorted_sizes = sorted(sizes.items(), key=lambda v: v[1])
    print(sorted_sizes)
    applicable_dirs = [d for d in sorted_sizes if d[1] >= space_to_free]
    smallest_dir = applicable_dirs[0]
    print("PART 2", smallest_dir)


def main():
    input_data = parse_input()
    part_1(input_data)
    part_2(input_data)


if __name__ == "__main__":
    main()
