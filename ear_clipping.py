from triangle import Triangle

def direction(p1, p2, p3):
  x1, y1 = p1
  x2, y2 = p2
  x3, y3 = p3
  return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

def on_segment(p1, p2, p3):
  return min(p1[0], p2[0]) <= p3[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p3[1] <= max(p1[1], p2[1])

def segments_intersect(p1, p2, p3, p4):
  d1 = direction(p3, p4, p1)
  d2 = direction(p3, p4, p2)
  d3 = direction(p1, p2, p3)
  d4 = direction(p1, p2, p4)

  if((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3>0 and d4 < 0) or (d3 < 0 and d4 >0)):
    return 1
  elif d1 == 0 and on_segment(p3, p4, p1):
    return 1
  elif d2 == 0 and on_segment(p3, p4, p2):
    return 1
  elif d3 == 0 and on_segment(p1, p2, p3):
    return 1
  elif d4 == 0 and on_segment(p1, p2, p4):
    return 1
  else:
    return 0

def check_in_triangle(point, triangle):
  point_segment = (point[0], 0) #traca uma reta vertical do ponto até o y 0, já que o menor valor de y nos arquivos é 1
  intercepts_1 = segments_intersect(point, point_segment, triangle.a, triangle.b)
  intercepts_2 = segments_intersect(point, point_segment, triangle.a, triangle.c)
  intercepts_3 = segments_intersect(point, point_segment, triangle.b, triangle.c)
  interceptions = intercepts_1 + intercepts_2 + intercepts_3
  
  return (interceptions % 2) != 0

def check_convex(vertex1, vertex2, vertex3) -> bool:
  x1, y1 = vertex1
  x2, y2 = vertex2
  x3, y3 = vertex3
  cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
  return cross_product >= 0


def check_ear(vertex1, vertex2, vertex3, vertices) -> bool:
  triangle = Triangle(vertex1, vertex2, vertex3)
  for vertex in vertices:
    if vertex not in (vertex1, vertex2, vertex3):
      if check_in_triangle(vertex, triangle):
        return False
  return True

def ear_clipping(polygon):
  triangles = []
  vertices = polygon.vertices

  while len(vertices) > 3:
    for i in range(len(vertices)):
      vertex1 = vertices[i-1]
      vertex2 = vertices[i]
      vertex3 = vertices[i+1]

      if check_convex(vertex1, vertex2, vertex3) and check_ear(vertex1, vertex2, vertex3, vertices):
        triangle = Triangle(vertex1, vertex2, vertex3)
        triangles.append(triangle)
        vertices.remove(vertex2)
        break

  triangle = Triangle(vertices[0], vertices[1], vertices[2])
  triangles.append(triangle)
  return triangles
  