# Request Infomer

### Webhook definition

In order to accept request requests from the request informer systems,
you need to define a POST endpoint which accepts a MessageLog object,
every 200 type response will be considered as successfull every other will
be considered as an error.


### Set webhook

To set the webhook you must set the field on the hash:


- KEY = system-webhook:{system-id}

you can set the incoming/outgoing fields based on the message log origin


### Systems IDS

- 1 -> Whatsapp Manager
- 2 -> Request Informer
- 3 -> Whatsapp Workflow
- 4 -> META API
- 5 -> Request Classificator