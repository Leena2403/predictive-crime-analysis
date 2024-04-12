import folium, pandas
from folium.plugins import HeatMap
from shapely.geometry import Point
from folium.plugins import MarkerCluster
import os
import matplotlib.pyplot as plt
import io


## Crime maps based on crime and year selected
def crime_maps(crime_name, year, df):
    global lat_long_dict, fir_short

    df_a_crimes = df[(df['CrimeHead_Name'] == crime_name) & (df['Year'] == year)]

    crime_count_in_year = len(df_a_crimes)

    crime_counts = df_a_crimes['District_Name'].value_counts()

    top_5_districts = crime_counts.head(5).index.tolist()
    df_filtered = df_a_crimes[df_a_crimes['District_Name'].isin(top_5_districts)]

    crimes_map = folium.Map(location=[15.3173, 75.7139], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(crimes_map)

    for index, row in df_filtered.iterrows():
        district_name = row['District_Name']
        latitude, longitude = lat_long_dict[district_name]
        popup = "<br> PS name: " + str(row['UnitName']) + "<br> Beat Name: " + str(
            row['Beat_Name']) + "<br> Date/Time: " + str(row['Offence_From_Date']) + "<br> Address: " + row[
                    'Place of Offence'] + "</p>"
        folium.Marker([latitude, longitude], popup=popup).add_to(marker_cluster)

    # Add text to display crime count in the selected year
    text = f"Total {crime_name} crimes in {year}: {crime_count_in_year}"
    folium.Marker(
        location=[15.5, 75.5],  # Adjust location as needed
        icon=folium.map.Icon(),
        popup=text
    ).add_to(crimes_map)

    return crimes_map.save('templates/crime_map.html')