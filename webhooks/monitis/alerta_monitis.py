from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase
import json

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

        create_time = parse_date(context['timestamp'])

        return Alert(
            resource=context['url'],
            event=context['name'].context['adddata'],
            environment=environment,
            severity=severity,
            service=[context['url']],
            group=context['group'],
            value='',
            text=context['alertId'],
            tags=[context['type']],
            attributes={},
            origin='Monitis',
            type=context['type'],
            create_time=create_time,
            raw_data=json.dumps(payload, indent=4)
        )