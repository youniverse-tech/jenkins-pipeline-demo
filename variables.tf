variable "container_name" {
  description = "Name of the Docker container"
  type        = string
  default     = "my-nginx-container"
}

variable "image_name" {
  description = "Docker image to use"
  type        = string
  default     = "nginx:latest"
}
