# Request Infomer

### Webhook definition

In order to accept request requests from the request informer systems,
you need to define a POST endpoint which accepts a MessageLog object,
every 200 type response will be considered as successfull every other will
be considered as an error.


### Set webhook

To set the webhook you must set the path on a Redis key called:

- KEY = system-webhook:{system-id}
- VALUE = https://api.pescarauto.cl/systemxyz/webhook

