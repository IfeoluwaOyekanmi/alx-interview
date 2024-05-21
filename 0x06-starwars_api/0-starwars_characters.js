#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

function fetch (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, res, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function getMovieCharacters () {
  try {
    const characters = [];
    const movieData = await fetch(movieUrl);
    for (const url of movieData.characters) {
      const characterData = await fetch(url);
      characters.push(characterData.name);
    }
    characters.forEach(element => {
      console.log(element);
    });
  } catch (error) {
    console.error(error);
  }
}

getMovieCharacters();
