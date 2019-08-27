from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase
import json
import datetime

class MonitisWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        context = payload['data']['alert']

        # Load variables from querystring
        try:
            environment = query_string['environment']
        except:
            environment = 'Monitis'
        try:
            severity = query_string['severity']
        except:
            severity = 'major'
        if context['alertType'] == 'RECOVERY':
            severity = 'ok'

        return Alert(
            resource=context['url'],
            type=context['type']',
            event=context['name'].context['adddata'],
            environment=environment,
            severity=severity,
            service=[context['url']],
            group=context['group'],
            text=context['alertId'],
            tags=[context['type']],
            attributes={},
            origin='Monitis',
            raw_data=json.dumps(payload, indent=4)
        )