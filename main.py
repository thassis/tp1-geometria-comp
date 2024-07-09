import plotly.graph_objs as go
from polygon import Polygon
from triangle import Triangle
from ear_clipping import check_in_triangle, ear_clipping

def plot_polygon(polygon):
  vertices = polygon.vertices
  print(len(vertices))
  fig = go.Figure()
  for vertex in vertices:
    x_values = [vertex[0] for vertex in vertices]
    y_values = [vertex[1] for vertex in vertices]

    x_values.append(vertices[0][0])
    y_values.append(vertices[0][1])

    fig = go.Figure(data=[go.Scatter(x=x_values, y=y_values, mode='lines+markers', name='Polygon')])

    fig.update_layout(
        title='Polygon',
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        showlegend=True
    )
    return fig

if __name__ == "__main__":    
  polygon = Polygon("./instances/agp2007-minarea/min-20-1.pol")
  triangles = ear_clipping(polygon)

  fig = plot_polygon(polygon)

  html_content = fig.to_html()

  with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)
