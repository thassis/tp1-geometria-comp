import plotly.graph_objs as go
from polygon import Polygon
from triangle import Triangle
from ear_clipping import check_in_triangle, ear_clipping

def plot_polygon_and_triangles(polygon, triangles):
  vertices = polygon.vertices
  polygon_x = [v[0] for v in vertices] + [vertices[0][0]]
  polygon_y = [v[1] for v in vertices] + [vertices[0][1]]
  
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=polygon_x, y=polygon_y, mode='lines+markers', name='Polygon'))
  
  for triangle in triangles:
    tri_x = [triangle.a[0], triangle.b[0], triangle.c[0], triangle.a[0]]
    tri_y = [triangle.a[1], triangle.b[1], triangle.c[1], triangle.a[1]]
    fig.add_trace(go.Scatter(x=tri_x, y=tri_y, mode='lines+markers', name='Triangle'))

  fig.update_layout(title='Polygon and Triangulation',
    xaxis_title='X',
    yaxis_title='Y',
    showlegend=True)
  
  return fig.to_html()

if __name__ == "__main__":    
  polygon = Polygon("./instances/agp2007-minarea/min-20-1.pol")
  triangles = ear_clipping(polygon)

  html_content = plot_polygon_and_triangles(polygon, triangles)

  with open("polygon_and_triangles2.html", "w", encoding="utf-8") as file:
    file.write(html_content)
