## Coin Project Prerequisites

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
