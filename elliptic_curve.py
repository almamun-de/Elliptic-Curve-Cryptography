# elliptic_curve.py

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, x, y):
        """Check if the point (x, y) lies on the curve y^2 = x^3 + ax + b (mod p)."""
        return (y**2 - (x**3 + self.a * x + self.b)) % self.p == 0

    def point_addition(self, P, Q):
        """Add two points P and Q on the elliptic curve."""
        if P == Q:
            return self.point_doubling(P)
        
        x1, y1 = P
        x2, y2 = Q
        m = (y2 - y1) * pow(x2 - x1, -1, self.p) % self.p
        x3 = (m**2 - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def point_doubling(self, P):
        """Double a point P on the elliptic curve."""
        x1, y1 = P
        m = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p) % self.p
        x3 = (m**2 - 2 * x1) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        return (x3, y3)


