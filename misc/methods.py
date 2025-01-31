
def triad_census (nodes, edges):
        census = []
        """census.append(triad_1(nodes, edges))
        print(triad_1(nodes, edges))
        census.append(triad_2(nodes, edges))
        print(triad_2(nodes, edges))
        census.append(triad_3(nodes, edges))
        print(triad_3(nodes, edges))
        census.append(triad_4(nodes, edges))
        print(triad_4(nodes, edges))
        census.append(triad_5(nodes, edges))
        print(triad_5(nodes, edges))
        census.append(triad_6(nodes, edges))
        print(triad_6(nodes, edges))
        census.append(triad_7(nodes, edges))"""
        print(triad_7(nodes, edges))
        print(triad_8(nodes, edges))
        print(triad_9(nodes, edges))
        """census.append(triad_10(nodes, edges))
        print(triad_10(nodes, edges))
        census.append(triad_11(nodes, edges))
        print(triad_11(nodes, edges))
        census.append(triad_12(nodes, edges))
        print(triad_12(nodes, edges))
        census.append(triad_13(nodes, edges))
        print(triad_13(nodes, edges))
        return census"""


def triad_1 (nodes, edges):
    #find triad 1: b <- a -> c
        message = ""
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a: #skip if they are the same node
                    edge_one = (node_a, node_b) #a -> b
                    inverse_edge_one = (node_b, node_a) #a <- b

                    if edge_one in edges and inverse_edge_one not in edges:
                        for node_c in nodes:
                            if node_c != node_b and node_c != node_a: #skip if they are the same node
                                edge_two = (node_a, node_c) #a -> c
                                inverse_edge_two = (node_c, node_a) #a <- c
                                b_to_c = ((node_c, node_b) in edges) or ((node_b, node_c) in edges)
                                if edge_one != edge_two and edge_two:
                                    if not b_to_c and edge_two in edges and inverse_edge_two not in edges:
                                        if message.find(""+ node_c + " <- " + node_a + " -> " + node_b + "\n") == -1:
                                            triad = node_b + " <- " + node_a + " -> " + node_c + "\n"
                                            message += triad
                                            count+=1
        return count

def triad_2 (nodes, edges):
        # b -> a <- c
        message = ""
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a: #skip if they are the same node
                    edge_one = (node_b, node_a)
                    inverse_edge_one = (node_a, node_b)

                    if edge_one in edges and inverse_edge_one not in edges:
                        for node_c in nodes:
                            if node_c != node_b and node_c != node_a: #skip if they are the same node
                                edge_two = (node_c, node_a)
                                inverse_edge_two = (node_a, node_c)
                                b_to_c = ((node_c, node_b) in edges) or ((node_b, node_c) in edges)
                                if message.find(""+ node_c + " -> " + node_a + " <- " + node_b + "\n") == -1:
                                    if not b_to_c and edge_two in edges and inverse_edge_two not in edges and edge_one != edge_two:
                                        triad = node_b + " -> " + node_a + " <- " + node_c + "\n"
                                        message += triad
                                        count+=1
        return count

def triad_3 (nodes, edges):
    #find triad 03: a-> b -> c
        message = ""
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a: #skip if they are the same node
                    edge_one = (node_a, node_b) #a -> b
                    inverse_edge_one = (node_b, node_a) #a <- b
                    if edge_one in edges and inverse_edge_one not in edges:
                        for node_c in nodes:
                            if node_c != node_b and node_c != node_a: #skip if they are the same node
                                edge_two = (node_b, node_c) #b -> c
                                inverse_edge_two = (node_c, node_b) #c <- b
                                a_to_c = ((node_c, node_a) in edges) or ((node_a, node_c) in edges)
                                if message.find(""+ node_c + " -> " + node_b + " -> " + node_a + "\n") == -1:
                                    if not a_to_c and edge_two in edges and inverse_edge_two not in edges and edge_one != edge_two:
                                        triad = node_a + " -> " + node_b + " -> " + node_c + "\n"
                                        message += triad
                                        count+=1
        return count

