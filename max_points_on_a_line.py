# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def gcd(self, a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
        while b:
            a, b = b, a%b
        return a

    def reduce(self, a, b):
        if a == 0 and b == 0:
            return (0, 0)
        if a == 0:
            return (0, 1)
        if b == 0:
            return (1, 0)
        divisor = self.gcd(a, b)
        return (a / divisor, b / divisor)

    def maxPoints(self, points):
        max_points = 0
        for point_a in points:
            freq = {}
            for point_b in points:
                delta_x, delta_y = self.reduce(point_a.x-point_b.x, point_a.y-point_b.y)
                if not (delta_x, delta_y) in freq:
                    freq[(delta_x, delta_y)] = 1
                else:
                    freq[(delta_x, delta_y)] += 1
            tangents = [freq[i] for i in freq if i != (0, 0)]
            n_otherpoints = max(tangents) if len(tangents) else 0
            npoints = n_otherpoints + freq[(0, 0)]
            if max_points < npoints:
                max_points = npoints
        return max_points

pointlist = [(0,9),(138,429),(115,359),(115,359),(-30,-102),(230,709),(-150,-686),(-135,-613),(-60,-248),(-161,-481),(207,639),(23,79),(-230,-691),(-115,-341),(92,289),(60,336),(-105,-467),(135,701),(-90,-394),(-184,-551),(150,774)]
points = []
for p in pointlist:
    points.append(Point(p[0], p[1]))
s = Solution()
print s.maxPoints(points)
