import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):
    if len(points) == 2:
        return points[0], points[1]
    if len(points) == 1:
        return None

    sorted_points = sorted(points, key=lambda p: p[0])
    mid = len(sorted_points) // 2
    left_closest_pair = closest_pair(sorted_points[:mid])
    right_closest_pair = closest_pair(sorted_points[mid:])

    if left_closest_pair is None:
        min_distance = distance(right_closest_pair[0], right_closest_pair[1])
    elif right_closest_pair is None:
        min_distance = distance(left_closest_pair[0], left_closest_pair[1])
    else:
        min_distance = min(distance(left_closest_pair[0], left_closest_pair[1]), distance(right_closest_pair[0], right_closest_pair[1]))

    closest_across_split = None
    x_mid = sorted_points[mid][0]
    strip = [point for point in sorted_points if abs(point[0] - x_mid) < min_distance]
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            current_distance = distance(strip[i], strip[j])
            if current_distance < min_distance:
                min_distance = current_distance
                closest_across_split = strip[i], strip[j]

    if closest_across_split:
        return closest_across_split
    else:
        if left_closest_pair and distance(left_closest_pair[0], left_closest_pair[1]) <= distance(right_closest_pair[0], right_closest_pair[1]):
            return left_closest_pair
        else:
            return right_closest_pair

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
closest = closest_pair(points)
p1, p2 = closest
print(f"Closest pair: {closest}")
print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"Distance:{distance(p1,p2)}")