def triad_4 (nodes, edges):
        #a -> b <-> c
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a:
                    edge_one = (node_a, node_b) in edges#a -> b
                    inverse_edge_one = (node_b, node_a) in edges#make sure a <- b does not exist
                    if edge_one and not inverse_edge_one:
                        for node_c in nodes:
                            if node_c != node_b and node_c != node_a: #make sure a,b,c are not the same node
                                edge_two = (node_b, node_c) in edges and (node_c, node_b) in edges #check for b <-> c
                                c_to_a = (node_c, node_a) in edges or (node_a, node_c) in edges #make sure a -> c or a <- c is not in edges
                                if edge_two and not c_to_a:
                                    count+=1
        return count

def triad_5 (nodes, edges):
        #a <-> b -> c
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a:
                    edge_one = (node_a, node_b) in edges and (node_b, node_a) in edges
                    if edge_one:
                        for node_c in nodes:
                            if node_c != node_b:
                                edge_two = (node_b, node_c) in edges and (node_c, node_b) not in edges
                                c_to_a = (node_c, node_a) in edges or (node_a, node_c) not in edges
                                if edge_two and not c_to_a:
                                    count+=1
        return count

def triad_6 (nodes, edges):
        #b <-> a <-> c
        count  = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a:
                    edge_one = (node_a, node_b) in edges and (node_b, node_a) in edges
                    if edge_one:
                        for node_c in nodes:
                            if node_c != node_b and node_c != node_a:
                                edge_two = (node_b, node_c) in edges and (node_c, node_b) in edges
                                c_to_a = (node_c, node_a) in edges or (node_a, node_c) not in edges
                                if edge_two and not c_to_a:
                                    count+=1
        return count

def triad_7 (nodes, edges):
    # b <- a -> c -> b
        triads = set()        
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a: #skip if they are the same node
                    edge_one = (node_a, node_b) #a -> b
                    inverse_edge_one = (node_b, node_a) #a <- b
                    if (edge_one in edges) and (inverse_edge_one not in edges):
                        for node_c in nodes:
                            if node_c != node_b and node_c != node_a:
                                    edge_two = (node_a, node_c) #a -> c
                                    inverse_edge_two = (node_c, node_a) #c <- a
                                    edge_three = (node_c, node_b) #c -> b
                                    inverse_edge_three = (node_b, node_c) #b -> c
                                    if edge_three != edge_two and edge_two != edge_one:
                                        if edge_three in edges and edge_two in edges and inverse_edge_two not in edges and inverse_edge_three not in edges:
                                            sorted_nodes = sorted([node_a, node_b, node_c])
                                            triad = tuple(sorted_nodes)
                                            if triad not in triads:
                                                triads.add(triad)
                                                count+=1
        return count

def triad_8 (nodes, edges):
    #a-> b -> c -> a
        triads = set() #this set will have triads that were already counted
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a: #skip if they are the same node
                    edge_one = (node_a, node_b) #a -> b
                    inverse_edge_one = (node_b, node_a) #a <- b
                    if edge_one in edges and inverse_edge_one not in edges:
                        for node_c in nodes:
                            if node_c != node_b and node_c != node_a: #if this combo of nodes was not 
                                    edge_two = (node_b, node_c) #b -> c
                                    inverse_edge_two = (node_c, node_b) #c <- b
                                    edge_three = (node_c, node_a)
                                    inverse_edge_three = (node_a, node_c)
                                    if edge_three in edges and edge_two in edges and inverse_edge_two not in edges and inverse_edge_three not in edges:
                                        sorted_nodes = sorted([node_a, node_b, node_c])
                                        triad = tuple(sorted_nodes)
                                        if triad not in triads:
                                            triads.add(triad)
                                            count+=1
        return count

