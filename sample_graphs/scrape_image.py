# Downloads an image from a remote HTTP server and saves it to a local file

from datamodel.base import graph
from datamodel.nodes.lib import files, value, http


def scraper_image(img_url, target_path):
    url = value.Value(value=img_url)
    client = http.Get(mime_type='image/png', )
    writer = files.BinaryFileWriter(filepath=target_path)

    g = graph.Graph('scrape_image', [url, client, writer])

    g.connect(writer, client, 'data')
    g.connect(client, url, 'url')

    return g
