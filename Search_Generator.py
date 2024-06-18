import random
from Fretboard import fretboard
# Fretboard and scale positions already defined
c_major_pentatonic_Positions = {
    "Position 1": {
        "e": ["5", "8"],
        "B": ["5", "8"],
        "G": ["5", "7"],
        "D": ["5", "7"],
        "A": ["5", "7"],
        "E": ["5", "8"]
    },
    "Position 2": {
        "e": ["8", "10"],
        "B": ["8", "10"],
        "G": ["7", "9"],
        "D": ["7", "10"],
        "A": ["7", "10"],
        "E": ["8", "10"]
    },
    "Position 3": {
        "e": ["10", "12"],
        "B": ["10", "13"],
        "G": ["9", "12"],
        "D": ["10", "12"],
        "A": ["10", "12"],
        "E": ["10", "12"]
    },
    "Position 4": {
        "e": ["0", "3"],
        "B": ["1", "3"],
        "G": ["0", "2"],
        "D": ["0", "2"],
        "A": ["0", "3"],
        "E": ["0", "3"]
    },
    "Position 5": {
        "e": ["3", "5"],
        "B": ["3", "5"],
        "G": ["2", "5"],
        "D": ["2", "5"],
        "A": ["3", "5"],
        "E": ["3", "5"]
    }
}

d_major_pentatonic_Positions = {
    "Position 1": {
        "e": ["7", "10"],
        "B": ["7", "10"],
        "G": ["7", "9"],
        "D": ["7", "9"],
        "A": ["7", "9"],
        "E": ["7", "10"]
    },
    "Position 2": {
        "e": ["10", "12"],
        "B": ["10", "12"],
        "G": ["9", "11"],
        "D": ["9", "12"],
        "A": ["9", "12"],
        "E": ["10", "12"]
    },
    "Position 3": {
        "e": ["12", "14"],
        "B": ["12", "15"],
        "G": ["11", "14"],
        "D": ["12", "14"],
        "A": ["12", "14"],
        "E": ["12", "14"]
    },
    "Position 4": {
        "e": ["2", "5"],
        "B": ["3", "5"],
        "G": ["2", "4"],
        "D": ["2", "4"],
        "A": ["2", "5"],
        "E": ["2", "5"]
    },
    "Position 5": {
        "e": ["5", "7"],
        "B": ["5", "7"],
        "G": ["4", "7"],
        "D": ["4", "7"],
        "A": ["5", "7"],
        "E": ["5", "7"]
    }
}

e_major_pentatonic_Positions = {
    "Position 1": {
        "e": ["9", "12"],
        "B": ["9", "12"],
        "G": ["9", "11"],
        "D": ["9", "11"],
        "A": ["9", "11"],
        "E": ["9", "12"]
    },
    "Position 2": {
        "e": ["12", "14"],
        "B": ["12", "14"],
        "G": ["11", "13"],
        "D": ["11", "14"],
        "A": ["11", "14"],
        "E": ["12", "14"]
    },
    "Position 3": {
        "e": ["2", "4"],
        "B": ["2", "5"],
        "G": ["1", "4"],
        "D": ["2", "4"],
        "A": ["2", "4"],
        "E": ["2", "4"]
    },
    "Position 4": {
        "e": ["4", "7"],
        "B": ["5", "7"],
        "G": ["4", "6"],
        "D": ["4", "6"],
        "A": ["4", "7"],
        "E": ["4", "7"]
    },
    "Position 5": {
        "e": ["7", "9"],
        "B": ["7", "9"],
        "G": ["6", "9"],
        "D": ["6", "9"],
        "A": ["7", "9"],
        "E": ["7", "9"]
    }
}

