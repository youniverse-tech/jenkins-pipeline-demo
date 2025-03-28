terraform {
  required_providers {
    docker = {                         
      source  = "kreuzwerker/docker"    
      version = "~> 3.0.2"              
    }
  }
}

provider "docker" {}  

# -------------------- Docker Image Resource --------------------
resource "docker_image" "nginx" {
  name         = var.image_name    
  keep_locally = false             
}

# -------------------- Docker Container Resource (With Scaling) --------------------
resource "docker_container" "nginx" {
  count = var.num_containers  

  image = docker_image.nginx.image_id  
  name  = "${var.container_name}-${count.index}"  # Unique names

  # Mapping unique ports: 8081, 8082, ...
  ports {
    internal = 80
    external = 8081 + count.index  
  }

  restart = "always"  

  env = [
    "ENV=production"  
  ]
}
