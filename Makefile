export UID=$(shell id -u)
export GID=$(shell id -g)

down:
	docker compose down

shell:
	docker compose up -d
	docker compose exec workbench bash

logs:
	docker compose logs -f
