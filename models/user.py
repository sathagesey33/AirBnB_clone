from models.base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the User class.

        Args:
            *args: Not used in this implementation.
            **kwargs: Dictionary containing attribute values.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, getattr(self, 'id', None), self.__dict__)

