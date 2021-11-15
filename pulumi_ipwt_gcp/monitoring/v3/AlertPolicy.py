from pulumi import Output
from pulumi.dynamic import Resource
from pulumi.dynamic import ResourceProvider

from pulumi_ipwt_gcp.helpers import _DictExt
from pulumi_ipwt_gcp.helpers import gcp_session

from enum import EnumMeta

class AlertPolicy(Resource, module='IPWT-gcp', name='monitoring/v3/AlertPolicy'):

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
      super().add(name=name)
      super().add(displayName=displayName)
      super().add(documentation=documentation)
      super().add(userLabels=userLabels)
      super().add(conditions=conditions)
      super().add(combiner=combiner)
      super().add(enabled=enabled)
      super().add(validity=validity)
      super().add(notificationChannels=notificationChannels)
      super().add(creationRecord=creationRecord)
      super().add(mutationRecord=mutationRecord)
      super().add(alertStrategy=alertStrategy)

  class Documentation(_DictExt):
    def __init__(self,
      **kwargs,
    ):
      super().add(content=kwargs.get('content', None))
      super().add(mimeType=kwargs.get('mimeType', None))

  class Condition(_DictExt):
    def __init__(self,
      name=None,
      displayName=None,
      conditionThreshold=None,
      conditionAbsent=None,
      conditionMatchedLog=None,
      conditionMonitoringQueryLanguage=None,
    ):
      super().add(name=name)
      super().add(displayName=displayName)
      super().add(conditionThreshold=conditionThreshold)
      super().add(conditionAbsent=conditionAbsent)
      super().add(conditionMatchedLog=conditionMatchedLog)
      super().add(conditionMonitoringQueryLanguage=conditionMonitoringQueryLanguage)

  class MetricThreshold(_DictExt):
    def __init__(self,
      **kwargs,
    ):
      super().add(filter=kwargs.get('filter', None))
      super().add(aggregations=kwargs.get('aggregations', None))
      super().add(denominatorFilter=kwargs.get('denominatorFilter', None))
      super().add(comparison=kwargs.get('comparison', None))
      super().add(thresholdValue=kwargs.get('thresholdValue', None))
      super().add(duration=kwargs.get('duration', None))
      super().add(trigger=kwargs.get('trigger', None))

  class Aggregation(_DictExt):
    def __init__(self,
      **kwargs,
    ):
      super().add(alignmentPeriod=kwargs.get('alignmentPeriod', None))
      super().add(perSeriesAligner=kwargs.get('perSeriesAligner', None))
      super().add(crossSeriesReducer=kwargs.get('crossSeriesReducer', None))
      super().add(groupByFields=kwargs.get('groupByFields', None))

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
      **kwargs,
    ):
      super().add(count=kwargs.get('count', None))
      super().add(percent=kwargs.get('percent', None))

  class MetricAbsence(_DictExt):
    def __init__(self,
      **kwargs
    ):
      super().add(filter=kwargs.get('filter', None))
      super().add(aggregations=kwargs.get('aggregations', None))
      super().add(duration=kwargs.get('duration', None))
      super().add(trigger=kwargs.get('trigger', None))

  class Aggregation(_DictExt):
    def __init__(self,
      **kwargs
    ):
      super().add(alignmentPeriod=kwargs.get('alignmentPeriod', None))
      super().add(perSeriesAligner=kwargs.get('perSeriesAligner', None))
      super().add(crossSeriesReducer=kwargs.get('crossSeriesReducer', None))
      super().add(groupByFields=kwargs.get('groupByFields', None))

  class LogMatch(_DictExt):
    def __init__(self,
      **kwargs
    ):
      super().add(filter=kwargs.get('filter', None))
      super().add(labelExtractors=kwargs.get('labelExtractors', None))

  class MonitoringQueryLanguageCondition(_DictExt):
    def __init__(self,
      **kwargs
    ):
      super().add(query=kwargs.get('query', None))
      super().add(duration=kwargs.get('duration', None))
      super().add(trigger=kwargs.get('trigger', None))

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
      super().add(notificationRateLimit=notificationRateLimit)
      super().add(autoClose=autoClose)
      
  class NotificationRateLimit(_DictExt):
    def __init__(self,
      **kwargs
    ):
      super().add(period=kwargs.get('period', None))

  class _AlertPolicyProvider(ResourceProvider):

    _gcp_session = None

    def create(self, resource):
      import json
      from pulumi.dynamic import CreateResult

      alert_policy_object = AlertPolicy.Args(**resource)

      gcp_request = gcp_session.post(
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

      gcp_request = gcp_session.get(
        f'https://monitoring.googleapis.com/v3{resource.get("name")}',
      )
      if gcp_request.status_code == 200:
        return ReadResult(
          name,
          json.dumps(gcp_request.text)
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
      print(json.dumps(alert_policy_object, indent=2))

      gcp_request = gcp_session.patch(
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
      gcp_request = gcp_session.delete(
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

  def __init__(self, name, **kwargs):

    opts = kwargs.pop('opts', None)

    super(AlertPolicy, self).__init__(self._AlertPolicyProvider(), name,
      kwargs,
      opts=opts
    )