#!/usr/bin/env python3

from flask import Flask, render_template, send_from_directory, safe_join
from flaskrun import flaskrun
import os

app = Flask(__name__)
app.jinja_env.filters['dirname'] = os.path.dirname
app.jinja_env.filters['basename'] = os.path.basename


@app.route("/", defaults={'filename': "."})
@app.route("/<path:filename>")
def serve_gallery(filename):
    if os.path.isdir(filename):
        return serve_directory(filename)
    else:
        return serve_file(filename)

def serve_file(filename):
    """Show a raw file."""
    return send_from_directory(os.getcwd(), filename)

def is_image(filename):
    """Check if the file is an image (judging by the extension)."""
    extensions = ["." + ext for ext in "jpg jpeg gif png".split()]
    identity = lambda x: x
    modifiers = [identity, str.upper]
    for ext in extensions:
        for mod in modifiers:
            if filename.endswith(mod(ext)):
                return True
    return False

def serve_directory(dirname):
    """Show a gallery."""
    all_files = set(safe_join(dirname, f) for f in os.listdir(dirname))
    directories = set(filter(os.path.isdir, all_files))
    images = set(filter(is_image, all_files))
    regular_files = all_files - images - directories

    template_args = {
        'directories': sorted(directories),
        'files': sorted(regular_files),
        'all': sorted(all_files),
        'images': sorted(images),
        'dirname': dirname,
        'appname': app.name,
    }

    return render_template(
        "index.html",
        **template_args,
    )

if __name__ == '__main__':
    flaskrun(app, threaded=True)
