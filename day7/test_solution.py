import pytest

from solution import Dir, File, Terminal


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
