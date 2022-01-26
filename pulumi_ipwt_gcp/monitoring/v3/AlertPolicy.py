from pulumi import Output
from pulumi.dynamic import Resource
from pulumi.dynamic import ResourceProvider

from pulumi_ipwt_gcp.helpers import _DictExt
from pulumi_ipwt_gcp.helpers import _GcpSession

from enum import EnumMeta

class AlertPolicy(Resource, module='IPWT-gcp', name='monitoring/v3/AlertPolicy'):
  '''
  https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies
  '''

  class Args(_DictExt):
    def __init__(self,
      name=None,
      displayName=None,
      documentation=None,
      userLabels=None,
      conditions=None,
      combiner=None,
      enabled=None,
      validity=None,
      notificationChannels=None,
      creationRecord=None,
      mutationRecord=None,
      alertStrategy=None,
      **kwargs
    ):
      kwargs = None
      super().update_locals(locals())

  class Documentation(_DictExt):
    def __init__(self,
      content=None,
      mimeType=None,
    ):
      super().update_locals(locals())

  class Condition(_DictExt):
    def __init__(self,
      name=None,
      displayName=None,
      conditionThreshold=None,
      conditionAbsent=None,
      conditionMatchedLog=None,
      conditionMonitoringQueryLanguage=None,
    ):
      super().update_locals(locals())

  class MetricThreshold(_DictExt):
    def __init__(self,
      filter=None,
      aggregations=None,
      denominatorFilter=None,
      comparison=None,
      thresholdValue=None,
      duration=None,
      trigger=None,
    ):
      super().update_locals(locals())

  class Aggregation(_DictExt):
    def __init__(self,
      alignmentPeriod=None,
      perSeriesAligner=None,
      crossSeriesReducer=None,
      groupByFields=None,
    ):
      super().update_locals(locals())

  class Aligner(EnumMeta):
    ALIGN_NONE='ALIGN_NONE'
    ALIGN_DELTA='ALIGN_DELTA'
    ALIGN_RATE='ALIGN_RATE'
    ALIGN_INTERPOLATE='ALIGN_INTERPOLATE'
    ALIGN_NEXT_OLDER='ALIGN_NEXT_OLDER'
    ALIGN_MIN='ALIGN_MIN'
    ALIGN_MAX='ALIGN_MAX'
    ALIGN_MEAN='ALIGN_MEAN'
    ALIGN_COUNT='ALIGN_COUNT'
    ALIGN_SUM='ALIGN_SUM'
    ALIGN_STDDEV='ALIGN_STDDEV'
    ALIGN_COUNT_TRUE='ALIGN_COUNT_TRUE'
    ALIGN_COUNT_FALSE='ALIGN_COUNT_FALSE'
    ALIGN_FRACTION_TRUE='ALIGN_FRACTION_TRUE'
    ALIGN_PERCENTILE_99='ALIGN_PERCENTILE_99'
    ALIGN_PERCENTILE_95='ALIGN_PERCENTILE_95'
    ALIGN_PERCENTILE_50='ALIGN_PERCENTILE_50'
    ALIGN_PERCENTILE_05='ALIGN_PERCENTILE_05'
    ALIGN_PERCENT_CHANGE='ALIGN_PERCENT_CHANGE'

  class Reducer(EnumMeta):
    REDUCE_NONE='REDUCE_NONE'
    REDUCE_MEAN='REDUCE_MEAN'
    REDUCE_MIN='REDUCE_MIN'
    REDUCE_MAX='REDUCE_MAX'
    REDUCE_SUM='REDUCE_SUM'
    REDUCE_STDDEV='REDUCE_STDDEV'
    REDUCE_COUNT='REDUCE_COUNT'
    REDUCE_COUNT_TRUE='REDUCE_COUNT_TRUE'
    REDUCE_COUNT_FALSE='REDUCE_COUNT_FALSE'
    REDUCE_FRACTION_TRUE='REDUCE_FRACTION_TRUE'
    REDUCE_PERCENTILE_99='REDUCE_PERCENTILE_99'
    REDUCE_PERCENTILE_95='REDUCE_PERCENTILE_95'
    REDUCE_PERCENTILE_50='REDUCE_PERCENTILE_50'
    REDUCE_PERCENTILE_05='REDUCE_PERCENTILE_05'

  class ComparisonType(EnumMeta):
    COMPARISON_UNSPECIFIED='COMPARISON_UNSPECIFIED'
    COMPARISON_GT='COMPARISON_GT'
    COMPARISON_GE='COMPARISON_GE'
    COMPARISON_LT='COMPARISON_LT'
    COMPARISON_LE='COMPARISON_LE'
    COMPARISON_EQ='COMPARISON_EQ'
    COMPARISON_EQ='COMPARISON_NE'

  class Trigger(_DictExt):
    def __init__(self,
      count=None,
      percent=None,
    ):
      super().update_locals(locals())

  class MetricAbsence(_DictExt):
    def __init__(self,
      filter=None,
      aggregations=None,
      duration=None,
      trigger=None,
    ):
      super().update_locals(locals())

  class Aggregation(_DictExt):
    def __init__(self,
      alignmentPeriod=None,
      perSeriesAligner=None,
      crossSeriesReducer=None,
      groupByFields=None,
    ):
      super().update_locals(locals())

  class LogMatch(_DictExt):
    def __init__(self,
      filter=None,
      labelExtractors=None,
    ):
      super().update_locals(locals())

  class MonitoringQueryLanguageCondition(_DictExt):
    def __init__(self,
      query=None,
      duration=None,
      trigger=None,
    ):
      super().update_locals(locals())

  class ConditionCombinerType(EnumMeta):
    COMBINE_UNSPECIFIED='COMBINE_UNSPECIFIED'
    AND='AND'
    OR='OR'
    AND_WITH_MATCHING_RESOURCE='AND_WITH_MATCHING_RESOURCE'

  class AlertStrategy(_DictExt):
    def __init__(self,
      notificationRateLimit=None,
      autoClose=None,
    ):
      super().update_locals(locals())
      
  class NotificationRateLimit(_DictExt):
    def __init__(self,
      period=None,
    ):
      super().update_locals(locals())

  class _AlertPolicyProvider(ResourceProvider):

    def create(self, resource):
      import json
      from pulumi.dynamic import CreateResult

      alert_policy_object = AlertPolicy.Args(**resource)

      gcp_request = _GcpSession().post(
        f'https://monitoring.googleapis.com/v3/projects/{resource.pop("project")}/alertPolicies',
        headers={
          'content-type': 'application/json'
        },
        json=alert_policy_object
      )

      final_result = {
        **resource,
        **json.loads(gcp_request.text),
      }

      if gcp_request.status_code == 200:
        return CreateResult(
          id_=final_result['name'],
          outs=final_result
        )

      else:
        raise Exception(
          gcp_request.text
        )

    def read(self, name, resource):
      import json
      from pulumi.dynamic import ReadResult

      gcp_request = _GcpSession().get(
        f'https://monitoring.googleapis.com/v3/{resource.get("name")}',
      )
      if gcp_request.status_code == 200:
        return ReadResult(
          id_ = name,
          outs = json.loads(gcp_request.text)
        )
      elif gcp_request.status_code == 404:
        return ReadResult(
          '',
          {}
        )
      else:
        raise Exception(
          gcp_request.text
        )

    def update(self, name, old_resource, new_resource):
      from pulumi.dynamic import UpdateResult
      import json

      alert_policy_object = AlertPolicy.Args(**new_resource)

      gcp_request = _GcpSession().patch(
        f'https://monitoring.googleapis.com/v3/{old_resource.get("name")}',
        headers={
          'content-type': 'application/json'
        },
        json=alert_policy_object
      )

      if gcp_request.status_code == 200:
        return UpdateResult(
          outs=json.loads(gcp_request.text)
        )

      else:
        raise Exception(
          gcp_request.text
        )

    def delete(self, name, resource):
      import json
      alert_policy_object = AlertPolicy.Args(**resource)
      gcp_request = _GcpSession().delete(
        f'https://monitoring.googleapis.com/v3/{alert_policy_object.get("name")}',
      )

      if gcp_request.status_code != 200:
        raise Exception(
          gcp_request.text
        )

  name: Output[str]
  displayName: Output[str]
  documentation: Output[dict]
  userLabels: Output[dict]
  conditions: Output[list]
  combiner: Output[str]
  enabled: Output[bool]
  validity: Output[dict]
  notificationChannels: Output[list]
  creationRecord: Output[dict]
  mutationRecord: Output[dict]
  alertStrategy: Output[dict]

  def __init__(self, resource_name, 
    args: Output[Args] = None,
    name: Output[str] = None,
    displayName: Output[str] = None,
    documentation: Output[dict] = None,
    userLabels: Output[dict] = None,
    conditions: Output[list] = None,
    combiner: Output[str] = None,
    enabled: Output[bool] = None,
    validity: Output[dict] = None,
    notificationChannels: Output[list] = None,
    creationRecord: Output[dict] = None,
    mutationRecord: Output[dict] = None,
    alertStrategy: Output[dict] = None,
    **kwargs,
  ):

    resource_parameters = {
      **args,
      **kwargs,
    } if args is not None else {
      **dict(
        name=name,
        displayName=displayName,
        documentation=documentation,
        userLabels=userLabels,
        conditions=conditions,
        combiner=combiner,
        enabled=enabled,
        validity=validity,
        notificationChannels=notificationChannels,
        creationRecord=creationRecord,
        mutationRecord=mutationRecord,
        alertStrategy=alertStrategy,
      ),
      **kwargs,
    }

    opts = resource_parameters.pop('opts', None)

    super(AlertPolicy, self).__init__(self._AlertPolicyProvider(),
      resource_name,
      resource_parameters,
      opts=opts
    )