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
    
    # Check if the response status is not 200 OK
    if response.status_code != 200:
        st.error(f"Error {response.status_code}: {response.text}")
        return None

    # Check if the response content type is not JSON
    if 'application/json' not in response.headers.get('Content-Type', ''):
        st.error("The response from the server is not in JSON format.")
        st.text(response.text)
        return None

    # Try to parse the response as JSON and handle any JSONDecodeError
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        st.error("Failed to decode the response from the server. The response might not be in JSON format.")
        st.text(response.text)
        return None

st.title("Brave Search Interface")

# Input for API Key at the top of the page
api_key = st.text_input("Enter your Brave API key:", type="password")

# Input for Search Query without a default value
search_query = st.text_input("Enter your search query:")

if st.button("Search") and api_key:
    results = brave_search(api_key, search_query)
    if results and 'data' in results:
        for article in results['data']:
            st.markdown(f"### [{article['title']}]({article['url']})")
            st.markdown(article['description'])
            st.write("---")
