## Coin Project Prerequisites
## Running the Project with Docker Compose

This project includes a `docker-compose.yaml` file to simplify the setup and deployment process. Follow the steps below to run the project using Docker Compose.

### Prerequisites

- Ensure you have Docker and Docker Compose installed on your machine. You can download and install Docker from [Docker's official website](https://www.docker.com/get-started).

### Steps to Run the Project

1. **Navigate to the Project Directory**:

    Open a terminal and navigate to the root directory of the project where the `docker-compose.yaml` file is located.

    ```bash
    cd /path/to/your/project
    ```

2. **Create the Containers**:

    Use the following command to create the containers defined in the `docker-compose.yaml` file without starting them immediately.

    ```bash
    docker compose create
    ```

    This command will prepare the containers based on the configuration but will not start them yet.

3. **Manually Start the Containers in the Correct Order**:

    Start the containers manually in the following order to ensure proper initialization:

    - **Start Zookeeper**:

        ```bash
        docker compose start zookeeper
        ```

    - **Start Kafka**:

        ```bash
        docker compose start kafka
        ```

    - **Start Kafdrop**:

        ```bash
        docker compose start kafdrop
        ```

    - **Start PostgreSQL**:

        ```bash
        docker compose start postgres
        ```

    - **Start Dev-Env**:

        ```bash
        docker compose start dev-env
        ```

    - **Start Elasticsearch**:

        ```bash
        docker compose start elasticsearch
        ```

    - **Start Kibana**:

        ```bash
        docker compose start kibana
        ```

4. **Verify the Containers are Running**:

    Check that the containers are up and running by listing all running containers:

    ```bash
    docker ps
    ```

    You should see the containers listed and their status as `Up`.

5. **Access the Services**:

    Depending on the services defined in your `docker-compose.yaml`, you can now access them via their respective ports. For example:
    - If you have a web application, you can visit `http://localhost:PORT` in your browser.
    - If you have a database service, you can connect to it using the defined ports in your `docker-compose.yaml`.

6. **Shut Down the Containers**:

    When you're done, you can stop and remove the containers with the following command:

    ```bash
    docker compose down
    ```

### Customization

If you need to customize the configuration, you can modify the `docker-compose.yaml` file to suit your specific requirements. Be sure to recreate the containers after making any changes:

```bash
docker compose down
docker compose create

Before starting the `coin_project`, make sure to follow these steps:

1. **Download PostgreSQL JDBC Driver**:
    - Download the PostgreSQL JDBC driver from the following link:
      [postgresql-42.5.6.jar](https://jdbc.postgresql.org/download/postgresql-42.5.6.jar)
    - Place the downloaded driver in the `/opt/driver` directory within the `dev-env` container.

    ```bash
    # Example command to copy the driver into the container
    docker cp postgresql-42.5.6.jar dev-env:/opt/driver/
    ```

2. **Create the Target Table in PostgreSQL**:
    - Log in to the PostgreSQL instance using DBeaver with a PostgreSQL connection or via the command line interface (CLI).

    - If using Docker, access the PostgreSQL container:

    ```bash
    docker exec -it -u 0 postgres bash
    ```

    - Connect to PostgreSQL using the `psql` command:

    ```bash
    psql -h localhost -p 5432 -U postgres -d postgres
    ```

    - Create the target table `crypto_data` by running the following SQL command:

    ```sql
    CREATE TABLE crypto_data (
        currency VARCHAR(50),
        dates DATE,
        price DOUBLE PRECISION,
        volume DOUBLE PRECISION,
        market_cap DOUBLE PRECISION
    );
    ```

Once these steps are completed, you can proceed with the next steps in the `coin_project`.
