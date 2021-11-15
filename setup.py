from setuptools import setup


VERSION = "0.1"

setup(
  name='pulumi_ipwt_gcp',
  version=VERSION,
  description="Pulumi dynamic provider package for GCP by IPWT.PL",
  url='https://github.com/mszewczyk-ipwt/pulumi-ipwt-gcp',
  project_urls={
      'Repository': 'https://github.com/mszewczyk-ipwt/pulumi-ipwt-gcp'
  },
  license='Apache-2.0',
  install_requires=[
      'pulumi'
  ],
  zip_safe=False
)
