# Setup Guide for YogaGPT Application

This document provides an overview of the available commands in the Makefile, explaining how to build, run, and manage the YogaGPT application.

## Prerequisites

Before running any of the commands, ensure you have the following installed:
- Docker
- Docker Buildx plugin (for multi-platform builds)
- Python 3.9+
- `virtualenv` (for managing Python virtual environments)

## Table of Contents

- [Makefile Targets](#makefile-targets)
  - [Default Goal: `run`](#default-goal-run)
  - [Building the Docker Image](#building-the-docker-image)
    - [`setup`](#setup)
    - [`build`](#build)
    - [`build-and-push`](#build-and-push)
  - [Running the Application](#running-the-application)
    - [`venv`](#venv)
    - [`install`](#install)
    - [`run`](#run)
    - [`docker-run`](#docker-run)
  - [Cleanup](#cleanup)
    - [`clean`](#clean)
    - [`destroy-venv`](#destroy-venv)

---

## Makefile Targets

### Default Goal: `run`

By default, running `make` without specifying a target will run the Python application:

```bash
make
```

This executes the `run` target, which runs the `main.py` Python file of the YogaGPT application.

### Building the Docker Image

#### `setup`

This command ensures that a Docker Buildx builder is created for multi-platform builds. If the builder already exists, it skips the creation.

```bash
make setup
```

This is a prerequisite for building Docker images using Buildx.

#### `build`

Build the Docker image for multiple platforms (e.g., `linux/amd64` and `linux/arm64`):

```bash
make build
```

This will:
- Set up the Docker Buildx builder (if not already set up).
- Build the image specified by `IMAGE_NAME` and `TAG` from the Dockerfile.

#### `build-and-push`

Build and push the Docker image to the container registry:

```bash
make build-and-push
```

This command builds the Docker image for multiple platforms and pushes it to the Docker registry (e.g., Docker Hub). The `IMAGE_NAME` and `TAG` values are used to tag the image in the registry.

### Running the Application

#### `venv`

Create a Python virtual environment and install the required dependencies:

```bash
make venv
```

This will:
- Create a virtual environment using Python 3.9.
- Install the application dependencies from `requirements.txt`.

#### `install`

If the virtual environment is already set up, you can use the `install` target to install the application requirements:

```bash
make install
```

This command installs the dependencies without creating a new virtual environment.

#### `run`

Run the YogaGPT Python application:

```bash
make run
```

This executes the `main.py` script, starting the application.

#### `docker-run`

Run the application using Docker Compose:

```bash
make docker-run
```

This command uses `docker-compose.yml` to run the YogaGPT application in a Docker container. It recreates the container forcefully to ensure any changes are applied.

### Cleanup

#### `clean`

Remove the Buildx builder, the Docker image, and prune unused Docker networks:

```bash
make clean
```

This command performs a cleanup by:
- Removing the multi-platform builder.
- Removing the Docker image.
- Pruning Docker networks that are not being used.

#### `destroy-venv`

Remove the virtual environment:

```bash
make destroy-venv
```

This command deactivates the virtual environment (if active) and deletes the `.venv` directory.

---

## Conclusion

With the provided Makefile, you can easily manage the building, running, and cleanup of your YogaGPT application, both locally and within Docker environments. Follow the steps above to ensure smooth setup and usage of the application.

If you encounter any issues, ensure you have installed all the necessary prerequisites and that your environment variables are correctly set.

