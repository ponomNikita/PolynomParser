from math import fabs

class Polynome:

    def __init__(self, cooefs):
        self.cooefs = cooefs

    def ToString(self):
        str = ""
        power = 0

        for i in reversed(self.cooefs):
            if i != 0:
                part = ""
                cooef = ""

                if i < 0:
                    cooef = " - {0:g}".format(fabs(i))
                elif i > 1:
                    cooef = " + {0:g}".format(fabs(i))


                if (power == 0):
                    part = "{0}".format(cooef)
                elif (power == 1):
                    part = "{0}x".format(cooef)
                else:
                    part = "{0}x^{1}".format(cooef, power)

                str = "{0}{1}".format(part, str)

            power += 1

        if str.startswith(" + ") or str.startswith(" - "):
            str = str[3:]

        return str

