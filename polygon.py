class Polygon:
  def __init__(self, file_name):
    self.read_file(file_name)

  def read_file(self, file_name):
    def get_point(point_str):
      point = point_str.split("/")
      return int(point[0]) / int(point[1])
      
    file = open(file_name, 'r')
    line = file.readline().strip()
    parts = line.split()
    self.num_vertices = int(parts[0])
    self.vertices = []
    for i in range(1, len(parts), 2):
      first_point = get_point(parts[i])
      second_point = get_point(parts[i+1])
      self.vertices.append((first_point, second_point))

    print(self.num_vertices, self.vertices)
    