from bokeh.io import save
from bokeh.layouts import row
from bokeh.plotting import figure


def make_figure(output_backend):
    p = figure(width=400,
               height=400,
               output_backend=output_backend,
               title=f"Backend: {output_backend}")

    p.circle(x=[1, 2, 3], y=[1, 2, 3], radius=0.25, color="blue", alpha=0.5)
    p.annulus(x=[1, 2, 3], y=[1, 2, 3], inner_radius=0.1, outer_radius=0.20, color="orange")

    return p

canvas = make_figure("canvas")
webgl  = make_figure("webgl")
svg    = make_figure("svg")

save(row(canvas, webgl, svg))
