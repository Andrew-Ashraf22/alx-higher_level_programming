#!/usr/bin/python3
#!/usr/bin/python3
"""makes a base geometry class"""


class BaseGeometry:
    """a base geometry class"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if value is int

        Args:
            name (str): The name
            value (int): The int to check
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is negative or == 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
