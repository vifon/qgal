qgal — quick gallery
====================

`qgal` was intended as a `python3 -m http.server` focused on images.
It serves the current directory via HTTP (by default on
`0.0.0.0:5000`) with the previews of all the images in it. The served
directory tree is fully browsable so be aware of what you're
serving/sharing. It is mostly designed for a local and/or LAN usage,
as it does not resize the images for the thumbnails, they are
downscaled client-side. It may change in the future or not.

Some of `qgal`'s goals:
- [X] an easy to use web-based image browser
- [X] a mobile version
- [X] responsive design
- [X] it should never modify any local files; completely stateless operation
- [X] minimal dependencies: Python 3 and Flask

What can to be improved:
- [ ] server-side image downscaling for the previews
- [ ] partial/range HTTP requests for audio/video streaming

Installation
------------

1. Clone this repository:

```
$ git clone https://github.com/vifon/qgal
```

2. Place a symlink to the `run.sh` wrapper in your `$PATH`, for example:

```
# ln -s /path/to/qgal/run.sh /usr/local/bin/qgal
```

3. Run `qgal` wherever it is needed!


Copyright
---------

Copyright (C) 2017  Wojciech Siewierski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
