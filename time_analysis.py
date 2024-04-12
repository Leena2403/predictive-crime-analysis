import pandas as pd
import folium
from folium.plugins import MarkerCluster

fir = pd.read_csv('Datasets/FIR_Details_Data.csv')

lat_long_dict = {
    'Bagalkot': (16.1850, 75.700),
    'Ballari': (15.1394, 76.9214),
    'Belagavi City': (15.8497, 74.4977),
    'Belagavi Dist': (16.1681, 74.7805),
    'Bengaluru City': (12.9716, 77.5946),
    'Bengaluru Dist': (12.58207912, 77.34503148),
    'Bidar': (17.9104, 77.5199),
    'Chamarajanagar': (11.9261, 76.9437),
    'Chickballapura': (13.4355, 77.7315),
    'Chikkamagaluru': (13.3161, 75.7720),
    'Chitradurga': (14.2251, 76.3980),
    'CID': (12.9814, 77.5855),
    'Coastal Security Police': (14.830648, 74.126346),
    'Dakshina Kannada': (12.8438, 75.2479),
    'Davanagere': (14.4644, 75.9218),
    'Dharwad': (15.4589, 75.0078),
    'Gadag': (15.4315, 75.6355),
    'Hassan': (13.0033, 76.1004),
    'Haveri': (14.7951, 75.3991),
    'Hubballi Dharwad City': (15.3647, 75.1240),
    'ISD Bengaluru': (12.9688, 77.6160),
    'K.G.F': (12.9585, 78.2710),
    'Kalaburagi': (17.3297, 76.8343)
}

def year_wise_map(year, df):
    global lat_long_dict, fir
    df_a_crimes = df[df['Year'] == year]

    crime_counts = df_a_crimes['District_Name'].value_counts()

    top_5_districts = crime_counts.head(5).index.tolist()
    df_filtered = df_a_crimes[df_a_crimes['District_Name'].isin(top_5_districts)]

    crimes_map = folium.Map(location=[15.3173, 75.7139], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(crimes_map)

    for index, row in df_filtered.iterrows():
        district_name = row['District_Name']
        latitude, longitude = lat_long_dict[district_name]
        popup = "<br> PS name: " + str(row['UnitName']) + "<br> Beat Name: " + str(row['Beat_Name']) + "<br> Date/Time: " + str(row['Offence_From_Date']) + "<br> Address: " + row['Place of Offence'] + "</p>"
        folium.Marker([latitude, longitude], popup=popup).add_to(marker_cluster)

    # crimes_map.save(f'{year}.html')

    return crimes_map.save('templates/timemap.html')