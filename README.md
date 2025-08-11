# CQC Data ETL Pipeline

This project is an Extract, Transform, Load (ETL) pipeline designed to fetch data about care providers in the Oldham area from the Care Quality Commission (CQC) API. The pipeline then transforms this data and loads it into a MySQL database. It's configured to handle both a production environment with the live CQC API and a testing environment that uses a local dummy API to prevent excessive API calls.

---

## Project Structure

-   `etl-pipeline/`: Contains the core ETL logic and utility functions.
    -   `src/main.py`: The entry point for the pipeline.
    -   `etl/`: Contains the `extract.py`, `transform.py`, and `load.py` modules.
    -   `utils/`: Contains `config.py` for managing environment variables and `api_client.py` for API interaction.
-   `mock_api/`: A simple Flask application that serves dummy CQC data for testing purposes.
    -   `dummy_data/`: JSON files containing the mock data.
    -   `dummy_api.py`: The Flask server.
-   `docker-compose.yml`: Defines the services for running the ETL pipeline and the mock API in a Dockerized environment.

---

## Getting Started

### Prerequisites

-   Python 3.x
-   Docker and Docker Compose
-   A MySQL database (local or remote)

### Running the Pipeline (without Docker)

This is the recommended approach for local development and testing.

1.  **Create environment files**:
    You need to create two environment files within the `etl-pipeline/` directory: `.env.test` and `.env.production`.

    **`.env.test`**: For running with the local mock API.

    ```
    DUMMY_API_KEY=
    DUMMY_API_BASE_URL=http://localhost:5000
    DOCKER_MOCK_API_BASE_URL=http://mock_api:5000
    DB_USER=[your_local_db_user]
    DB_PASS=[your_local_db_password]
    DB_NAME=[your_local_db_name]
    DB_UNIX_SOCKET=[your_local_db_unix_socket_path]
    ```

    **`.env.production`**: For running with the live CQC API.

    ```
    CQC_API_KEY=[your_cqc_api_key]
    CQC_BASE_URL=[https://api.service.cqc.org.uk/public/v1](https://api.service.cqc.org.uk/public/v1)
    DB_HOST=[your_production_db_host]
    DB_PORT=[your_production_db_port]
    DB_USER=[your_production_db_user]
    DB_PASS=[your_production_db_password]
    DB_NAME=[your_production_db_name]
    ```

2.  **Set up the mock API**:
    Navigate to the `mock_api/` directory and run the Flask server.
    ```bash
    python dummy_api.py
    ```
    This will start the mock API on `http://localhost:5000`.

3.  **Run the ETL pipeline**:
    With the mock API running, navigate to the `etl-pipeline/src/` directory and execute the main script. The pipeline will use the `.env.test` file by default.
    ```bash
    python main.py
    ```
    The script will fetch data from your local mock API and load it into your local MySQL database.

---

### Running the Pipeline (with Docker)

Docker is used to create an isolated environment for the pipeline and its dependencies.

1.  **Build and run the containers**:
    From the root directory, use Docker Compose to build and start the services. By default, it will use the `test` environment.
    ```bash
    docker-compose up --build
    ```
    This command will spin up two containers: `mock_api` and `etl-pipeline`. The pipeline will automatically fetch data from the `mock_api` container and attempt to connect to the database specified in `.env.test`.

2.  **Running in Production**:
    To run the pipeline against the live CQC API, you need to specify the `production` environment when using Docker Compose. Ensure you have populated your `.env.production` file.

    ```bash
    ENV=production docker-compose up --build
    ```

    *Note: The `mock_api` service will still be started but will not be used by the ETL pipeline in this configuration.*
