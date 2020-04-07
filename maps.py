from enum import Enum
from pathlib import Path
import sqlite3
import csv
import pprint


pp = pprint.PrettyPrinter(indent=2)


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

    with Path('./data/areas.positional.relationships.csv').open() as f:
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
        select seed
        from (
            select id,
                lag(direction) over (order by id) as prev_d,
                from_level, direction as curr_d, seed,
                lead(direction) over (order by id) as next_d
            from positional_relationship
        ) as t
        where from_level = "Blood Moor"
        and prev_d = 3
        and curr_d = 0
        and next_d = 1
    ''')

    for row in query:
        yield row[0]

    conn.close()