f_major_pentatonic_Positions = {
    "Position 1": {
        "e": ["10", "13"],
        "B": ["10", "13"],
        "G": ["10", "12"],
        "D": ["10", "12"],
        "A": ["10", "12"],
        "E": ["10", "13"]
    },
    "Position 2": {
        "e": ["1", "3"],
        "B": ["1", "3"],
        "G": ["0", "2"],
        "D": ["0", "3"],
        "A": ["0", "3"],
        "E": ["1", "3"]
    },
    "Position 3": {
        "e": ["3", "5"],
        "B": ["3", "6"],
        "G": ["2", "5"],
        "D": ["3", "5"],
        "A": ["3", "5"],
        "E": ["3", "5"]
    },
    "Position 4": {
        "e": ["5", "8"],
        "B": ["6", "8"],
        "G": ["5", "7"],
        "D": ["5", "7"],
        "A": ["5", "8"],
        "E": ["5", "8"]
    },
    "Position 5": {
        "e": ["8", "10"],
        "B": ["8", "10"],
        "G": ["7", "10"],
        "D": ["7", "10"],
        "A": ["8", "10"],
        "E": ["8", "10"]
    }
}

g_major_pentatonic_Positions = {
    "Position 1": {
        "e": ["0", "3"],
        "B": ["0", "3"],
        "G": ["0", "2"],
        "D": ["0", "2"],
        "A": ["0", "2"],
        "E": ["0", "3"]
    },
    "Position 2": {
        "e": ["3", "5"],
        "B": ["3", "5"],
        "G": ["2", "4"],
        "D": ["2", "5"],
        "A": ["2", "5"],
        "E": ["3", "5"]
    },
    "Position 3": {
        "e": ["5", "7"],
        "B": ["5", "8"],
        "G": ["4", "7"],
        "D": ["5", "7"],
        "A": ["5", "7"],
        "E": ["5", "7"]
    },
    "Position 4": {
        "e": ["7", "10"],
        "B": ["8", "10"],
        "G": ["7", "9"],
        "D": ["7", "9"],
        "A": ["7", "10"],
        "E": ["7", "10"]
    },
    "Position 5": {
        "e": ["10", "12"],
        "B": ["10", "12"],
        "G": ["9", "12"],
        "D": ["9", "12"],
        "A": ["10", "12"],
        "E": ["10", "12"]
    }
}

a_major_pentatonic_Positions = {
    "Position 1": {
        "e": ["2", "5"],
        "B": ["2", "5"],
        "G": ["2", "4"],
        "D": ["2", "4"],
        "A": ["2", "4"],
        "E": ["2", "5"]
    },
    "Position 2": {
        "e": ["5", "7"],
        "B": ["5", "7"],
        "G": ["4", "6"],
        "D": ["4", "7"],
        "A": ["4", "7"],
        "E": ["5", "7"]
    },
    "Position 3": {
        "e": ["7", "9"],
        "B": ["7", "10"],
        "G": ["6", "9"],
        "D": ["7", "9"],
        "A": ["7", "9"],
        "E": ["7", "9"]
    },
    "Position 4": {
        "e": ["9", "12"],
        "B": ["10", "12"],
        "G": ["9", "11"],
        "D": ["9", "11"],
        "A": ["9", "12"],
        "E": ["9", "12"]
    },
    "Position 5": {
        "e": ["12", "14"],
        "B": ["12", "14"],
        "G": ["11", "14"],
        "D": ["11", "14"],
        "A": ["12", "14"],
        "E": ["12", "14"]
    }
}

b_major_pentatonic_Positions = {
    "Position 1": {
        "e": ["4", "7"],
        "B": ["4", "7"],
        "G": ["4", "6"],
        "D": ["4", "6"],
        "A": ["4", "6"],
        "E": ["4", "7"]
    },
    "Position 2": {
        "e": ["7", "9"],
        "B": ["7", "9"],
        "G": ["6", "8"],
        "D": ["6", "9"],
        "A": ["6", "9"],
        "E": ["7", "9"]
    },
    "Position 3": {
        "e": ["9", "11"],
        "B": ["9", "12"],
        "G": ["8", "11"],
        "D": ["9", "11"],
        "A": ["9", "11"],
        "E": ["9", "11"]
    },
    "Position 4": {
        "e": ["11", "14"],
        "B": ["12", "14"],
        "G": ["11", "13"],
        "D": ["11", "13"],
        "A": ["11", "14"],
        "E": ["11", "14"]
    },
    "Position 5": {
        "e": ["2", "4"],
        "B": ["2", "4"],
        "G": ["1", "4"],
        "D": ["1", "4"],
        "A": ["2", "4"],
        "E": ["2", "4"]
    }
}

