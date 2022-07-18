from django.http import HttpResponse


class StripeWH_handler:
    """ handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)