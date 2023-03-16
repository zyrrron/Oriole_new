import EdgeFunctions as ef
import networkx as nx
import UpdateFunctions as uf

# check indegree/outdegree constraints for a given community
def checkInOut(G, community, constraint, CurrentVerifyResult):
    InEdges = ef.findIncomingEdges(G, community)
    OutEdges = ef.findOutgoingEdges(G, community)
    # check high constraint
    if len(constraint) == 2:
        if len(InEdges) <= constraint[0] and len(OutEdges) <= constraint[1]:
            return 0
        else:
            return max(0, len(InEdges)-constraint[0]) + max(0, len(OutEdges)-constraint[1])
    # check low constraint
    else:
        if len(InEdges) + len(OutEdges) <= constraint[0]:
            return 0
        else:
            return len(InEdges) + len(OutEdges) - constraint


# check community size
def checkSize(CurrentVerifyResult, c):
    size = 0
    for key in CurrentVerifyResult:
        if CurrentVerifyResult[key] == c:
            size += 1
    return size


# Find all neighbor communities around the given community c in G.
def findAllNeighborsComm(G, c, CurrentVerifyResult):

    # collect all neighbor nodes for the nodes inside community c
    NeighborNodes = set()
    for node in c:
        tmp = nx.all_neighbors(G, node)
        for t in tmp:
            NeighborNodes.add(t)

    # find the neighbor communities according to the NeiborNodes
    NeighborComm = set()
    for node in NeighborNodes:
        if CurrentVerifyResult[node] != c:
            NeighborComm.add(CurrentVerifyResult[node])
    return list(NeighborComm)


# Find Cycles related to given communities c
def findCyleComm(G, PendingCommunity, CurrentVerifyResult):
    return 0


# Find all incoming edges to Community C
def findIncomingEdgesComm(G, c, CurrentVerifyResult):
    CommunityNumToNodes = uf.mapCommunityToNodes(CurrentVerifyResult)
    InEdges = []
    # Collect all incoming edges for the nodes in community c
    for node in c:
        tmp = ef.findIncomingEdges(G, node)
        for t in tmp:
            InEdges.append(t)

    # select the Incoming edges for the community c
    InEdgesComm = []
    for ele in list(InEdges):
        # ele[1] must be in c, because it is an incoming edge, end node must in c.
        if ele[0] not in CommunityNumToNodes[c]:
            InEdgesComm.append(ele)
        else: print(ele)

    return InEdgesComm


# Find all outgoing edges from Community C
def findOutgoingEdgesComm(G, c, CurrentVerifyResult):
    CommunityNumToNodes = uf.mapCommunityToNodes(CurrentVerifyResult)
    OutEdges = []

    # Collect all outgoing edges for the nodes in community c
    for node in c:
        tmp = ef.findOutgoingEdges(G, node)
        for t in tmp:
            OutEdges.append(t)

    # select the Outgoing edges for the community c
    OutEdgesComm = []
    for ele in list(OutEdges):
        # ele[1] must be in c, because it is an incoming edge, end node must in c.
        if ele[0] not in CommunityNumToNodes[c]:
            OutEdgesComm.append(ele)
        else:
            print(ele)
    return OutEdgesComm


# Add neighbor Community into current pending community
def addNeighborComm(CurrentVerifyResult, NeighborComm, PendingCommunity):
    return CurrentVerifyResult


# Check loop caused by the current community c, if there is a loop, drop this try and back tracking to the last level.
def checkLoop(G, c, CurrentVerifyResult):
    InEdges = findIncomingEdgesComm(G, c, CurrentVerifyResult)
    OutEdges = findOutgoingEdgesComm(G, c, CurrentVerifyResult)

    # Find all communities provide incoming edges to community c
    InEdgesComm = []

    # Find all communities provide outgoing edges from community c
    OutEdgesComm = []

    # Compare InEdgesComm and OutEdgesComm, if they have same community b, that means loop between b and c.
    # Calculate the total number of cycles and return it.


    return 0


# Check and find the worst case in PendingCommunities
# There won't be any cycle when we get into this function, because we will not allow a community make cycles during the
# community enlarge procedure. Every time when we try to run this function, the current graph should not have any cycle between communities.
def findWorstCommunity(G, PendingCommunities, CurrentVerifyResult):
    maxVal = 0
    maxKey = ''
    maxEdges = 0
    for key in PendingCommunities:
        # update the worst case when a community has bigger value
        if PendingCommunities[key] > maxVal:
            maxKey = key
            maxEdges = findIncomingEdgesComm(G, key, CurrentVerifyResult) + findOutgoingEdgesComm(G, key, CurrentVerifyResult)

        # If the number of unmet constraints is equal, choose the one has more edges connected
        if PendingCommunities[key] == maxVal:
            if findIncomingEdgesComm(G, key, CurrentVerifyResult) + findOutgoingEdgesComm(G, key, CurrentVerifyResult) > maxEdges:
                maxKey = key
                maxEdges = findIncomingEdgesComm(G, key, CurrentVerifyResult) + findOutgoingEdgesComm(G, key, CurrentVerifyResult)
    return maxKey


# Find the communities that cannot meet all constraints, if there is no pending community exists, return -1, else return its community number
def findPendingCommunities(G, result, constraint):
    PendingCommunities = {}
    for key in result:
        res = checkInOut(G, key, constraint, result)
        if res != 0:
            PendingCommunities[key] = res
    print(PendingCommunities)
    return PendingCommunities