g_minor_pentatonic_patterns = {
    "Pattern 1": {
        "e": ["3", "6"],
        "B": ["3", "6"],
        "G": ["3", "5"],
        "D": ["3", "5"],
        "A": ["3", "5"],
        "E": ["3", "6"]
    },
    "Pattern 2": {
        "e": ["6", "8"],
        "B": ["6", "8"],
        "G": ["5", "7"],
        "D": ["5", "8"],
        "A": ["5", "8"],
        "E": ["6", "8"]
    },
    "Pattern 3": {
        "e": ["8", "10"],
        "B": ["8", "11"],
        "G": ["7", "10"],
        "D": ["8", "10"],
        "A": ["8", "10"],
        "E": ["8", "10"]
    },
    "Pattern 4": {
        "e": ["10", "13"],
        "B": ["11", "13"],
        "G": ["10", "12"],
        "D": ["10", "12"],
        "A": ["10", "13"],
        "E": ["10", "13"]
    },
    "Pattern 5": {
        "e": ["1", "3"],
        "B": ["1", "3"],
        "G": ["0", "3"],
        "D": ["0", "3"],
        "A": ["1", "3"],
        "E": ["1", "3"]
    }
}

c_minor_pentatonic_patterns = {
    "Pattern 1": {
        "e": ["8", "11"],
        "B": ["8", "11"],
        "G": ["8", "10"],
        "D": ["8", "10"],
        "A": ["8", "10"],
        "E": ["8", "11"]
    },
    "Pattern 2": {
        "e": ["11", "13"],
        "B": ["11", "13"],
        "G": ["10", "12"],
        "D": ["10", "13"],
        "A": ["10", "13"],
        "E": ["11", "13"]
    },
    "Pattern 3": {
        "e": ["1", "3"],
        "B": ["1", "4"],
        "G": ["0", "3"],
        "D": ["1", "3"],
        "A": ["1", "3"],
        "E": ["1", "3"]
    },
    "Pattern 4": {
        "e": ["3", "6"],
        "B": ["4", "6"],
        "G": ["3", "5"],
        "D": ["3", "5"],
        "A": ["3", "6"],
        "E": ["3", "6"]
    },
    "Pattern 5": {
        "e": ["6", "8"],
        "B": ["6", "8"],
        "G": ["5", "8"],
        "D": ["5", "8"],
        "A": ["6", "8"],
        "E": ["6", "8"]
    }
}



a_minor_pentatonic_Positions = {
    "Position 1": {
        "e": ["5", "8"],
        "B": ["5", "8"],
        "G": ["5", "7"],
        "D": ["5", "7"],
        "A": ["5", "7"],
        "E": ["5", "8"]
    },
    "Position 2": {
        "e": ["8", "10"],
        "B": ["8", "10"],
        "G": ["7", "9"],
        "D": ["7", "10"],
        "A": ["7", "10"],
        "E": ["8", "10"]
    },
    "Position 3": {
        "e": ["10", "12"],
        "B": ["10", "13"],
        "G": ["9", "12"],
        "D": ["10", "12"],
        "A": ["10", "12"],
        "E": ["10", "12"]
    },
    "Position 4": {
        "e": ["0", "3"],
        "B": ["1", "3"],
        "G": ["0", "2"],
        "D": ["0", "2"],
        "A": ["0", "3"],
        "E": ["0", "3"]
    },
    "Position 5": {
        "e": ["3", "5"],
        "B": ["3", "5"],
        "G": ["2", "5"],
        "D": ["2", "5"],
        "A": ["3", "5"],
        "E": ["3", "5"]
    }
}

