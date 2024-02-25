terraform {
  required_providers {
    github = {
      source = "integrations/github",
      version = "~> 5.0"
    }
  }
}
provider "github" {
  # token = "latest"
}

resource "github_repository" "new_repo" {
  name = "Important"
  description = "my awsome"
  visibility = "public"

}

output "name" {
  value = github_repository.new_repo.id
}