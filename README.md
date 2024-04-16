
# Searchland Task 1 Take Home



## Running The Project Locally
### Requirements:
- Python version 3.12.2
### Steps:
1. Clone the following repository:
    ```sh
    git clone https://github.com/dagster-io/dagster-quickstart

    cd dagster-quickstart
    ```
2. Clone the following repository:
    ```sh
    git clone https://github.com/dagster-io/dagster-quickstart

    cd dagster-quickstart
    ```

3. Install the required dependencies.

    Here we are using `-e`, for ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs), so that when Dagster code is modified, the changes automatically apply. 

    ```sh
    pip install -e ".[dev]"
    ```

4. Run the project!

    ```sh
    dagster dev
    ```

## Changed files:
- dagster_quickstart/assets.py
- dagster_quickstart/configurations.py
- added /tmp folder
- This README.md file
- setup.py