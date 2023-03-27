.DEFAULT_GOAL := build

build:
	docker build -t starwars-app .
.PHONY: build

run:
	docker run --init -p 3000:3000 -d --name starwars-api starwars-app
.PHONY: run
