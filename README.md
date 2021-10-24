<img align="right" src="https://img.etimg.com/thumb/msid-83328202,width-650,imgsize-501342,,resizemode-4,quality-100/while-the-mcu-movies-have-touched-upon-lokis-mischievous-side-the-series-loki-marvel-studioss-third-series-at-disney-plus-aims-to-give-an-insight-into-what-hides-beneath-the-wickedness-of-the-fan-favourite-villain-.jpg" width="200">

# `Loki` - Fake services - "I know what this place is. It's an illusion."

## Simulate your services 
You know when you have no way out to solve a problem, one of the best things you can use is **magic**! When you need several services communicating to be able to test a feature, it can be quite complex to prepare all the necessary infrastructure. Another problem is when services that are available in *staging* and *devint* environments do not have cohesive data. There is nothing better than asking the **God of lies Loki** for help and creating a great illusion between the services in a local and simple way.

## Requirements
- Docker
- Docker-compose

## How to use
1. Clone the repository
```bash
git clone git@github.com:thiagonf/Loki.git
```   

2. Run the project
```bash
docker-compose up
```   

3. Access the Swagger documentation
```
http://localhost:81/
```   
## Examples
This project has an example endpoint that returns a fake user and leaves the user's uuid dynamic, always returning the uuid that comes in the request. To add more fake endpoints it is only necessary to add a new method in ```main.py``` and create JSON response in jsons folder.