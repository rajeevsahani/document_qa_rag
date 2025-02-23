import streamlit as st
import requests

API_BASE_URL = "http://192.168.2.227:8000"

st.title("Document Management & RAG-based Q&A")

# File Upload Section
st.header("Upload a Document")
uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx", "ppt", "pptx"])

if uploaded_file is not None:
    # Prepare the file to be sent with both the file content and filename
    files = {
        "file": (uploaded_file.name, uploaded_file, uploaded_file.type)  # Tuple with filename
    }

    # Send POST request to FastAPI endpoint
    response = requests.post(f"{API_BASE_URL}/upload/", files=files)
    
    if response.status_code == 200:
        st.success("File uploaded successfully!")
        st.json(response.json())  # Display response
    else:
        st.error(f"Failed to upload file. Error: {response.text}")


# Document Selection Section
st.header("Available Documents")
docs_response = requests.get(f"{API_BASE_URL}/documents/")
if docs_response.status_code == 200:
    documents = docs_response.json()
    doc_options = {doc["id"]: doc["filename"] for doc in documents}
    selected_docs = st.multiselect("Select documents to query from", options=doc_options.keys(), format_func=lambda x: doc_options[x])
else:
    st.error("Failed to fetch documents.")

# Header for Query Section
st.header("Ask a Question")
query = st.text_input("Enter your question")

# If the user presses the "Search" button
if st.button("Search"):
    if query:
        # Make sure to send the query as a POST request with the correct payload
        query_response = requests.post(f"{API_BASE_URL}/query/", json={"query": query})

        # If the request was successful, display the results
        if query_response.status_code == 200:
            results = query_response.json().get("results", [])
            if results:
                st.subheader("Results:")
                for result in results:
                    st.write(f"**Filename**: {result['filename']}")
                    st.write(f"**Content**: {result['content']}")
            else:
                st.warning("No results found.")
        else:
            st.error("Failed to retrieve results.")
    else:
        st.warning("Please enter a query.")
