from flask import Flask, render_template, send_file, send_from_directory, render_template_string, request
import folium
from flask import jsonify
import pandas as pd
import io
import matplotlib.pyplot as plt
import os
import district_heatmap as dmap
import criminal_analysis as criminal
from time_analysis import year_wise_map
from crime_analysis import crime_maps
import vulnerable_spots as vs

fir = pd.read_csv('Datasets/FIR_Details_Data.csv')
app = Flask(__name__, template_folder='/Users/leenagoyal/Downloads/Flask/templates')

@app.route('/')
def index():
    return render_template('root.html')

@app.route('/root.html')
def home():
    return render_template('root.html')

# District Home page
@app.route('/district.html')
def district():
    with open('data/district.txt', 'r') as file:
        districts = [line.strip() for line in file]
    with open('data/year.txt', 'r') as file:
        years = [line.strip() for line in file]
    
    return render_template('district.html', districts=districts, years=years)

# Time Home Page
@app.route('/time.html')
def time():
    with open('data/year.txt', 'r') as file:
        years = [line.strip() for line in file]
    with open('data/crimegroup.txt', 'r') as file:
        crimes = [line.strip() for line in file]

    return render_template('time.html', crimegroup=crimes, years=years)

# # Time map
# @app.route('/time_map')
# # @app.route('/year_selection')
# def timemap():
#     year = request.form.get('year')
#     if district:
#         return render_template('timemap.html',map_html=year_wise_map(year, fir))
#     else:
#         return jsonify({'error': 'District not selected'}), 400
    
# Time map
@app.route('/year_selection', methods=['POST', 'GET'])
def map_view():
    try:
        year=int(request.form.get('year').strip())
    except Exception as e:
        return f"Error: {e}"

    df = pd.read_csv('Datasets/FIR_Details_Data.csv')
    crimes_map = year_wise_map(year, df)
    # print(type(year))
    # return year
    return render_template('timemap.html', map_html=year_wise_map(year, df))    

# @app.route('/Datasets/FIR_Details_Data.csv')
# def serve_csv():
#     directory = os.path.join(app.root_path, 'datasets')
#     return send_from_directory(directory, filename='FIR_Details_Data.csv')

# Criminal Home page
@app.route('/criminal.html')
def criminal_analysis():
    with open('data/district.txt', 'r') as file:
        districts = [line.strip() for line in file]
    with open('data/year.txt', 'r') as file:
        years = [line.strip() for line in file]
    with open('data/crimesno.txt', 'r') as file:
        crimeno = [line.strip() for line in file]
    with open('data/arrested.txt', 'r') as file:
        arrid = [line.strip() for line in file]
    with open('data/unitid.txt', 'r') as file:
        unit_id = [line.strip() for line in file]
    with open('data/unitname.txt', 'r') as file:
        unit_name = [line.strip() for line in file]
    with open('data/fir.txt', 'r') as file:
        firs = [line.strip() for line in file]
    
    return render_template('criminal.html', districts=districts, years=years, crimeno=crimeno, arrestid=arrid, unitid=unit_id, firs=firs, crimeno2=crimeno, unitname=unit_name)

# District wise map
@app.route('/dropdown_selection', methods=['POST'])
def district_map():
    district = request.form.get('district')
    if district:
        return render_template('heatmap.html',map_html=dmap.district_crimes(district))
    else:
        return jsonify({'error': 'District not selected'}), 400

# Criminal Confidence Matrix
@app.route('/confidence', methods=['POST', 'GET'])
def show_confidence_matrix():
    district = request.form.get('District')
    year = int(request.form.get('Year', '2024'))
    unitname = request.form.get('UnitName')
    crimeno = request.form.get('CrimeNo')
    month = request.form.get('Month')

    if None in (district, unitname, crimeno, month):
        return "Missing form data. Please provide all required parameters."

    plot_filename = criminal.compute_confidence_matrix(district, unitname, crimeno, month, year)
    return render_template('confidence_matrix.html', plot_filename=plot_filename)

# District Heat map
@app.route('/year_selection', methods=['POST', 'GET'])
def show_district_heatmap():
    return render_template('district_heatmap.html',map_html=dmap.district_heatmap_folium())

# District Analysis
# @app.route('/district_crimes', methods=['POST'])
# def district_crimes():
#     try:
#         district_name = request.json['district']
#         year = int(request.json['year'])
#         crimes_map = dmap.crime_per_year_district(district_name, year)
#         filename = 'crimes_map.html'
#         crimes_map.save(os.path.join('templates', filename))
#         return render_template(filename)
#     except KeyError as e:
#         return jsonify({'error': 'Missing key in request: {}'.format(e)}), 400
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    
# Victim Home page
@app.route('/victim.html')
def victim():
    with open('data/crimehead.txt', 'r') as file:
        crimeheads = [line.strip() for line in file]
    with open('data/crimesno.txt', 'r') as file:
        crimeno = [line.strip() for line in file]

    return render_template('victim.html', crimeheads=crimeheads, crimeno=crimeno)

# Police Home page
@app.route('/police.html')
def police():
    with open('data/crimegroup.txt', 'r') as file:
        crimegroup = [line.strip() for line in file]
    with open('data/unitname.txt', 'r') as file:
        unitname = [line.strip() for line in file]
    with open('data/beatname.txt', 'r') as file:
        beatname = [line.strip() for line in file]

    return render_template('performance.html', crimegroup=crimegroup, unitname=unitname, beatname=beatname)

# Crime home page
@app.route('/crime.html')
def crime():
    with open('data/crimehead.txt', 'r') as file:
        crimehead = [line.strip() for line in file]
    # with open('data/crimesno.txt', 'r') as file:
    #     crimeno = [line.strip() for line in file]
    with open('data/year.txt', 'r') as file:
        year = [line.strip() for line in file]

    return render_template('crime.html',crimehead=crimehead, years=year, crimes=crimehead)

# Crimes Map
@app.route('/crime_map')
def crime_map():
    with open('data/year.txt', 'r') as file:
        year = [line.strip() for line in file]
    with open('data/crimehead.txt', 'r') as file:
        crimehead = [line.strip() for line in file]  
    return render_template('crimemap.html',map_html=crime_maps(crimehead, year, fir))   

# Vulnerable Map
@app.route('/victim_selection', methods=['POST', 'GET'])
def victim_map():
        try:
            crimehead = request.form.get('crimehead')
        except Exception as e:
            return f"Error: {e}"
        # return crimehead
        return render_template('vulnerable_map.html',map_html=vs.generate_top_districts_map(crimehead, fir))

# Crime Hotspots
@app.route('/CrimeHead_selection', methods=['POST', 'GET'])
def crime_hotspots():
    try:
        crimehead = request.form.get('CrimeHead')
        map_html = vs.generate_top_districts_map(crimehead, fir)
        return render_template('vulnerable_map.html', map_html=map_html)
    except Exception as e:
        return f"Error: {e}"

# For analysis
@app.route('/get_FIR')
def get_FIR():
    return send_from_directory('Datasets/FIR_Details_Data.csv')

if __name__ == "__main__":
    app.run(debug=True)