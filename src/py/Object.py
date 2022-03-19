import hashlib
class Object:
    def __init__(self,id,corruption_rate,pool_id=0):
        self.id=id
        # sha256 string
        self.pool_id=pool_id
        # discuss if the pool_id should be hashed with the object in a real case
        self.hash=hashlib.sha256(str(id).encode("utf-8")).hexdigest()
        # corruption rate from 0.01 to 0.2
        self.corruption_rate=corruption_rate

        self.is_corruped = False
    def to_string(self):
        return "id: " + str(self.id) + " sha256: " + self.hash + " corruption_rate: " + str(self.corruption_rate)