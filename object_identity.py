"""
In der Theorie haben Sie gelernt, wie mit der Methode isinstance die
Zugehörigkeit eines Objekts zu einer Klasse festgestellt werden kann
und wie mit dem Operator is geprüft wird, ob Referenzen identisch sind.
Der folgende Code geht noch ein bisschen weiter. Sie sollen den Code
studieren und sein Verhalten erklären. Dazu kann es notwendig sein,
dass Sie sich über passende Suchbegriffe im Internet "schlau" machen.
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
        Vergleicht zwei Objekte auf deren Inhalt, sodass sie mit dem
        ==-Operator verglichen werden können.
        Diese Methode ist implizit für jedes Objekt verfügbar und kann
        überschrieben werden, um den gewünschten Effekt des Vergleichs
        zu bekommen.

        Es soll dabei Folgendes möglich sein:
        - Zwei Instanzen von ObjectIdentity sind gleich, wenn ihr Attribut
          'text' denselben Wert hat.
        - Zusätzlich soll es möglich sein, eine Instanz direkt mit einem
          String zu vergleichen. In diesem Fall gilt das Objekt als gleich,
          wenn der String mit dem Attribut 'text' übereinstimmt.
        """
        pass


if __name__ == "__main__":
    # erzeugen Sie hier 2 Objekt obj1 und obj2 der Klasse ObjectIdentity.
    # TODO

    ##
    # prüfen der Klassenzugehörigkeit von obj1 zur Klasse ObjectIdentity
    # Geben Sie je nach Testergebnis einen passenden Text aus.
    # TODO

    ##
    # prüfen Sie, ob die beiden Objekte obj1 und obj2 identisch sind.
    # Geben Sie je nacht Testergebnis einen passenden Text aus.
    # TODO

    ##
    # prüfen Sie hier den Inhalt (das Attribut) der beiden Objekte auf Gleichheit.
    # Beachten Sie dazu auch die Hinweise in der Methode __eq__
    # TODO
    pass
