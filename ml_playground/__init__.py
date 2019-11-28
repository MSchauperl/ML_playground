"""
ML_playground
Playing around wiht tf, pytorch, ANI, deepchem ....
"""

# Add imports here
from .ml_playground import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
