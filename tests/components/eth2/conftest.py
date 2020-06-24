import pytest

from eth2.beacon.state_machines.forks.skeleton_lake.configs import (
    MINIMAL_SERENITY_CONFIG,
)
from eth2.beacon.tools.misc.ssz_vector import override_lengths


# SSZ
@pytest.fixture(scope="function", autouse=True)
def override_ssz_lengths():
    override_lengths(MINIMAL_SERENITY_CONFIG)
