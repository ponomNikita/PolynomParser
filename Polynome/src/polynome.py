from math import fabs

class Polynome:

    def __init__(self, cooefs):

        if (len(cooefs) == 0):
            raise Exception("cooefs must have one item at least")

        if (all(isinstance(elem, float) or isinstance(elem, int) for elem in cooefs) == False):
            raise Exception("All items must be instance of floating type")


        self.cooefs = cooefs[::-1]

    def ToString(self):
        str = ""
        power = 0

        for i in self.cooefs:

            if power == 0 and i != 0:

                part = " + {0}".format(i) if i > 0 else " - {0:g}".format(fabs(i))
                str = "{0}{1}".format(part, str)
                power += 1

                continue

            if i != 0:

                part = ""
                cooef = ""

                if i < 0 and i != -1:
                    cooef = " - {0:g}".format(fabs(i))
                elif i == -1:
                    cooef = " - "
                elif i > 0 and i != 1:
                    cooef = " + {0:g}".format(fabs(i))
                elif i == 1:
                    cooef = " + "

                if (power == 0):
                    part = "{0}".format(cooef)
                elif (power == 1):
                    part = "{0}x".format(cooef)
                else:
                    part = "{0}x^{1}".format(cooef, power)

                str = "{0}{1}".format(part, str)

            power += 1

        if str.startswith(" "):
            str = str[1:]

        if str.startswith("+ "):
            str = str[2:]

        if str == "":
            str = "0"

        return str

    def __add__(self, other):
        new_cooefs = []

        if len(self.cooefs) >= len(other.cooefs):
            new_cooefs = self.sum(self.cooefs, other.cooefs)
        else:
            new_cooefs = self.sum(other.cooefs, self.cooefs)

        return Polynome(new_cooefs[::-1])

    def sum(self, beggerList, lessList):
        result = []

        for i in range(0, len(lessList)):
            result.append(beggerList[i] + lessList[i])

        if (len(beggerList) > len(lessList)):
            result.extend(beggerList[-len(beggerList) + len(lessList):])

        return result

    def __sub__(self, other):
        return self.__add__(other * -1)

    def __mul__(self, other):

        if isinstance(other, int) or isinstance(other, float):
            new_cooefs = [i * other for i in self.cooefs]
            return Polynome(new_cooefs[::-1])

        if isinstance(other, Polynome):
            result = [0]*(len(self.cooefs) + len(other.cooefs) - 1)
            for selfpow, selfco in enumerate(self.cooefs):
                for valpow, valco in enumerate(other.cooefs):
                    result[selfpow + valpow] += selfco * valco

            return Polynome(result[::-1])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):

        if not isinstance(other, Polynome):
            return NotImplemented

        if len(self.cooefs) != len(other.cooefs):
            return False

        for i in range(0, len(self.cooefs)):
            if self.cooefs[i] != other.cooefs[i]:
                return False

        return True

    def __ne__(self, other):

        result = self.__eq__(other)

        if result == NotImplemented:
            return result

        return not result




