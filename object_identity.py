"""
Compare two objects in different ways
"""
class ObjectIdentity:
    """
    A simple class
    """
    def __init__(self, value):
        """
        Constructor for an object with a text.
        :param value: ein beliebiger Text
        """
        self.text = value

    @property
    def text(self):
        """
        Gets the value of _text
        :return: aktueller Text
        """
        return self._text

    @text.setter
    def text(self, value):
        """
        Sets the value of _text
        :param value: ein beliebiger Text
        """
        self._text = value

    def __eq__(self, other):
        """
        Compares the objects for equality.
        """
        if isinstance(other, ObjectIdentity):
            return self.text == other.text
        elif isinstance(other, str):
            return self.text == other
        return False


if __name__ == "__main__":
    obj1 = ObjectIdentity('auf ein Wort')
    obj2 = ObjectIdentity('auf ein Wort')

    if isinstance(obj1, ObjectIdentity):
        print('obj1 ist vom Typ ObjectIdentity')
    else:
        print('obj1 ist nicht vom Typ ObjectIdentity')

    if obj1 is obj2:
        print('ob1 und obj2 sind identisch')
    else:
        print('obj1 und obj2 sind nicht identisch')

    if obj1 == obj2:
        print('obj1 und obj2 haben den gleichen Inhalt')
    else:
        print('obj1 und obj2 haben unterschiedlichen Inhalt')
