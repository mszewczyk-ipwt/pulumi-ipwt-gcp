from pulumi import Output
from pulumi.dynamic import Resource
from pulumi.dynamic import ResourceProvider

from pulumi_ipwt_gcp.helpers import _DictExt
from pulumi_ipwt_gcp.helpers import gcp_session

from enum import EnumMeta

class UptimeCheckConfig(Resource, module='IPWT-gcp', name='monitoring/v3/UptimeCheckConfig'):
  '''
  https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs
  '''

  class Args(_DictExt):
    def __init__(self,
      name=None,
      displayName=None,
      period=None,
      timeout=None,
      contentMatchers=None,
      selectedRegions=None,
      isInternal=None,
      internalCheckers=None,
      monitoredResource=None,
      resourceGroup=None,
      httpCheck=None,
      tcpCheck=None,
      **kwargs
    ):
      super().update_locals(locals())


  class UptimeCheckRegion(EnumMeta):
    REGION_UNSPECIFIED='REGION_UNSPECIFIED'
    USA='USA'
    EUROPE='EUROPE'
    SOUTH_AMERICA='SOUTH_AMERICA'
    ASIA_PACIFIC='ASIA_PACIFIC'

  class InternalChecker(_DictExt):
    def __init__(self,
      name=None,
      displayName=None,
      network=None,
      gcpZone=None,
      peerProjectId=None,
      state=None,
    ):
      super().update_locals(locals())

  class MonitoredResource(_DictExt):
    def __init__(self,
      type=None,
      labels=None
    ):
      super().update_locals(locals())

  class ResourceGroup(_DictExt):
    def __init__(self,
      groupId=None,
      resourceType=None,
    ):
      super().update_locals(locals())

  class GroupResourceType(EnumMeta):
    RESOURCE_TYPE_UNSPECIFIED='RESOURCE_TYPE_UNSPECIFIED'
    INSTANCE='INSTANCE'
    AWS_ELB_LOAD_BALANCER='AWS_ELB_LOAD_BALANCER'

  class HttpCheck(_DictExt):
    def __init__(self,
      requestMethod=None,
      useSsl=None,
      path=None,
      port=None,
      authInfo=None,
      maskHeaders=None,
      headers=None,
      contentType=None,
      validateSsl=None,
      body=None,
    ):
      super().update_locals(locals())

  class RequestMethod(EnumMeta):
    METHOD_UNSPECIFIED='METHOD_UNSPECIFIED'
    GET='GET'
    POST='POST'

  class BasicAuthentication(_DictExt):
    def __init__(self,
      username=None,
      password=None,
    ):
      super().update_locals(locals())

  class ContentType(EnumMeta):
    TYPE_UNSPECIFIED='TYPE_UNSPECIFIED'
    URL_ENCODED='URL_ENCODED'

  class TcpCheck:
    def __init__(self,
      json={},
      port=None,
    ):
      super().update_locals(locals())

  class ContentMatcher(_DictExt):

    def __init__(self,
      content=None,
      matcher=None,
    ):
      super().update_locals(locals())

  class ContentMatcherOption(EnumMeta):
    CONTENT_MATCHER_OPTION_UNSPECIFIED='CONTENT_MATCHER_OPTION_UNSPECIFIED'
    CONTAINS_STRING='CONTAINS_STRING'
    NOT_CONTAINS_STRING='NOT_CONTAINS_STRING'
    MATCHES_REGEX='MATCHES_REGEX'
    NOT_MATCHES_REGEX='NOT_MATCHES_REGEX'

  class State(EnumMeta):
    UNSPECIFIED='UNSPECIFIED'
    CREATING='CREATING'
    RUNNING='RUNNING'

  class _UptimeCheckConfigProvider(ResourceProvider):

    _gcp_session = None

    def create(self, resource):
      import json
      from pulumi.dynamic import CreateResult

      uck_object = UptimeCheckConfig.Args(**resource)

      gcp_request = gcp_session.post(
        f'https://monitoring.googleapis.com/v3/projects/{resource.pop("project")}/uptimeCheckConfigs',
        headers={
          'content-type': 'application/json'
        },
        json=uck_object
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
      import json
      from pulumi.dynamic import UpdateResult

      uptime_check_config_object = UptimeCheckConfig.Args(**new_resource)

      gcp_request = gcp_session.patch(
        f'https://monitoring.googleapis.com/v3/{old_resource.get("name")}',
        headers={
          'content-type': 'application/json'
        },
        json=uptime_check_config_object
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
      uptime_check_config_object = UptimeCheckConfig.Args(**resource)
      gcp_request = gcp_session.delete(
        f'https://monitoring.googleapis.com/v3/{uptime_check_config_object.get("name")}',
      )

      if gcp_request.status_code != 200:
        raise Exception(
          gcp_request.text
        )


  name: Output[str]
  displayName: Output[str]
  period: Output[str]
  timeout: Output[str]
  ContentMatchers: Output[dict]
  selectedRegions: Output[list]
  isInternal: Output[bool]
  internalCheckers: Output[str]
  monitoredResource: Output[dict]
  resourceGroup: Output[str]
  httpCheck: Output[dict]
  tcpCheck: Output[str]
  project: Output[str]

  def __init__(self, resource_name, 
    args: Output[Args] = None,
    name: Output[str] = None,
    displayName: Output[str] = None,
    period: Output[str] = None,
    timeout: Output[str] = None,
    ContentMatchers: Output[dict] = None,
    selectedRegions: Output[list] = None,
    isInternal: Output[bool] = None,
    internalCheckers: Output[str] = None,
    monitoredResource: Output[dict] = None,
    resourceGroup: Output[str] = None,
    httpCheck: Output[dict] = None,
    tcpCheck: Output[str] = None,
    project: Output[str] = None,
    **kwargs,
  ):

    resource_parameters = {
      **args,
      **kwargs,
    } if args is not None else {
      **dict(
        name=name,
        displayName=displayName,
        period=period,
        timeout=timeout,
        ContentMatchers=ContentMatchers,
        selectedRegions=selectedRegions,
        isInternal=isInternal,
        internalCheckers=internalCheckers,
        monitoredResource=monitoredResource,
        resourceGroup=resourceGroup,
        httpCheck=httpCheck,
        tcpCheck=tcpCheck,
        project=project,
      ),
      **kwargs,
    }

    opts = resource_parameters.pop('opts', None)

    super(UptimeCheckConfig, self).__init__(self._UptimeCheckConfigProvider(),
      resource_name,
      resource_parameters,
      opts=opts
    )