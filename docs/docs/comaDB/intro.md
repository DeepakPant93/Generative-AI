# Chroma DB Python Application

This is a Python-based application that demonstrates how to insert data into Chroma DB (a vector database) and perform search queries. The project utilizes Docker Compose to deploy Chroma DB locally for easy setup and usage. It showcases how Chroma DB can efficiently store and search vector embeddings.

### Features:
1. **Data Insertion:** Insert vectorized data into Chroma DB.
2. **Vector Search:** Perform searches based on vector similarities.
3. **Docker Deployment:** Easily run Chroma DB using Docker Compose.

### Prerequisites:
1. **Docker & Docker Compose:** Install Docker and Docker Compose on your machine.
2. **Python 3.10+**: Ensure Python is installed.
3. **pip**: For Python package management.

### Setup Instructions:

1. **Install the required Python libraries:**

   Install dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

2. **Start Chroma DB with Docker:**

   Use Docker Compose to set up Chroma DB locally:

   ```bash
   docker compose up -d
   ```

   This will pull the Chroma DB image and run the service locally.

3. **Run the Application:**

   Execute the `app.py` script to insert data and perform a search:

   ```bash
   python app.py
   ```

### Folder Structure:

```bash
.
├── docker-compose.yml    # Docker Compose file for Chroma DB setup
├── app.py                # Python script for inserting data and performing search queries
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

### Docker Compose Setup:

A `docker-compose.yml` file is used to run the Chroma DB service. You can start the service by running `docker-compose up` from the terminal in the project directory. For further guidance on Docker deployment, refer to the official documentation.

- **Docker Deployment Documentation**: https://docs.trychroma.com/deployment/docker

### Additional Resources:

- **Chroma DB Documentation**: Learn more about Chroma DB and its features: https://docs.trychroma.com/
- **Reference Video**: Watch this video to get an overview of Chroma DB deployment: https://www.youtube.com/watch?v=QSW2L8dkaZk