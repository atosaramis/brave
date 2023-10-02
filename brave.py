# Import necessary libraries
import streamlit as st
import requests

# Define the main function for the Streamlit app
def main():
    st.title("Brave Search API Explorer")

    # Input for API Key
    api_key = st.text_input("Enter your Brave Search API Key:", type="password")

    # Input for search term
    search_term = st.text_input("Enter your search term:")

    # Button to trigger the search
    if st.button("Search"):
        if not api_key or not search_term:
            st.warning("Please provide both API Key and Search Term.")
            return

        # Hypothetical API endpoint for Brave Search
        url = "https://api.bravesearch.com/search"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "query": search_term
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()
            # Displaying the results in markdown format
            st.markdown("## Results")
            for result in data.get("results", []):
                st.markdown(f"### {result['title']}")
                st.markdown(result['description'])
                st.markdown(f"[Read more]({result['url']})")
                st.write("---")
        else:
            st.error("Failed to fetch results. Please check your API key and try again.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
