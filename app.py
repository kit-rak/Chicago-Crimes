import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import geopandas as gpd

option = st.sidebar.selectbox("Choose an option", ['Home', 'Map'])

if option == 'Home':
    st.title('Chicago Crime Data')
    st.write('This web application provides a visualization of Chicago crime data.')
    st.write('The data is from the Chicago Data Portal and contains information on reported incidents of crime that occurred in the City of Chicago from 2001 to present.')
    st.write('The data is updated daily and covers the following fields:')
    st.write('ID, Case Number, Date, Block, IUCR, Primary Type, Description, Location Description, Arrest, Domestic, Beat, District, Ward, Community Area, FBI Code, X Coordinate, Y Coordinate, Year, Updated On, Latitude, Longitude, Location')
    st.write('The data can be found [here](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)')

if option == 'Map':
    st.title('Chicago Crime Map')
    st.write('This map visualizes the number of crimes in each community area in Chicago.')
    st.write('The data is from the Chicago Data Portal and contains information on reported incidents of crime that occurred in the City of Chicago from 2001 to present.')
    st.write('The data is updated daily and covers the following fields:')
    st.write('ID, Case Number, Date, Block, IUCR, Primary Type, Description, Location Description, Arrest, Domestic, Beat, District, Ward, Community Area, FBI Code, X Coordinate, Y Coordinate, Year, Updated On, Latitude, Longitude, Location')
    st.write('The data can be found [here](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)')
    geo_file = 'chicago-community-areas.geojson'

    df_geo = gpd.read_file(geo_file)
    df_geo.area_num_1 = df_geo.area_num_1.astype(int)
    df_geo.area_numbe = df_geo.area_numbe.astype(int)
        
    year_c = st.selectbox('Choose the year', ['2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004'], placeholder='Choose the year')

    df = pd.read_csv(f"Chicago_Crimes_{year_c}.csv")
    df_area_counts = df[['Year','Community Area']].value_counts().sort_index().reset_index().rename(columns = {0:'Counts', 'Community Area':'area_num_1'})
    df_area_counts['area_num_1'] = df_area_counts['area_num_1'].astype(int)
    df_geo_1 = pd.merge(df_area_counts,df_geo,on = 'area_num_1')
    df_geo_2 = df_geo_1[df_geo_1['Year'] == int(year_c)][['count','geometry']]


    years = df_geo_1['Year'].sort_index().unique()
    location_mean = [df['Latitude'].mean(), df['Longitude'].mean()]

    for year in years:
        map_obj = folium.Map(location=location_mean, zoom_start=10, width=500, height=500)
        
        folium.Choropleth(
            geo_data=df_geo,
            data=df_geo_1[df_geo_1['Year'] == year],
            columns=['community', 'count'],
            key_on='feature.properties.community',
            line_opacity=0.3,
            fill_opacity=0.5,
            fill_color='YlOrRd',
            legend_name=f'Chicago Crime Count by Community - Year: {year}', 
            highlight=True, smooth_factor=2
        ).add_to(map_obj)
        
        folium_static(map_obj)

    