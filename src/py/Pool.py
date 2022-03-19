import hashlib
class Pool:
    def __init__(self,objects,id=-1,transaction=""):
        # list of objects in the pool
        self.objects=objects
        # sha256 root hash of the hash-list
        self.hash=hashlib.sha256("".join([obj.hash for obj in objects]).encode("utf-8")).hexdigest()
        # reference to the pool, integer from 1 - inf 
        self.id=id
        # transaction hash on the ethereum blockchain
        self.transaction=transaction
    def to_string(self):
        return "PoolId: " + str(self.id) + " with " + str(len(self.objects)) +" objects in pool"