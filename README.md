# SMS Alert Service

## About

A simple service for sending SMS Alerts using Twilio's SMS API

## Starting the service

First check if the port specified in the start.sh is free, by running the following command:

```bash
sudo nc localhost 8080 < /dev/null; echo $?
```

If the port is not free, choose another port and add it to the start.sh. Then, create the Docker image and build a container

```bash
sudo bash start.sh
```

## Updating the service

For any changes made after you've built the container to take effect, you will need to stop and restart the Docker container. Run the following command to rebuild the container:

```bash
sudo docker stop alert-api && sudo docker start alert-api

```

## Request & response structure

The API primarily consumes and returns JSON. All calls must be accompanied by a JSON payload and a Content-type=application/json header. Below is a summary of the verb(s) the API recognises.

| Verb        | Interpretation                    | Expected responses |
| ------------| ----------------------------------|--------------------|
| POST        | Send notification/ alert          |200 - OK            |

Failed requests are flagged by 4XX status codes. Errors in this range generally have a response body of the following structure:

```json
{
    "status": "error",
    "error": "error message"
}
```

## Endpoint

| Endpoint    | HTTP Method                       | Description        |
| ------------| ----------------------------------|--------------------|
|/v1/sms/send | POST                              |Sends SMS alert     |

## Sample Payload

For sender you can use alphanumeric sender ID or the normal phone number (e.g. +265999111222). You can find out which countries support alphanumeric sender IDs on [https://support.twilio.com/hc/en-us/articles/223133767-International-support-for-Alphanumeric-Sender-ID]

```json
{
    "recipient": "+265111222333",
    "body": "Hello from Kyryo!",
    "sender": "Kyryo"
}

```
