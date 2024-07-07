import plotly.graph_objs as go

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
  
  def plot_polygon(self, output_file='polygon.html'):
    x_values = [vertex[0] for vertex in self.vertices]
    y_values = [vertex[1] for vertex in self.vertices]

    x_values.append(self.vertices[0][0])
    y_values.append(self.vertices[0][1])

    fig = go.Figure(data=[go.Scatter(x=x_values, y=y_values, mode='lines+markers', name='Polygon')])

    fig.update_layout(
        title='Polygon',
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        showlegend=True
    )

    fig.write_html(output_file, auto_open=True)


    