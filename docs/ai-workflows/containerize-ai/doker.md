# Docker Compose

```bash
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama_data:/root/.ollama \
  --restart unless-stopped \
  ollama/ollama
```

## Simple compose

Use this minimal `docker-compose.yml` for a CPU-based setup: [ollama](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)

```yaml
services:
  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped

volumes:
  ollama_data:
```

This matches Ollama’s documented Docker pattern: publish port `11434`, keep model data in `/root/.ollama`, and run the official image. [docs.ollama](https://docs.ollama.com/docker)

## Start and pull a model

Start the container with: [ollama](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)

```bash
docker compose up -d
```

Then download and run a model from inside the container, for example: [ollama](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)

```bash
docker exec -it ollama ollama run llama3.2
```

The first run will pull the model into the mounted volume, so later restarts do not need to download it again. [ollama](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)

## API usage

Once the container is up, Ollama listens on port `11434`, so your local apps can call its REST API at `http://localhost:11434`. [docs.ollama](https://docs.ollama.com/docker)

Example test request: [ollama](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Explain Docker Compose in simple terms."
}'
```

That works well when you want another containerized app, script, or test framework to talk to Ollama over the local API. [ollama](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)

## GPU version

For Linux with NVIDIA GPUs, Ollama’s docs say to install the NVIDIA Container Toolkit and run the container with `--gpus=all`; after configuring Docker for the NVIDIA runtime, you can adapt Compose to request GPU access. [ollama](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)

A practical Compose example is: [dev](https://dev.to/ajeetraina/running-ollama-with-docker-compose-and-gpus-lkn)

```yaml
services:
  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: ["gpu"]

volumes:
  ollama_data:
```

If you are on AMD, Ollama documents using the `ollama/ollama:rocm` image or exposing `/dev/kfd` and `/dev/dri` devices depending on your setup. [ollama](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)

## Notes

On Mac, Ollama’s official guidance says to run the standalone Ollama app outside Docker because Docker Desktop does not provide GPU support there. [docs.ollama](https://docs.ollama.com/docker)

If you want the model to be pulled automatically at startup, add a second helper service or an init script, but for a first setup the manual `docker exec ... ollama run llama3.2` approach is the cleanest. [ollama](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)

A good next step is pairing this with Open WebUI in the same Compose stack so you get a browser chat interface on top of the Ollama API. [github](https://github.com/mythrantic/ollama-docker)