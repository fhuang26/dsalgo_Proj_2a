"""
Project 2: Show Me the Data Structures

problem 4. Active Directory

   is_user_in_group(user, group) checks whether a user is in the group.
   
   In this group structure, from input group g1, there can be multiple paths to
   go to another group g3. For example g1 -> g2 -> g3 and g1 -> g4 -> g3. So
   this can be a dense group graph like a complete graph.
   
   We do BFS (breath-first search) with a visited set to visit each group once.
   
   Time: O(N*(M + N)), where M is the number of users and N is the number of groups.
                For worst case, most users may be in all groups, g3.get_groups()
                returns a list of neighbor groups of group g3, the graph of groups is
                dense, and it traverses each group once.
   
   Space: O(M + N), where M is the number of users and N is the number of groups.
                For worst case, most users may be in all groups, g2.get_groups()
                returns a list of neighbor groups of group g2, the graph of groups is
                dense, and it traverses each group once. As BFS goes on in the while
                loop, one copy of ul (user list, max length M) and gpList (group list,
                max length N) exist in memory. The length of gp_queue is O(N).
                The size of visited set is O(N). These lead to space O(M + N).

"""
import queue

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        
    def add_group(self, group):
        self.groups.append(group)
        
    def add_user(self, user):
        self.users.append(user)
    
    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

visited = None
def is_user_in_group(user=None, group=None):
    """
    Return True if user is in the group, False otherwise.
    
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or group is None:
        return False
    
    visited.add(group)
    ul = group.get_users()
    if user in ul:
        return True
    
    gp_queue = queue.Queue()
    gpList = group.get_groups()
    if len(gpList) > 0:
        for g1 in gpList:
            if g1 in visited:
                continue
            visited.add(g1)
            gp_queue.put(g1)
    
    # BFS visits each group once.
    while gp_queue.qsize() > 0:
        g2 = gp_queue.get()  # FIFO
        ul = g2.get_users()
        if user in ul:
            return True
        gpList = g2.get_groups()
        if len(gpList) > 0:
            for g3 in gpList:
                if g3 in visited:
                    continue
                visited.add(g3)
                gp_queue.put(g3)
    
    return False

parent = Group("parent")
child1 = Group("child1")
child2 = Group("child2")
subchild6 = Group("subchild6")
subchild7 = Group("subchild7")
subchild8 = Group("subchild8")
subchild14 = Group("subchild14")
subchild13 = Group("subchild13")
subchild19 = Group("subchild19")

parent.add_group(child1)
parent.add_group(child2)
child1.add_group(subchild14)
child1.add_group(subchild13)
child1.add_group(subchild19)
child2.add_group(subchild6)
child2.add_group(subchild7)
child2.add_group(subchild8)
subchild13.add_group(subchild19)
subchild19.add_group(subchild13)

subchild6.add_user("u6")
subchild7.add_user("u7")
subchild7.add_user("u6")
subchild8.add_user("u8")
subchild14.add_user("u14")
subchild13.add_user("u13")
subchild19.add_user("u19")
child1.add_user("u1")
child2.add_user("u2")
parent.add_user("u3")

def test_func(f1, f2):
    if f1 == f2:
        print("Pass")
    else:
        print("Fail")

visited=set(); test_func(is_user_in_group("u7", child2), True)
visited=set(); test_func(is_user_in_group("u6", parent), True)
visited=set(); test_func(is_user_in_group("u8", subchild8), True)
visited=set(); test_func(is_user_in_group("u5", parent), False)
visited=set(); test_func(is_user_in_group("u19", subchild13), True)
visited=set(); test_func(is_user_in_group("u14", child1), True)
visited=set(); test_func(is_user_in_group("u13", subchild19), True)
visited=set(); test_func(is_user_in_group("u6", child1), False)
visited=set(); test_func(is_user_in_group("", child1), False)
visited=set(); test_func(is_user_in_group("u3"), False)
visited=set(); test_func(is_user_in_group("u3", None), False)
visited=set(); test_func(is_user_in_group(), False)
visited=set(); test_func(is_user_in_group(None, child1), False)

"""
Output:

Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass

"""
