"""conftest.py
"""

import sys
import os
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../mesh/')


@pytest.fixture
def nodeIDcoords():
    """create node ID and coordinate matrix from nodes.dyn

    :returns: [snic, axes]
    """
    from fem_mesh import load_nodeIDs_coords
    nodefile = '%s/nodes.dyn' % myPath

    nodeIDcoords = load_nodeIDs_coords(nodefile)

    return nodeIDcoords


@pytest.fixture
def sorted_elems(nodeIDcoords):
    """create sorted elements numpy array from nodes.dyn & elems.dyn

    :returns: sorted_elems
    """
    from fem_mesh import load_elems
    from fem_mesh import SortElems
    from fem_mesh import SortNodeIDs
    elefile = '%s/elems.dyn' % myPath
    elems = load_elems(elefile)
    [snic, axes] = SortNodeIDs(nodeIDcoords, sort=False)
    sorted_elems = SortElems(elems, axes)

    return sorted_elems

