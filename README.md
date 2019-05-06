# Luxembot

"Is that in Germany?"

Every American of Luxembourgian ancestry knows the pain of having to explain that Luxembourg is indeed a country in Europe (not a city) that has its own unique history and culture. Luxembot is a simple twitterbot that is designed to solve the problem of general ignorance about Luxembourg.

It was mainly conceived of as a way to become familiar with Docker and containers, and to get more experience using Twitter's REST API.

https://twitter.com/luxembot

## Docker

To run the bot in it's own Docker container, navigate to the directory where it was saved and build the image using the Dockerfile with the following command:

```
docker build .
```

Then the build is successfully completed copy the image ID and start the bot using:

```
docker run <image id>
```

Note that a registered Twitter developer account and credentials are required.
