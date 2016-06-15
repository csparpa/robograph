# Downloads an image from a remote HTTP server and saves it to a local file

from datamodel.base import graph
from datamodel.nodes import files, value
from datamodel.nodes.quick import http


def scraper_image(img_url, target_path):
    http_params = dict(url=img_url, output_encoding='binary')
    v = value.Value(http_params)
    h = http.Get()
    w = files.BinaryFileWriter(target_path)

    g = graph.Graph('scrape_image', [v, h, w])

    g.connect(w, h)
    g.connect(h, v)

    return g
