import streamlit as st
import requests

BRAVE_API_ENDPOINT = "https://api.search.brave.com/news"

def brave_search(api_key, query):
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "api.search.brave.com"
    }
    params = {"q": query}
    response = requests.get(BRAVE_API_ENDPOINT, headers=headers, params=params)
    
    if response.status_code != 200:
        st.error(f"Error {response.status_code}: {response.text}")
        return None

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        st.error("Failed to decode the response from the server. The response might not be in JSON format.")
        st.text(response.text)
        return None

st.title("Brave Search Interface")

# Input for API Key
api_key = st.text_input("Enter your Brave API key:", type="password")

# Input for Search Query
search_query = st.text_input("Enter your search query:")

if st.button("Search") and api_key:
    results = brave_search(api_key, search_query)
    if results and 'data' in results:
        for article in results['data']:
            st.markdown(f"### [{article['title']}]({article['url']})")
            st.markdown(article['description'])
            st.write("---")