d_minor_pentatonic_patterns = {
    "Pattern 1": {
        "e": ["10", "13"],
        "B": ["10", "13"],
        "G": ["10", "12"],
        "D": ["10", "12"],
        "A": ["10", "12"],
        "E": ["10", "13"]
    },
    "Pattern 2": {
        "e": ["1", "3"],
        "B": ["1", "3"],
        "G": ["0", "2"],
        "D": ["0", "3"],
        "A": ["0", "3"],
        "E": ["1", "3"]
    },
    "Pattern 3": {
        "e": ["3", "5"],
        "B": ["3", "6"],
        "G": ["2", "5"],
        "D": ["3", "5"],
        "A": ["3", "5"],
        "E": ["3", "5"]
    },
    "Pattern 4": {
        "e": ["5", "8"],
        "B": ["6", "8"],
        "G": ["5", "7"],
        "D": ["5", "7"],
        "A": ["5", "8"],
        "E": ["5", "8"]
    },
    "Pattern 5": {
        "e": ["8", "10"],
        "B": ["8", "10"],
        "G": ["7", "10"],
        "D": ["7", "10"],
        "A": ["8", "10"],
        "E": ["8", "10"]
    }
}

e_minor_pentatonic_patterns = {
    "Pattern 1": {
        "e": ["0", "3"],
        "B": ["0", "3"],
        "G": ["0", "2"],
        "D": ["0", "2"],
        "A": ["0", "2"],
        "E": ["0", "3"]
    },
    "Pattern 2": {
        "e": ["3", "5"],
        "B": ["3", "5"],
        "G": ["2", "4"],
        "D": ["2", "5"],
        "A": ["2", "5"],
        "E": ["3", "5"]
    },
    "Pattern 3": {
        "e": ["5", "7"],
        "B": ["5", "8"],
        "G": ["4", "7"],
        "D": ["5", "7"],
        "A": ["5", "7"],
        "E": ["5", "7"]
    },
    "Pattern 4": {
        "e": ["7", "10"],
        "B": ["8", "10"],
        "G": ["7", "9"],
        "D": ["7", "9"],
        "A": ["7", "10"],
        "E": ["7", "10"]
    },
    "Pattern 5": {
        "e": ["10", "12"],
        "B": ["10", "12"],
        "G": ["9", "12"],
        "D": ["9", "12"],
        "A": ["10", "12"],
        "E": ["10", "12"]
    }
}

f_minor_pentatonic_patterns = {
    "Pattern 1": {
        "e": ["1", "4"],
        "B": ["1", "4"],
        "G": ["1", "3"],
        "D": ["1", "3"],
        "A": ["1", "3"],
        "E": ["1", "4"]
    },
    "Pattern 2": {
        "e": ["4", "6"],
        "B": ["4", "6"],
        "G": ["3", "5"],
        "D": ["3", "6"],
        "A": ["3", "6"],
        "E": ["4", "6"]
    },
    "Pattern 3": {
        "e": ["6", "8"],
        "B": ["6", "9"],
        "G": ["5", "8"],
        "D": ["6", "8"],
        "A": ["6", "8"],
        "E": ["6", "8"]
    },
    "Pattern 4": {
        "e": ["8", "11"],
        "B": ["9", "11"],
        "G": ["8", "10"],
        "D": ["8", "10"],
        "A": ["8", "11"],
        "E": ["8", "11"]
    },
    "Pattern 5": {
        "e": ["11", "13"],
        "B": ["11", "13"],
        "G": ["10", "13"],
        "D": ["10", "13"],
        "A": ["11", "13"],
        "E": ["11", "13"]
    }
}

