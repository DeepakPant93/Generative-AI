import os

import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Initialize Chroma DB client
client = chromadb.HttpClient(
    host="localhost",
    port=8000,
    settings=Settings(
        chroma_client_auth_provider="chromadb.auth.basic_authn.BasicAuthClientProvider",
        chroma_client_auth_credentials=os.getenv("CHROMA_CLIENT_AUTH_CREDENTIALS")
    )
)

# Create a collection in Chroma DB
# client.delete_collection(name="my_collection")
collection = client.create_collection(name="my_collection")

# Insert some sample data
data = {"ids": ["1", "2", "3", "4"],
        "text": ["The Eiffel Tower is in Paris.", "The Colosseum is in Rome.", "The Great Wall is in China.",
                 "The Taj Mahal is in Agra."],
        "metadata": [{"city": "Paris"}, {"city": "Rome"}, {"city": "China"}, {"city": "Agra"}]}

# Generate embeddings for the data
collection.add(ids=data.get("ids"), documents=data.get("text"), metadatas=data.get("metadata"))

print("Data inserted into Chroma DB.")

# Perform a search
query = "Where is the Eiffel Tower?"
results = collection.query(query_texts=[query], n_results=3)

# Display search results
print("Search results:")
print(results)

# Close the Chroma DB client
client.delete_collection(name="my_collection")
