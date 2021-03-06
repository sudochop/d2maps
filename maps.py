from enum import Enum
from pathlib import Path
import sqlite3
import csv


class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3
    Top = 4
    Right = 5
    Bottom = 6
    Left = 7

    @classmethod
    def from_csv(cls, dir):
        return {
            'TopRight': cls.North,
            'BottomRight': cls.East,
            'BottomLeft': cls.South,
            'TopLeft': cls.West,
            'Top': cls.Top,
            'Right': cls.Right,
            'Bottom': cls.Bottom,
            'Left': cls.Left
        }[dir]


def get_db_connection():
    return sqlite3.connect('./data/seeds.db')


def db_create_table_arcane():
    conn = get_db_connection()

    conn.execute('''
        CREATE TABLE arcane (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            seed INTEGER NOT NULL UNIQUE,
            summoner_dir INTEGER NOT NULL,
            portals_dir	INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def db_create_table_positional_relationship():
    conn = get_db_connection()

    conn.execute('''
        CREATE TABLE positional_relationship (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            seed INTEGER NOT NULL,
            from_level TEXT NOT NULL,
            to_level TEXT NOT NULL,
            direction INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def db_create_table_room():
    conn = get_db_connection()

    conn.execute('''
        CREATE TABLE room (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            seed INTEGER NOT NULL,
            level_name TEXT NOT NULL,
            room_flags INTEGER NOT NULL,
            room_number	INTEGER NOT NULL,
            sub_number INTEGER NOT NULL,
            preset_type	INTEGER NOT NULL,
            is_preset INTEGER NOT NULL,
            preset_txt_number INTEGER NOT NULL,
            level_relative_room_coords_x INTEGER NOT NULL,
            level_relative_room_coords_y INTEGER NOT NULL,
            absolute_room_coords_x INTEGER NOT NULL,
            absolute_room_coords_y INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def db_create_table_preset():
    conn = get_db_connection()

    conn.execute('''
        CREATE TABLE preset (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            seed INTEGER NOT NULL,
            level_name TEXT NOT NULL,
            preset_id TEXT NOT NULL,
            level_relative_room_coords_x INTEGER NOT NULL,
            level_relative_room_coords_y INTEGER NOT NULL,
            absolute_room_coords_x INTEGER NOT NULL,
            absolute_room_coords_y INTEGER NOT NULL,
            room_relative_preset_coords_x INTEGER NOT NULL,
            room_relative_preset_coords_y INTEGER NOT NULL,
            absolute_preset_coords_x INTEGER NOT NULL,
            absolute_preset_coords_y INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def csv_import_arcanes():
    conn = get_db_connection()

    with Path('./data/arcane.csv').open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            fields = (
                int(row['seed']),
                Direction.from_csv(row['summoner_dir']).value,
                Direction.from_csv(row['portals_dir']).value
            )
            conn.execute('''
                INSERT INTO arcane
                    (
                        seed,
                        summoner_dir,
                        portals_dir
                    )
                VALUES (?,?,?)
            ''', fields)

    conn.commit()
    conn.close()


def csv_import_areas_positional_relationships():
    conn = get_db_connection()

    with Path('./data/areas.positional.relationships 2.csv').open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            fields = (
                int(row['seed']),
                row['from_level'],
                row['to_level'],
                Direction.from_csv(row['direction']).value
            )
            conn.execute('''
                INSERT INTO positional_relationship
                    (
                        seed,
                        from_level,
                        to_level,
                        direction
                    )
                VALUES (?,?,?,?)
            ''', fields)

    conn.commit()
    conn.close()


def csv_import_rooms():
    conn = get_db_connection()

    with Path('./data/areas.rooms.csv').open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            fields = (
                int(row['seed']),
                row['level_name'],
                int(row['room_flags']),
                int(row['room_number']),
                int(row['sub_number']),
                int(row['preset_type']),
                int(row['is_preset']),
                int(row['preset_txt_number']),
                int(row['level_relative_room_coords_x']),
                int(row['level_relative_room_coords_y']),
                int(row['absolute_room_coords_x']),
                int(row['absolute_room_coords_y'])
            )
            conn.execute('''
                INSERT INTO room
                    (
                        seed,
                        level_name,
                        room_flags,
                        room_number,
                        sub_number,
                        preset_type,
                        is_preset,
                        preset_txt_number,
                        level_relative_room_coords_x,
                        level_relative_room_coords_y,
                        absolute_room_coords_x,
                        absolute_room_coords_y
                    )
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            ''', fields)

    conn.commit()
    conn.close()


def csv_import_presets():
    conn = get_db_connection()

    with Path('./data/areas.rooms.presets.csv').open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            fields = (
                int(row['seed']),
                row['level_name'],
                row['id'],
                int(row['level_relative_room_coords_x']),
                int(row['level_relative_room_coords_y']),
                int(row['absolute_room_coords_x']),
                int(row['absolute_room_coords_y']),
                int(row['room_relative_preset_coords_x']),
                int(row['room_relative_preset_coords_y']),
                int(row['absolute_preset_coords_x']),
                int(row['absolute_preset_coords_y'])
            )
            conn.execute('''
                INSERT INTO preset
                    (
                        seed,
                        level_name,
                        preset_id,
                        level_relative_room_coords_x,
                        level_relative_room_coords_y,
                        absolute_room_coords_x,
                        absolute_room_coords_y,
                        room_relative_preset_coords_x,
                        room_relative_preset_coords_y,
                        absolute_preset_coords_x,
                        absolute_preset_coords_y
                    )
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
            ''', fields)

    conn.commit()
    conn.close()


def db_create_tables():
    print('creating table "arcane"')
    db_create_table_arcane()
    print('creating table "positional_relationship"')
    db_create_table_positional_relationship()
    print('creating table "room"')
    db_create_table_room()
    print('creating table "preset"')
    db_create_table_preset()
    print('done')


def csv_import():
    print('importing arcanes')
    csv_import_arcanes()
    print('importing positional relationships')
    csv_import_areas_positional_relationships()
    print('importing rooms')
    csv_import_rooms()
    print('importing presets')
    csv_import_presets()
    print('done')


def get_indrek_seeds():
    conn = get_db_connection()

    query = conn.execute('''
        SELECT
            seed
        FROM (
            SELECT
                id,
                LAG(direction) OVER (ORDER BY id) AS prev_d,
                from_level, direction AS curr_d, seed,
                LEAD(direction) OVER (ORDER BY id) AS next_d
            FROM
                positional_relationship
        )
        WHERE
            from_level = "Blood Moor"
            AND prev_d = 3
            AND curr_d = 0
            AND next_d = 1
    ''')

    for row in query:
        yield row[0]

    conn.close()


def get_indrek_seeds_with_arcane():
    conn = get_db_connection()

    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = cursor.execute('''
        SELECT
            pr.seed AS seed,
            ar.portals_dir AS portals,
            ar.summoner_dir AS summoner
        FROM (
            SELECT
                id,
                LAG(direction) OVER (ORDER BY id) AS prev_d,
                from_level, direction AS curr_d, seed,
                LEAD(direction) OVER (ORDER BY id) AS next_d
            FROM
                positional_relationship
        ) AS pr
        JOIN arcane AS ar ON
            pr.seed = ar.seed
        WHERE
            from_level = "Blood Moor"
            AND prev_d = 3
            AND curr_d = 0
            AND next_d = 1
    ''')

    for row in query:
        yield dict(row)

    conn.close()


def get_palace_arcane_door():
    conn = get_db_connection()

    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = cursor.execute('''
        SELECT
            a.seed,
            a.summoner_dir,
            a.seed % 2 AS pairity
        FROM preset AS p
        JOIN arcane AS a ON
            p.seed = a.seed
        WHERE  p.level_name = "Palace Cellar Level 3"
            AND p.preset_id = "Object 292 door (Door)"
            AND p.level_relative_room_coords_x = 0
    ''')

    for row in query:
        yield dict(row)

    conn.close()


def get_door():
    parities = [[0, 0, 0, 0], [0, 0, 0, 0]]
    for row in get_palace_arcane_door():
        parities[row['pairity']][row['summoner_dir']] += 1
    return parities


def get_indrek_summoner_spread():
    '''Summoner directions for indrek seeds.'''
    summoners = [0, 0, 0, 0]
    for indrek in get_indrek_seeds_with_arcane():
        summoners[indrek['summoner']] += 1
    return summoners


def get_indrek_seed_parity():
    '''How often indrek is an even or odd seed.'''
    parity = [0, 0]
    for seed in get_indrek_seeds():
        parity[seed % 2] += 1
    return parity


def prng_generator(x, c=666, a=1791398085, b=4294967296):
    yield (x, c)
    while True:
        h = a*x + c
        x = h % b
        c = h / b
        yield (x, c)