def triad_9 (nodes, edges):
    #b <- a -> c <-> b
        triads = set()
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a: #skip if they are the same node
                    edge_one = (node_a, node_b) #a -> b
                    inverse_edge_one = (node_b, node_a) #a <- b
                    if edge_one in edges and inverse_edge_one not in edges:
                        for node_c in nodes:
                            if node_c != node_b and node_c != node_a:
                                    edge_two = (node_a, node_c) in edges and (node_c, node_a) not in edges  #a -> c
                                    edge_three = (node_c, node_b) in edges and (node_b, node_c) in edges    # c <-> b
                                    if edge_three and edge_two:                                        
                                        sorted_nodes = sorted([node_a, node_b, node_c])
                                        triad = tuple(sorted_nodes)
                                        if triad not in triads:
                                            triads.add(triad)
                                            count+=1
        return count

def triad_10 (nodes, edges):
    #c <- b <-> a -> c
        triads = set()
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a: #skip if they are the same node
                    edge_one = (node_a, node_b) in edges and (node_b, node_a) in edges #a <-> b
                    if edge_one:
                        for node_c in nodes:
                            triad = (node_a,node_b,node_c)
                            if triad not in triads and node_c != node_b and node_c != node_a:
                                    edge_two = (node_a, node_c) in edges and (node_c, node_a) not in edges  #a -> c
                                    edge_three = (node_b, node_c) in edges and (node_c, node_b) not in edges #b -> c
                                    #double_counting = (node_a, node_b) != (node_a, node_c) and (node_c, node_b) != (node_a, node_b)
                                    if edge_three and edge_two:
                                                triads.add(tuple(sorted(triad)))
                                                count+=1
        return count

def triad_11 (nodes, edges):
    #a -> b -> c <-> a
        triads = set()
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a: #skip if they are the same node
                    edge_one = (node_a, node_b) in edges and (node_b, node_a) not in edges #a -> b
                    if edge_one:
                        for node_c in nodes:
                            triad = (node_a,node_b,node_c)
                            if triad not in triads and node_c != node_b and node_c != node_a:
                                    edge_two = (node_a, node_c) in edges and (node_c, node_a) in edges  #a <-> c
                                    edge_three = (node_b, node_c) in edges and (node_c, node_b) not in edges #b -> c
                                    #double_counting = (node_a, node_b) != (node_a, node_c) and (node_c, node_b) != (node_a, node_b)
                                    if edge_three and edge_two:
                                                triads.add(tuple(sorted(triad)))
                                                count+=1
        return count

def triad_12 (nodes, edges):
    #a -> b <-> c <-> a
        triads = set()
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a: #skip if they are the same node
                    edge_one = (node_a, node_b) in edges and (node_b, node_a) not in edges #a -> b
                    if edge_one:
                        for node_c in nodes:
                            triad = (node_a,node_b,node_c)
                            if triad not in triads and node_c != node_b and node_c != node_a:
                                    edge_two = (node_a, node_c) in edges and (node_c, node_a) in edges  #a <-> c
                                    edge_three = (node_b, node_c) in edges and (node_c, node_b) in edges #b <-> c
                                    #double_counting = (node_a, node_b) != (node_a, node_c) and (node_c, node_b) != (node_a, node_b)
                                    if edge_three and edge_two:
                                                triads.add(tuple(sorted(triad)))
                                                count+=1
        return count

def triad_13 (nodes, edges):
    # b <-> a <-> c <-> b
        triads = set()
        message = ""
        count = 0
        for node_a in nodes:
            for node_b in nodes:
                if node_b != node_a: #skip if they are the same node
                    edge_one = (node_a, node_b) #a -> b
                    inverse_edge_one = (node_b, node_a) #a <- b
                    if (edge_one in edges) and (inverse_edge_one in edges):
                        for node_c in nodes:                                    
                            triad = (node_a,node_b,node_c)
                            if triad not in triads and node_c != node_b and node_c != node_a:
                                    edge_two = (node_a, node_c) #a -> c
                                    inverse_edge_two = (node_c, node_a) #c <- a
                                    edge_three = (node_c, node_b) #c -> b
                                    inverse_edge_three = (node_c, node_a) #b <- c
                                    if edge_three != edge_two and edge_two != edge_one:
                                        if edge_three in edges and edge_two in edges and inverse_edge_two in edges and inverse_edge_three in edges:
                                                triads.add(tuple(sorted(triad)))
                                                count+=1
        return count