b_minor_pentatonic_patterns = {
    "Pattern 1": {
        "e": ["7", "10"],
        "B": ["7", "10"],
        "G": ["7", "9"],
        "D": ["7", "9"],
        "A": ["7", "9"],
        "E": ["7", "10"]
    },
    "Pattern 2": {
        "e": ["10", "12"],
        "B": ["10", "12"],
        "G": ["9", "11"],
        "D": ["9", "12"],
        "A": ["9", "12"],
        "E": ["10", "12"]
    },
    "Pattern 3": {
        "e": ["12", "14"],
        "B": ["12", "15"],
        "G": ["11", "14"],
        "D": ["12", "14"],
        "A": ["12", "14"],
        "E": ["12", "14"]
    },
    "Pattern 4": {
        "e": ["2", "5"],
        "B": ["3", "5"],
        "G": ["2", "4"],
        "D": ["2", "4"],
        "A": ["2", "5"],
        "E": ["2", "5"]
    },
    "Pattern 5": {
        "e": ["5", "7"],
        "B": ["5", "7"],
        "G": ["4", "7"],
        "D": ["4", "7"],
        "A": ["5", "7"],
        "E": ["5", "7"]
    }
}
# Function to get fretboard positions for a given scale
def get_fretboard_positions(scale):
    positions = {}
    for note in scale:
        for string, frets in fretboard.items():
            for fret_note, fret in frets:
                if fret_note == note:
                    if note not in positions:
                        positions[note] = []
                    positions[note].append((string, fret))
    return positions

# Function to find random path with constraints
def find_random_path(scale_positions, root_note, path_length, max_fret_jump=3, emotion=None):
    path = []
    current_note = root_note
    current_position = random.choice(scale_positions[current_note])
    path.append(current_position)
    
    for _ in range(path_length - 2):
        possible_positions = [pos for note in scale_positions for pos in scale_positions[note]]
        valid_positions = [pos for pos in possible_positions if abs(pos[1] - current_position[1]) <= max_fret_jump]
        
        if not valid_positions:
            valid_positions = possible_positions
        
        current_position = random.choice(valid_positions)
        path.append(current_position)
        
        next_notes = [note for note, positions in scale_positions.items() if current_position in positions]
        current_note = random.choice(next_notes)
    
    # End at root note
    path.append(random.choice(scale_positions[root_note]))
    return path

# Function to convert path to tab format
def path_to_tabs(path):
    tab_lines = ["e|", "B|", "G|", "D|", "A|", "E|"]
    string_indices = {"e": 0, "B": 1, "G": 2, "D": 3, "A": 4, "E": 5}
    for string, fret in path:
        for i in range(len(tab_lines)):
            if i == string_indices[string]:
                tab_lines[i] += f"--{fret}"
            else:
                tab_lines[i] += "--"
    return "\n".join(tab_lines)

# Example usage
a_minor_pentatonic_positions = a_minor_pentatonic_Positions["Position 1"]
root_note = "A"
path_length = 10

random_path = find_random_path(a_minor_pentatonic_positions, root_note, path_length)
tabs = path_to_tabs(random_path)
print(tabs)

def add_slides_bends(path):
    modified_path = []
    for i in range(len(path) - 1):
        modified_path.append(path[i])
        if random.random() < 0.2:  # 20% probability for slides/bends
            slide_or_bend = random.choice(["slide", "bend"])
            modified_path.append((slide_or_bend, path[i], path[i+1]))
    modified_path.append(path[-1])
    return modified_path

def path_to_tabs_with_effects(path):
    tab_lines = ["e|", "B|", "G|", "D|", "A|", "E|"]
    string_indices = {"e": 0, "B": 1, "G": 2, "D": 3, "A": 4, "E": 5}
    for item in path:
        if isinstance(item, tuple) and len(item) == 3:
            effect, pos1, pos2 = item
            string, fret1 = pos1
            _, fret2 = pos2
            effect_str = "--" if effect == "slide" else "b"
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

# Example usage
random_path = find_random_path(a_minor_pentatonic_positions, root_note, path_length)
path_with_effects = add_slides_bends(random_path)
tabs_with_effects = path_to_tabs_with_effects(path_with_effects)
print(tabs_with_effects)

