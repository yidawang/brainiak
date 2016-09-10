#  Copyright 2016 Intel Corporation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""Full correlation matrix analysis"""

import pyximport
from mpi4py import MPI
pyximport.install()

a = 'uninstalled'
# make the cython building execute only once
if MPI.COMM_WORLD.Get_rank() == 0:
    from . import cython_blas as blas
    blas.installed()
    a = 'installed'
# tell everybody the building is done
# functions as a barrier
a = MPI.COMM_WORLD.bcast(a, root=0)
