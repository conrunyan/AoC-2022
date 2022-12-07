import pytest

from solution import find_start_of_packet


@pytest.fixture
def sample_streams():
    return {
        "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
        "nppdvjthqldpwncqszvftbrmjlhg": 6,
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11,
    }


def test_find_start_of_packet(sample_streams):
    for stream, expected_idx in sample_streams.items():
        result = find_start_of_packet(stream)
        assert expected_idx == result
