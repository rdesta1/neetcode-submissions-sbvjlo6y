class Vertex:
    def __init__(self, val):
        self.val = val
        self.edgs = []

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        #Add the src or dst vertex if they dont exist
        if src not in self.graph:
            self.graph[src] = Vertex(src)
        if dst not in self.graph:
            self.graph[dst] = Vertex(dst)

        #Adding dst to src
        srcVrtx = self.graph[src]
        dstVrtx =self.graph[dst]

        srcVrtx.edgs.append(dstVrtx)


    def removeEdge(self, src: int, dst: int) -> bool:
        #return false if neither vertex exits
        if src not in self.graph or dst not in self.graph:
            return False

        srcVrtx = self.graph[src]
        dstVrtx = self.graph[dst]

        #return true if edge to dst is removed
        if dstVrtx in srcVrtx.edgs:
            srcVrtx.edgs.remove(dstVrtx)
            return True

        return False

    def hasPath(self, src: int, dst: int) -> bool:

        dq = deque()
        dq.append(self.graph[src])
        dstVrtx = self.graph[dst]

        while dq:
            cur = dq.popleft()

            if cur == dstVrtx:
                return True
            
            for edg in cur.edgs:
                if edg not in dq:
                    dq.append(edg)
            
        return False
            
                
            
























    
