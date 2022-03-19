import random
import hashlib
class Archive:
    def __init__(self,objects):
        self.objects=objects

    def retrieveObj(self,id):
        return next(obj for obj in self.objects if obj.id == id)

    def get_objects_by_pool_id(self,pool_id):
        return [obj for obj in self.objects if obj.pool_id == pool_id]
    
    def get_sample(self,n):
        return random.sample(self.objects,n)

    def corrupt(self,p):
        for obj in self.objects:
            if(random.uniform(0, 1)<p):
                obj.hash=hashlib.sha256((str(obj.id) + "x").encode("uft-8")).hexdigest()
                obj.is_corruped=True

    def clean(self):
        print("Cleanup archive")