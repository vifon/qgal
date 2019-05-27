#!/usr/bin/env python3

from PIL import Image
from flask import Flask, render_template, send_from_directory, safe_join, redirect, send_file
from flaskrun import flaskrun
from io import BytesIO
import mimetypes
import os

try:
    from natsort import natsorted as sort
except ImportError:
    sort = sorted

app = Flask(__name__)


@app.route("/")
def serve_root():
    return redirect("/qgal/")

@app.route("/qgal/", defaults={'filename': "."})
@app.route("/qgal/<path:filename>/")
def serve_gallery(filename='/'):
    if os.path.isdir(filename):
        return serve_directory(filename)
    else:
        return serve_file(filename)

@app.route("/thumb/<path:filename>")
def serve_thumb(filename):
    """Show a thumbnail or a raw file if it's not an image."""
    with open(filename, 'r+b') as f:
        with Image.open(f) as image:
            image.thumbnail((768, 1024))
            img_io = BytesIO()
            image.convert('RGB').save(img_io, 'JPEG', quality=70)
            img_io.seek(0)
            return send_file(img_io, mimetype='image/jpeg')

def serve_file(filename):
    """Show a raw file."""
    return send_from_directory(os.getcwd(), filename)

def is_image(filename):
    """Check if the file is an image (judging by the extension)."""
    mimetype, encoding = mimetypes.guess_type(filename)
    return mimetype is not None and mimetype.startswith("image/")

def serve_directory(dirname):
    """Show a gallery."""
    all_files = set(safe_join(dirname, f) for f in os.listdir(dirname))
    directories = set(map(os.path.basename, filter(os.path.isdir, all_files)))
    images = set(map(os.path.basename, filter(is_image, all_files)))
    regular_files = set(map(os.path.basename, all_files)) - images - directories

    template_args = {
        'directories': sort(directories),
        'files': sort(regular_files),
        'all': sort(all_files),
        'images': sort(images),
        'dirname': dirname,
        'appname': app.name,
    }

    return render_template(
        "index.html",
        **template_args
    )

if __name__ == '__main__':
    flaskrun(app, threaded=True)
