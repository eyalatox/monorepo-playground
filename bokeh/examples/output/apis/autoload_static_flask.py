from flask import Flask, Response

app = Flask(__name__)
port = 8878

def render_plot():
    import numpy as np

    from bokeh.embed import autoload_static
    from bokeh.plotting import figure
    from bokeh.resources import CDN

    N = 4000
    x = np.random.random(size=N) * 100
    y = np.random.random(size=N) * 100
    radii = np.random.random(size=N) * 1.5
    colors = np.array([(r, g, 150) for r, g in zip(50+2*x, 30+2*y)], dtype="uint8")

    TOOLS="crosshair,pan,wheel_zoom,box_zoom,reset,tap,save,box_select,poly_select,lasso_select"

    p = figure(tools=TOOLS)

    p.scatter(x, y, radius=radii,
              fill_color=colors, fill_alpha=0.6,
              line_color=None)

    js, tag = autoload_static(p, CDN, f"http://localhost:{port}/plot.js")

    html = f"""
    <html>
        <head>
            <title>color_scatter example</title>
        </head>
        <body>
            {tag}
        </body>
    </html>
    """

    return html, js

html, js = render_plot()

@app.route('/plot.html')
def plot_html():
    return html

@app.route('/plot.js')
def plot_js():
    return Response(js, mimetype='text/javascript')

if __name__ == "__main__":
    app.run(port=port)
