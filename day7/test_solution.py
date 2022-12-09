import pytest

from solution import Dir, Terminal, CommandUtils, Command


@pytest.fixture
def sample_dir_with_subdirs() -> Dir:
    root = Dir("/")
    root.add_file("b.txt", 14848514)
    root.add_file("c.dat", 8504156)

    # dir a
    a = root.add_sub_dir("a")
    a.add_file("f", 29116)
    a.add_file("g", 2557)
    a.add_file("h.lst", 62596)

    # dir e
    e = a.add_sub_dir("e")
    e.add_file("i", 584)

    # dir d
    d = root.add_sub_dir("d")
    d.add_file("j", 4060174)
    d.add_file("d.log", 8033020)
    d.add_file("d.ext", 5626152)
    d.add_file("k", 7214296)

    return root


@pytest.fixture
def sample_ls():
    return ["dir e", "29116 f", "2557 g"]


@pytest.fixture
def sample_cmd_input():
    return [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]


@pytest.fixture
def sample_parsed_commands(sample_cmd_input):
    return CommandUtils.parse_commands(sample_cmd_input)


def test_get_dir_size(sample_dir_with_subdirs: Dir):
    # Top level
    assert sample_dir_with_subdirs.get_dir_size() == 48381165
    # Down one level
    assert sample_dir_with_subdirs.sub_dirs["a"].get_dir_size() == 94853
    # Down another level
    assert sample_dir_with_subdirs.sub_dirs["a"].sub_dirs["e"].get_dir_size() == 584


def test_create_sub_dirs_from_ls(sample_ls):
    term = Terminal()
    d = Dir("/")
    d = term.load_ls_results(d, sample_ls)
    assert d.get_dir_size() == 31673
    assert "e" in d.sub_dirs


def test_parse_commands(sample_cmd_input):
    results = CommandUtils.parse_commands(sample_cmd_input)

    assert len(results) == 10
    assert results[0].cmd == "cd /"
    assert results[0].results == []

    assert results[1].cmd == "ls"
    assert results[1].results == ["dir a", "14848514 b.txt", "8504156 c.dat", "dir d"]


def test_execute_commands_cd(sample_parsed_commands):
    term = Terminal()
    term.execute_commands(sample_parsed_commands)

    assert term.cur_dir.name == "d"
    assert term.root.get_dir_size() == 48381165

    term.execute_commands([Command("cd ..")])
    assert list(term.cur_dir.sub_dirs.keys()) == ["a", "d"]


def test_list_dir_sizes(sample_parsed_commands):
    term = Terminal()
    term.execute_commands(sample_parsed_commands)
    expected = {"/-a": 94853, "a-e": 584, "/-d": 24933642}

    sizes = term.list_dir_sizes(term.root)

    assert sizes == expected


def test_print_dirs(sample_parsed_commands):
    term = Terminal()
    term.execute_commands(sample_parsed_commands)
    term.root.print_dirs()
