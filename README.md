# Alert API
## About
Service that handles notifications for Kyryo products
## Starting the service
Check if a port is free, by running the following command:
```
sudo nc localhost 56733 < /dev/null; echo $?
```
If the port is not free, choose another port and add it to the Dockerfile.
Create the Docker image and build a container
```
sudo bash start.sh
```
## Manually updating the service
In order for these changes to take effect, you will need to stop and restart the Docker containers. 
Run the following command to rebuild the container:
```
sudo docker stop kyryo-notification-service && sudo docker start kyryo-notification-service
```
## Request & response structure
The API primarily consumes and returns JSON. It makes use of a number of HTTP verbs for manipulating and access resources. All calls must be accompanied by a JSON payload and a Content-type=application/json header. Below is a summary of the verbs the API recognises.

| Verb        | Interpretation                    | Expected responses |
| ------------| ----------------------------------|--------------------|
| POST        | Send notification/ alert          |200 - OK            |

Failed requests are flagged by 4XX status codes. Errors in this range generally have a response body of the following structure:
```
{
    "status": "error",
    "error": "error message"
}
```

## Sample Payload
```
{
    "tenant_id": "12345",
    "recipient": "+265111222333",
    "message": "Hello from Kyryo!",
    "app": "ART",
    "brand_name": "EGPAF"
}
```