# Copyright (C) 2023 by
# Yangruirui Zhou <yrrzhou@bu.edu>, CIDAR Lab, Boston University
# All rights reserved.
# OSI Non-Profit Open Software License ("Non-Profit OSL") 3.0 license.
# Start working on the verification stage

import sys
import UpdateFunctions as uf
import csv
import EnlargeCommunity as ec
sys.path.append("../Oriole")
import utils
import time
import networkx as nx
import EdgeFunctions as ef
import CommunityFunctions as ccf
import InOutFunctions as iof
import InitiateFunctions as inf
import CalculationFunctions as clf


# If solution find, we return "verification passed" and save the current clustering solution.
def Verification(G_primitive, S_bounds, ConstraintType, constraint, loop_free, out_path, timestep,
    bio_flag, height, ub):

    begin_time = time.time()

    # If the max size for one community is bigger than the current total number of the nodes, output it and continue the next sample
    if len(G_primitive.nodes) < S_bounds[1]:
        CostTime = time.time() - begin_time
        iof.writeSolution(out_path, f'/sol_after_verify_{S_bounds[1]}_{constraint}.txt', G_primitive, [], CostTime)
        print("All nodes can be put in one community!")
        return

    # Initiate communities
    CurrentVerifyResult = inf.createInitialCommunities(G_primitive)

    # Find the pending community, if no pending community, save current cluster result.
    PendingCommunities = ccf.findPendingCommunities(G_primitive, CurrentVerifyResult, constraint, bio_flag)
    if len(PendingCommunities) == 0:
        CostTime = time.time() - begin_time
        iof.writeSolution(out_path, f'/sol_after_verify_{S_bounds[1]}_{constraint}.txt', G_primitive, CurrentVerifyResult, CostTime)
        return
    print("PendingCommunities: ", PendingCommunities)

    # Start to solve the pending communities
    # Find the worst case in the PendingCommunities
    PendingCommunity = ccf.findWorstCommunity(G_primitive, PendingCommunities, CurrentVerifyResult, bio_flag)
    print("PendingCommunity: ", PendingCommunity)

    # Start to solve the worst case by enlarging its size
    VerifyResult, VerifyFlag, ErrorLog, _ = ec.enlargeCommunity(G_primitive, PendingCommunity, S_bounds, ConstraintType, timestep,
                                                   constraint, loop_free, CurrentVerifyResult, bio_flag, ub, height)

    # If VerifyFlag is false, that means the graph and constraints don't pass the verification, user should change
    # it later. If it is ture, save the result. Then we go to the merging stage.
    if VerifyFlag:
        print("Verification passed!")
        # Write current verify solution into an output file
        CostTime = time.time() - begin_time
        iof.writeSolution(out_path, f'/sol_after_verify_{S_bounds[1]}_{constraint}.txt', G_primitive, VerifyResult, CostTime)
    else:
        iof.reportIssue(out_path, ErrorLog)


# Verification()
