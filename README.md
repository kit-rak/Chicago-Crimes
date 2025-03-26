# Chicago Crime Data Visualization

## 📌 Project Overview
This project is a **Streamlit-based web application** that provides an interactive visualization of **Chicago crime data**. The app allows users to explore crime trends and view crime distribution across different community areas using an interactive map.

## 🚀 Features
- **Crime Data Exploration:** View crime data from 2001 to present, sourced from the **Chicago Data Portal**.
- **Interactive Map:** Visualize crime density by community areas using **Folium and GeoPandas**.
- **Yearly Crime Trends:** Select a specific year to analyze crime distribution.
- **Dynamic Data Updates:** Automatically fetches the latest crime reports.

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Libraries:** Streamlit, Pandas, GeoPandas, Folium, Streamlit-Folium
- **Data Source:** Chicago Data Portal ([Crimes 2001-Present](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2))

## 📂 File Structure
```
├── app.py                  # Main Streamlit app
├── requirements.txt        # Dependencies
├── chicago-community-areas.geojson # Geospatial data for mapping
├── Chicago_Crimes_YYYY.csv # Crime datasets for selected years
```

## ⚡ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/chicago-crime-analysis.git
cd chicago-crime-analysis
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 📊 How It Works
1. **Select a year** from the sidebar dropdown.
2. **View crime trends and distribution** for the selected year.
3. **Explore an interactive map** displaying crime density across Chicago’s community areas.

## 📬 Contact
- **LinkedIn:** [kit-rak](https://www.linkedin.com/in/kit-rak)
- **GitHub:** [kit-rak](https://github.com/kit-rak)

🚀 **Happy Exploring!**
