from flask import Flask, request, render_template
from SoloOutput import *
import random

app = Flask(__name__)

# Define your functions here (the ones provided earlier)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    root_note = request.form['root_note']
    path_length = int(request.form['path_length'])
    
    scale_positions = [get_fretboard_positions(a_minor_pentatonic_Positions[f"Position {i+1}"]) for i in range(5)]
    
    random_path = find_random_path_with_positions(scale_positions, root_note, path_length)
    path_with_effects = add_effects(random_path)
    tabs_with_effects = path_to_tabs_with_effects(path_with_effects)
    
    return render_template('index.html', tabs=tabs_with_effects)

if __name__ == '__main__':
    app.run(debug=True)
