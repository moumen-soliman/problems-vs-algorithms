# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = RouteTrieNode()
        print(self.children)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        if word not in current_node.children:
            current_node.insert(word)
            current_node = current_node.children[word]
        else:
            current_node = current_node.children[word]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        return self.root.children[prefix]

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router_trie = RouteTrie()

    def add_handler(self, path):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        if type(path) is not str:
            return -1

        new_path = path.split('/')

        for i in new_path:
            self.router_trie.insert(i)


    def lookup(self, path=''):
        if type(path) is not str:
            return False

        if path == '/':
            return "root handler"

        path = path.split('/')

        for key in self.router_trie.root.children.keys():
            if type(key) is str:
                if key in path:
                    return key.capitalize() + " page"

        return False

router_tree = RouteTrie()
router_tree.root.insert('/')

new_router = Router()
new_router.add_handler('jobs/coolstuff')
print(new_router.lookup('coolstuff'))
print(new_router.lookup('coolsuff')) #returns false - not in route

#edge cases
new_router.add_handler(93850398205) #Not a string - returns -1
print(new_router.lookup(None)) #returns false - not in route
print(new_router.lookup(9384093840)) #returns false - not in route

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router()
router.add_handler("/home/about")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("home/about")) # should print 'about handler'
print(router.lookup("home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("home/about/me")) # should print 'not found handler' or None if you did not implement one
