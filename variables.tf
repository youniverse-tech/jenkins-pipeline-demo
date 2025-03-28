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

variable "num_containers" {
  description = "Number of containers to scale"
  type        = number
  default     = 1  # Default is 1, can be overridden in command
}
