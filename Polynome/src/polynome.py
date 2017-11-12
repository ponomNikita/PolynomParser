from math import fabs

class Polynome:

    def __init__(self, cooefs):

        if (len(cooefs) == 0):
            raise Exception("cooefs must have one item at least")

        if (all(isinstance(elem, float) or isinstance(elem, int) for elem in cooefs) == False):
            raise Exception("All items must be instance of floating type")


        self.cooefs = cooefs

    def ToString(self):
        str = ""
        power = 0

        for i in reversed(self.cooefs):

            if power == 0 and i != 0:

                part = " + {0}".format(i) if i > 0 else " - {0:g}".format(fabs(i))
                str = "{0}{1}".format(part, str)
                power += 1

                continue

            if i != 0:

                part = ""
                cooef = ""

                if i < 0:
                    cooef = " - {0:g}".format(fabs(i))
                elif i > 0 and i != 1:
                    cooef = " + {0:g}".format(fabs(i))

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


