## Twitter Streaming project 
Until now, the idea behind this project is to ingest tweets with Kafka. and use it in analytics afterward.
# TODO List
- [x] Tweets producer that will get a stream of data from twitter 
- [ ] Tweets consumer that will process the data using SparkStreaming and store it in mongodb
# How to launch the project 
- rename the file .env-copy to .env , and fill the variables with your credentials and run the following command that will set the enveromental variables in your machine, these varibles will be used in the docker compose file
   
```properties
source .env
```
- To run the project
```properties
docker compose build 
docker compose up
```
