from Search_Generator import *

# Example usage
scale_positions = [get_fretboard_positions(a_minor_pentatonic_Positions[f"Position {i+1}"]) for i in range(5)]
root_note = "A"
path_length = 24

random_path = find_random_path_with_positions(scale_positions, root_note, path_length)
path_with_effects = add_effects(random_path)
tabs_with_effects = path_to_tabs_with_effects(path_with_effects)
print(tabs_with_effects)