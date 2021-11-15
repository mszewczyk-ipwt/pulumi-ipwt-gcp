from pulumi_ipwt_gcp.monitoring.v3 import UptimeCheckConfig
from pulumi_ipwt_gcp.monitoring.v3 import AlertPolicy

from pulumi import ResourceOptions

uck = UptimeCheckConfig(
  'uptime-check-config-pulumi-resource',
  displayName='search-api-checker',
  monitoredResource=UptimeCheckConfig.MonitoredResource(
    type='uptime_url',
    labels=dict(
      host='search.dev.affiliate-partners.360codelab.com',
    ),
  ),
  httpCheck=UptimeCheckConfig.HttpCheck(
    requestMethod='GET',
    path='/',
    port='443'
  ),
  project='affiliate-partners-dev',
)

alert_policy = AlertPolicy(
  'alert-policy-pulumi-resource',
  combiner=AlertPolicy.ConditionCombinerType.OR,
  alertStrategy=AlertPolicy.AlertStrategy(
    notificationRateLimit=AlertPolicy.NotificationRateLimit(
      period='300s'
    ),
  ),
  conditions=[
    AlertPolicy.Condition(
      displayName="Log match condition",
      conditionMatchedLog=AlertPolicy.LogMatch(
        filter='resource.type="cloud_function" severity>=ERROR'
      ),
    ),
  ],
  displayName='Cloud Functions Errors',
  enabled=True,
  project='affiliate-partners-dev',
)