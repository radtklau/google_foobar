from fractions import Fraction
def answer(pegs):
    def find_rn(num):
        if num == 1:
            return 0
        else:
            return pegs[num-1]-pegs[num-2]-find_rn(num-1)

    ans = find_rn(len(pegs))
    if len(pegs)%2 == 0: #if it's even
        if ans >= 3/2:
            f = Fraction(ans*2, 3)
            radius = f.numerator/f.denominator * 1.0
            for i in range(0, len(pegs)-2): #make sure the radii of the circles in the middle still satisfy conditions
                width = pegs[i+1]-pegs[i]
                if radius < 0 or radius > width-1:
                    return [-1, -1]
                radius = width - radius
            return [f.numerator, f.denominator]
        else:
            return [-1, -1]
    else:
        if ans <= -1/2:
            f = Fraction(ans*(-2), 1)
            radius = f.numerator/f.denominator * 1.0
            for i in range(0, len(pegs)-2): #make sure the radii of the circles in the middle still satisfy conditions
                width = pegs[i+1]-pegs[i]
                if radius < 0 or radius > width-1:
                    return [-1, -1]
                radius = width - radius
            return [f.numerator, f.denominator]
        else:
            return [-1, -1]