import math
def calculate_angle(u, v):
    dot_product = sum(u_i * v_i for u_i, v_i in zip(u, v)
    magnitude_u = math.sqrt(sum(u_i**2 for u_i in u))
    magnitude_v = math.sqrt(sum(v_i**2 for v_i in v))
    cos_theta = dot_product / (magnitude_u * magnitude_v)
    theta_radians = math.acos(cos_theta)
    theta_degrees = math.degrees(theta_radians)
    return theta_degree
if __name__ == '__main__':
    input1 = input().strip().split()
    input2 = input().strip().split()
    u = list(map(float, input1))
    v = list(map(float, input2))
    angle = calculate_angle(u, v)
    print(f"{angle:.2f}")
