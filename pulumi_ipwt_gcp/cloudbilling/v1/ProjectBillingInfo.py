from pulumi import Output
from pulumi.dynamic import Resource
from pulumi.dynamic import ResourceProvider

from pulumi_ipwt_gcp.helpers import _DictExt
from pulumi_ipwt_gcp.helpers import _GcpSession

class ProjectBillingInfo(Resource, module='IPWT-gcp', name='cloudbilling/v1/ProjectBillingInfo'):
  '''
  https://cloud.google.com/billing/docs/reference/rest/v1/billingAccounts
  '''

  class Args(_DictExt):
    def __init__(self,
      name=None,
      projectId=None,
      billingAccountName=None,
      billingEnabled=None,
      **kwargs,
    ):
      kwargs = None
      super().update_locals(locals())

  class _ProjectBillingInfoProvider(ResourceProvider):

    def create(self, resource):
      import json
      from pulumi.dynamic import CreateResult

      project_billing_info = ProjectBillingInfo.Args(**resource)

      gcp_request = _GcpSession().put(
        f'https://cloudbilling.googleapis.com/v1/projects/{resource.pop("projectId")}/billingInfo',
        json=project_billing_info,
      )

      final_result = json.loads(gcp_request.text)

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
        f'https://cloudbilling.googleapis.com/v1/{resource.pop("name")}',
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

      project_billing_info = ProjectBillingInfo.Args(**new_resource)
      project_billing_info

      gcp_request = _GcpSession().put(
        f'https://cloudbilling.googleapis.com/v1/{new_resource.pop("name")}',
        json=project_billing_info
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
      project_billing_info = ProjectBillingInfo.Args(**resource)
      project_billing_info['billingEnabled'] == False
      gcp_request = _GcpSession().put(
        f'https://cloudbilling.googleapis.com/v1/{project_billing_info.get("name")}',
      )

      if gcp_request.status_code != 200:
        raise Exception(
          gcp_request.text
        )

  name: Output[str]
  projectId: Output[str]
  billingAccountName: Output[str]
  billingEnabled: Output[bool]

  def __init__(self, resource_name,
    args: Output[Args] = None,
    name: Output[str] = None,
    projectId: Output[str] = None,
    billingAccountName: Output[str] = None,
    billingEnabled: Output[bool] = None,
    **kwargs,
  ):

    resource_parameters = {
      **args,
      **kwargs,
    } if args is not None else {
      **dict(
        name=name,
        projectId=projectId,
        billingAccountName=billingAccountName,
        billingEnabled=billingEnabled,
      ),
      **kwargs,
    }

    opts = resource_parameters.pop('opts', None)

    super(ProjectBillingInfo, self).__init__(self._ProjectBillingInfoProvider(),
      resource_name,
      resource_parameters,
      opts=opts
    )

    