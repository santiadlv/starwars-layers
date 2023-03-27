# Star Wars API App

Run project with `makefile`

    make build

And run Docker image with `makefile`
    
    make run

You need to have Docker up for this to work.

## Project requirements

1. Endpoint `GET /` list the Star wars movies.
   * Sort them by ID in ascending order.

2. Create a new Endpoint to list all character names from a movie.
   * You pass an ID as a URL parameter.

## Usage

- Visit [http://localhost:3000/](http://localhost:3000/) to get a list with the Star Wars movies, sorted by their respective ID.
- Visit [http://localhost:3000/characters?id=1](http://localhost:3000/characters?id=1) to get the character list of each movie by ID. This query parameter can be changed and goes from 1-6.