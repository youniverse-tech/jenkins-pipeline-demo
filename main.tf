terraform {
  required_providers {
    docker = {                         # Defining the provider for Docker
      source  = "kreuzwerker/docker"    # This tells Terraform to use the Docker plugin
      version = "~> 3.0.2"              # The version constraint (ensures compatibility)
    }
  }
}

provider "docker" {}  # This initializes the Docker provider so Terraform can interact with Docker

# -------------------- Docker Image Resource --------------------
resource "docker_image" "nginx" {
  name         = var.image_name    # Pulls the Docker image from variables.tf
  keep_locally = false             # This ensures the image isn't stored locally after deployment
}

# -------------------- Docker Container Resource --------------------
resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id  # Uses the image ID from docker_image above
  name  = var.container_name           # Fetches container name from variables.tf

  # Mapping port 8081 (host) to 80 (container)
  ports {
    internal = 80
    external = 8081
  }

  # ✅ Fix: Moved inside the container resource block
  restart = "always"  # Restart policy: Always restart unless manually stopped

  env = [
    "ENV=production"  # Example environment variable (can be modified later)
  ]
}
