"""ATS smoke for the bumblebee-release-watch-proof-20260923 chart.

app-test-suite installs the packaged chart on the job's kind cluster and runs
this file with `pytest -m smoke`. The chart is template-app's placeholder and
deploys nothing yet, so the smoke is the cluster-level check alone: the kind
cluster ATS runs against is reachable. The generated tests/ats/pyproject.toml
makes ATS pick the pytest executor, which refuses a directory without a test
file (giantswarm/devctl#2354); this file is what a fresh scaffold lacks.
"""

import pykube
import pytest
from pytest_helm_charts.clusters import Cluster


@pytest.mark.smoke
def test_api_working(kube_cluster: Cluster) -> None:
    """The kind cluster ATS runs against is reachable."""
    assert kube_cluster.kube_client is not None
    assert len(pykube.Node.objects(kube_cluster.kube_client)) >= 1
