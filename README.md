# Tests Generation and Python Types Analisys

## Running the docker container

Build the docker container:

- Build the image: `docker build . -t pynguin_runner`
- Run Pynguin to your code:

```bash
docker run --rm \
  -v /path/to/your/code:/code \
  -it pynguin_runner \
  --module-name <module name>
```
