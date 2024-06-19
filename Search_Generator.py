import random
from Fretboard import *
# Function to get fretboard positions for a given scale position
def get_fretboard_positions(scale_position):
    positions = []
    for string, frets in scale_position.items():
        for fret in frets:
            positions.append((string, int(fret)))
    return positions

# Function to find a random path with constraints
def find_random_path_with_positions(scale_positions, root_note, path_length, max_fret_jump=2, stay_in_position=12):
    path = []
    current_position = random.choice(scale_positions[0])
    path.append(current_position)

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
        ]

        if not valid_positions:
            valid_positions = scale_positions[current_scale_index]

        current_position = random.choice(valid_positions)
        path.append(current_position)
        position_count += 1

    # End at root note
    end_positions = [pos for pos in scale_positions[0] if pos[0] == root_note]
    path.append(random.choice(end_positions))
    return path

# Function to convert path to tab format with effects
def path_to_tabs_with_effects(path):
    tab_lines = ["e|", "B|", "G|", "D|", "A|", "E|"]
    string_indices = {"e": 0, "B": 1, "G": 2, "D": 3, "A": 4, "E": 5}
    for item in path:
        if isinstance(item, tuple) and len(item) == 3:
            effect, pos1, pos2 = item
            string, fret1 = pos1
            _, fret2 = pos2
            effect_str = "s" if effect == "slide" else "p"
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
    return "\n".join(tab_lines)

def add_effects(path):
    modified_path = []
    for i in range(len(path) - 1):
        modified_path.append(path[i])
        if random.random() < 0.2:  # 20% probability for slides/pull-offs
            effect = random.choice(["slide", "pull-off"])
            modified_path.append((effect, path[i], path[i + 1]))
    modified_path.append(path[-1])
    return modified_path



