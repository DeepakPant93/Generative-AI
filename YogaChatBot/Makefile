# Set the default target
.DEFAULT_GOAL := run

# Variables
IMAGE_NAME = deepak93p/yoga-chatbot
TAG = latest
PLATFORMS = linux/amd64,linux/arm64
DOCKERFILE = Dockerfile
BUILD_DIR = .

# Default target
.PHONY: all
all: build

# Create and use buildx builder (if not already created)
.PHONY: setup
setup:
	@docker buildx create --name multiarch-builder --use || echo "Builder already exists"

# Build the Docker image for multiple platforms
.PHONY: build
build: setup
	@docker buildx build --platform $(PLATFORMS) -t $(IMAGE_NAME):$(TAG) -f $(DOCKERFILE) $(BUILD_DIR)

# Build and push the image to the registry
.PHONY: build-and-push
build-and-push: setup
	@docker buildx build --platform $(PLATFORMS) -t $(IMAGE_NAME):$(TAG) -f $(DOCKERFILE) $(BUILD_DIR) --push

# Clean up the buildx builder
.PHONY: clean
clean:
	@docker buildx rm multiarch-builder || echo "No builder to remove"
	docker rmi $(IMAGE_NAME):$(TAG)
	docker network prune -f

# Setup for virtual environment and install the application requirements
.PHONY: venv
venv:
	virtualenv -p python3.9 .venv
	sleep 5
	source .venv/bin/activate
	pip install -r requirements.txt

# Install the application requirements
.PHONY: install
install:
	pip install -r requirements.txt

# Destroy the virtual environment
.PHONY: destroy-venv
destroy-venv:
	deactivate
	rm -rf .venv

# Run the Emailer_Worker application
.PHONY: run
run:
	  streamlit run main.py --server.port 8502

# Run the Emailer_Worker application within a Docker container
.PHONY: docker-run
docker-run:
	docker-compose -f docker-compose.yml up -d --force-recreate
