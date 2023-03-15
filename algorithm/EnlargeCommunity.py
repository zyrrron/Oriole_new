import InitiateFunctions as inf
import CalculationFunctions as calf
import NodeFunctions as nf

# Try to enlarge the given community i.
# After searching and calculating all the gains for moving each neighbor node into community i,
# move the node j giving the highest positive gain to our community i.
# If all gains are negative or the node number achieve the size constraint, stop enlarge.
# Check if current community i meets all constraints every time when we move node j into community i.
# Record it if meets all constraints.
# Better use recursion here.
def enlargeCommunity(G, PendingCommunity, S_bounds, ConstraintType, constraint, loop_free, priority, timestep, CurrentVerifyResult):
    # calculate the rewards provided by all neighbor communities
    NeighborNodes = nf.findAllNeighborsComm(PendingCommunity, G)
    rewards = {}
    for node in NeighborNodes:
        rewards[node] = calf.calculateReward(G, node, PendingCommunity, CurrentVerifyResult)

    # find the community provides the highest reward

    return