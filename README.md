# AWS lambda with Docker

Lambda is the _serverless_ service provider by AWS. It has various
advantages over vanilla server deployments, but sometimes can be quite tricky.

Lambdas are just _functions_, pieces of code.

This repo contains an example on how to use Docker to create a lambda function
containing a Fast API application.

## Ways of lambda

There are 2 ways to deploy our code.

### Zip file

Compress our application and __all its dependencies__ into a zip file and
upload it to the lambda function. If the file is too big, we will need to
upload it to an S3 bucket, and then make the lambda read from there.


__pros__

- easy and quick

__cons__

- main one: lambda weight limits. This limit is about 260MB for the lambda and
its layers (if they are)
- hard to keep track of the changes
- hard to zip the python dependencies in a way that lambda will understand

### Docker image

Build a docker image with what we need and upload it to an ECR (Elastic Container
Registry, a repo of images), then make the lambda read from there.

__pros__

- robust, replicable environment. We can leverage docker for deployment and
be sure that the code will run in the lambda.
- we can track the versions of the images through tags.
- the size limit is way above (10 GBs) which for data applications is really
good.
- way easier to install dependencies.
- we can easily reproduce the lambda behavior locally.

__cons__

- well, you need to know docker. It is not super hard but takes more than
`zip -r file.zip app/`.
- cold start? Not sure if using an image will impact the response time from
lambdas


## How to dockerize it

Build the image

```
docker build -t IMAGE_NAME . 
```

Run the image. This will create and start a container based on this image

```
docker run --name CONTAINER_NAME --publish HOST_PORT:8080 -d IMAGE_NAME
```

It is a good practice to give the container a name, so we can easily locate it
later. We can use whichever port we want from our host to bind it to the 8080,
as long as it is not already in use. The `-d` flag will make the cotnainer
start in detatched mode. We won't see its outputs.

Complete example

```
docker build -t lambda-docker
docker run --name lambda-container --publish 8000:8080 -d lamda-docker
```

We could see the logs with
```
docker logs CONTAINER_NAME
```

## How to invoke it

We can run `./invoke.sh` to run `cURL` commands against the deployed endpoint.
This script reads from the dir `data/` the data it sends to the endpoint.
You might need to make them executable.

Another option would be to use the Python `requests` module. This can be done
using the `./invoke.py` file.

## Next steps

We would need to:

1. Create a registry for this image on AWS (ECR Service).
2. Tag this image so it can be pushed to that ECR.
3. Create a lambda function based on this image.
4. Crete an API Gateway to make the API accessible from the internet.
