import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_data = data[0] # Get the first country data
        
        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["N/A"])[0]
        population = country_data["population"]
        area = country_data["area"]
        currency = country_data["currencies"]
        region = country_data["region"]
        return name, capital, population, area, currency, region
    else:
        return None

def main():
    st.title("Country Information App")
    country_name = st.text_input("Enter a country name: ")
    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency, region = country_info

            st.subheader("Country Information")
            st.write(f"Name: {name}")
            st.write(f"Capital: {capital}")
            st.write(f"Population: {population}")
            st.write(f"Area: {area} square kilometers")
            st.write(f"Currency: {currency}")
            st.write(f"Region: {region}")
        else:
            st.error("Error: Country data not found.")

if __name__ == "__main__":
    main()

