import requests
import streamlit as st

# Function to fetch product data from MercadoLibre API
def get_products(query):
    url = f"https://api.mercadolibre.com/sites/MLA/search?q={query}"
    response = requests.get(url)
    data = response.json()
    return data.get("results", [])

# Streamlit UI
def main():
    st.title("MercadoLibre Product Search")

    # Search field for querying the API
    api_query = st.text_input("Enter API search term:", "smartwatch")

    # Fetch and display product data
    products = get_products(api_query)
    st.write(f"Found {len(products)} products")

    # Search field for filtering the displayed table
    table_search_term = st.text_input("Filter results by name:", "")

    # Display table with search functionality
    table_width = st.slider("Adjust Table Width", min_value=200, max_value=1200, value=800)
    filtered_products = [product for product in products if table_search_term.lower() in product.get("title", "").lower()]
    st.table(filtered_products).set_frame_width(table_width)

if __name__ == "__main__":
    main()
