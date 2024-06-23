from flask import Flask, request, render_template
from SoloOutput import *

# Define the scales (as provided)
pentatonic_scales = {
    "C Major": c_major_pentatonic_Positions,
    "D Major": d_major_pentatonic_Positions,
    "E Major": e_major_pentatonic_Positions,
    "F Major": f_major_pentatonic_Positions,
    "G Major": g_major_pentatonic_Positions,
    "A Major": a_major_pentatonic_Positions,
    "B Major": b_major_pentatonic_Positions,
    "A Minor": a_minor_pentatonic_Positions,
    "D Minor": d_minor_pentatonic_patterns,
    "E Minor": e_minor_pentatonic_patterns,
    "F Minor": f_minor_pentatonic_patterns,
    "G Minor": g_minor_pentatonic_patterns,
    "C Minor": c_minor_pentatonic_patterns,
    "B Minor": b_minor_pentatonic_patterns
}
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    key = request.form['key']
    path_length = request.form['path_length']

    if key not in pentatonic_scales:
        return render_template('index.html', error="Key not supported.")
    
    try:
        path_length = int(path_length)
    except ValueError:
        return render_template('index.html', error="Invalid path length.")

    scale_positions = [get_fretboard_positions(pentatonic_scales[key][f"Position {i+1}"]) for i in range(5)]
    
    random_path = find_random_path_with_positions(scale_positions, path_length)
    if not random_path:  # Check if the path is empty
        return render_template('index.html', error="An error occurred while generating the path.")
    
    path_with_effects = add_effects(random_path)
    tabs_with_effects = path_to_tabs_with_effects(path_with_effects)
    
    return render_template('index.html', tabs=tabs_with_effects)


if __name__ == '__main__':
    app.run(debug=True)