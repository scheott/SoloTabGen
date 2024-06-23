import random
from Fretboard import *

def get_fretboard_positions(scale_position):
    positions = []
    for string, frets in scale_position.items():
        for fret in frets:
            positions.append((string, int(fret)))
    return positions

def find_random_path_with_positions(scale_positions, path_length, max_fret_jump=2, max_fret_diff=6, stay_in_position=25):
    try:
        path_length = int(path_length)  # Ensure path_length is an integer
        stay_in_position = int(stay_in_position)  # Ensure stay_in_position is an integer
    except ValueError:
        return []

    print(f"scale_positions: {scale_positions}")
    print(f"path_length: {path_length}, stay_in_position: {stay_in_position}")

    path = []
    current_position = random.choice(scale_positions[0])
    path.append(current_position)

    print(f"Initial current_position: {current_position}")

    position_duration = max(1, path_length // stay_in_position)
    position_count = 0
    current_scale_index = 0

    for _ in range(path_length - 2):
        if position_count >= position_duration:
            current_scale_index = (current_scale_index + 1) % len(scale_positions)
            position_count = 0

        valid_positions = [
            pos for pos in scale_positions[current_scale_index]
            if abs(pos[1] - current_position[1]) <= max_fret_jump 
            and abs(pos[1] - current_position[1]) <= max_fret_diff
            and pos[0] != current_position[0]
        ]

        print(f"valid_positions: {valid_positions}")

        if not valid_positions:
            valid_positions = scale_positions[current_scale_index]

        current_position = random.choice(valid_positions)
        path.append(current_position)
        position_count += 1

    print(f"Final path before adding end position: {path}")

    end_positions = [pos for pos in scale_positions[0] if pos[0] == current_position[0]]
    path.append(random.choice(end_positions))
    print(f"Final path: {path}")
    return path

def add_effects(path):
    if not path:
        return path  # Return the path as is if it's empty

    modified_path = []
    for i in range(len(path) - 1):
        modified_path.append(path[i])
        if random.random() < 0.3:  # 30% probability for effects
            effect = random.choice(["slide", "pull-off", "bend"])
            pos1 = path[i]
            pos2 = path[i + 1]
            if pos1[1] != pos2[1]:  # Ensure the fret numbers are not the same
                modified_path.append((effect, pos1, pos2))
    modified_path.append(path[-1])
    return modified_path

def path_to_tabs_with_effects(path):
    tab_lines = ["e|", "B|", "G|", "D|", "A|", "E|"]
    string_indices = {"e": 0, "B": 1, "G": 2, "D": 3, "A": 4, "E": 5}
    max_length = 0
    for item in path:
        if isinstance(item, tuple) and len(item) == 3:
            effect, pos1, pos2 = item
            string, fret1 = pos1
            _, fret2 = pos2
            effect_str = "s" if effect == "slide" else "p" if effect == "pull-off" else "b"
            for i in range(len(tab_lines)):
                if i == string_indices[string]:
                    tab_lines[i] += f"{fret1}{effect_str}{fret2}"
                else:
                    tab_lines[i] += "--"
        else:
            string, fret = item
            for i in range(len(tab_lines)):
                if i == string_indices[string]:
                    tab_lines[i] += f"--{fret}"
                else:
                    tab_lines[i] += "--"
        max_length = max(max_length, len(tab_lines[string_indices[string]]))

    # Ensure all lines are the same length
    for i in range(len(tab_lines)):
        tab_lines[i] += "-" * (max_length - len(tab_lines[i]))

    return "\n".join(tab_lines)