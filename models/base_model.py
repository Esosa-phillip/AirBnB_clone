#!/usr/bin/python3

"""Model BaseModel Parent of all classes"""
from datetime import datetime
import uuid


class BaseModel:
    """Base class for AirBnB clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """Initializes the attributes:
        random uuid, date create or update"""
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(
                            kwargs["created_at"],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif "update_at" == key:
                    self.updated_at = datetime.strptime(
                            kwargs["updated_at"],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    # we are not doing anything with class
                    pass
                else:
                    setattr(self, key, value)
        else:
            # Generate random UUID
            self.id = str(uuid.uuid4())
            # assign current date time when an instance is created
            self.created_at = datetime.now
            self.updated_at = datetime.now
            # if it is a new inheritance add to the models
            from models.__init__ import storage
            storage.new(self)

    def __str__(self):
        """Info about models in string format"""
        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                self.id, self.__dict__))

    def __repr__(self):
        """Returns string representation"""
        return (self.__str__())

    def save(self):
        """Updates the public instance attriute updated_at
        with the current datetime"""
        self.update_at = datetime.now()
        from models.__init__ import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance"""

        # Define the dictionary that adds classs name as  element
        dic = {}
        dic["__class__"] = type(self).__name__
        # Loop over the dict items
        # Convert create_at and update_at to ISO format
        for key, val in self.__dict__.items():
            if isinstance(val, (datetime, )):
                dic[key] = val.isoformat()
            else:
                dic[key] = val
        return dic
