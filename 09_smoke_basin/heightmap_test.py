from heightmap import Coord, parse_heightmap, find_neighbors, find_basin, find_low_points

test_input = ['2199943210',
              '3987894921',
              '9856789892',
              '8767896789',
              '9899965678']


def test_parse_heightmap():
    heightmap = parse_heightmap(test_input)

    assert heightmap[Coord(0, 0)] == 2
    assert heightmap[Coord(0, 1)] == 3
    assert heightmap[Coord(1, 0)] == 1


def test_find_neighbors():
    heightmap = parse_heightmap(test_input)
    neighbors = find_neighbors(heightmap, Coord(0, 0))

    assert neighbors == {Coord(0, 1), Coord(1, 0)}


def test_find_low_points():
    heightmap = parse_heightmap(test_input)
    low_points = find_low_points(heightmap)

    assert set(low_points) == {Coord(x=1, y=0),
                               Coord(x=9, y=0),
                               Coord(x=6, y=4),
                               Coord(x=2, y=2)}


def test_find_basin():
    heightmap = parse_heightmap(test_input)

    basin = find_basin(heightmap, Coord(9, 0))
    assert len(basin) == 9
