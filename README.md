# Tests Generation and Type Inference Analisys

## Running the docker container

Run the following to start the docker container:

- `docker compose build`
- `docker compose run --rm app bash`

Inside the container run:
- `pynguin --project-path ./<SUBPROJECT>/<FOLDER> --output-path ./pynguin_tests/<SUBPROJECT>/<FOLDER> --module-name <MODULE>`
