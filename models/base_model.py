import models
from uuid import uuid4
from datetime import datetime

class Base_model():
    """
    this is the representation of AirBnB project 
    """
    def __init__(self, *args, **kwargs):
        """
        this will initialize the new basemodel
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for a, z in kwargs.items():
                if a == "created_at" or a == "updated_at":
                    self.__dict__[a] = datetime.strtime(z, tform)
                else:
                    self.__dict__[a] = z
        else:
            models.storage.new(self)

    def __str__(self):
        """
        this will print the string represenation of the basemodel 
        """
        the_name = self.__class__.__name__
        return"[{}] ({}) {}".format(the_name, self.id, self.__dict__)

    def save(self):
        """
        this updates the Updated_at instance with the date an time 
        """
        self.updated_at = datetime.today()
        models.storage.save()
    
    def to_dict(self):
        """
        this will return the dictionary of the base model
        """

        rdict = self.__dict__.copy()
        rdict["class"] = self.__class__.__name__
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        return rdict

