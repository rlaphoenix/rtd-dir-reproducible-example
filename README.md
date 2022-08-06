This is a reproducible example for https://github.com/sphinx-contrib/images/pull/31

Root error seems to be caused somewhat by sphinxcontrib-youtube v1.2.0 specifically.

Build error log:

```
Running Sphinx v4.5.0
loading translations [en]... done
making output directory... done
Initiated sphinxcontrib-images backend: `sphinxcontrib_images_lightbox2.lightbox2:LightBox2`
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 1 source files that are out of date
updating environment: [new config] 1 added, 0 changed, 0 removed
reading sources... [100%] index

Downloading remote images...[ 20%] https://www.lipsum.com/images/banners/black_234x60.gif
https://www.lipsum.com/images/banners/black_234x60.gif -> /home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/checkouts/latest/docs/_images/7843118d28263d43152f8e1380b7a9c50c0a38dd (downloading)
Downloading remote images...[ 40%] https://www.lipsum.com/images/banners/grey_234x60.gif
https://www.lipsum.com/images/banners/grey_234x60.gif -> /home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/checkouts/latest/docs/_images/c419a2ad7676d87e6fddae63ce7b3e2914908948 (downloading)
Downloading remote images...[ 60%] https://www.lipsum.com/images/banners/white_234x60.gif
https://www.lipsum.com/images/banners/white_234x60.gif -> /home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/checkouts/latest/docs/_images/24e5061ca764d033cde60a7b0c29ed6fceeb9865 (downloading)
Downloading remote images...[ 80%] https://vumbnail.com/657905289.jpg
https://vumbnail.com/657905289.jpg -> /home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/checkouts/latest/docs/_video_thumbnail/657905289.jpg (downloading)
/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/checkouts/latest/docs/index.rst:: WARNING: image file not readable: _images/7843118d28263d43152f8e1380b7a9c50c0a38dd
/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/checkouts/latest/docs/index.rst:: WARNING: image file not readable: _images/c419a2ad7676d87e6fddae63ce7b3e2914908948
/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/checkouts/latest/docs/index.rst:: WARNING: image file not readable: _images/24e5061ca764d033cde60a7b0c29ed6fceeb9865

Traceback (most recent call last):
  File "/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/envs/latest/lib/python3.8/site-packages/sphinx/events.py", line 94, in emit
    results.append(listener.handler(self.app, *args))
  File "/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/envs/latest/lib/python3.8/site-packages/sphinxcontrib/images.py", line 256, in download_images
    with open(dst, 'wb') as f:
FileNotFoundError: [Errno 2] No such file or directory: '/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/checkouts/latest/docs/_video_thumbnail/657905289.jpg'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/envs/latest/lib/python3.8/site-packages/sphinx/cmd/build.py", line 276, in build_main
    app.build(args.force_all, filenames)
  File "/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/envs/latest/lib/python3.8/site-packages/sphinx/application.py", line 330, in build
    self.builder.build_update()
  File "/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/envs/latest/lib/python3.8/site-packages/sphinx/builders/__init__.py", line 286, in build_update
    self.build(to_build,
  File "/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/envs/latest/lib/python3.8/site-packages/sphinx/builders/__init__.py", line 300, in build
    updated_docnames = set(self.read())
  File "/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/envs/latest/lib/python3.8/site-packages/sphinx/builders/__init__.py", line 413, in read
    for retval in self.events.emit('env-updated', self.env):
  File "/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/envs/latest/lib/python3.8/site-packages/sphinx/events.py", line 102, in emit
    raise ExtensionError(__("Handler %r for event %r threw an exception") %
sphinx.errors.ExtensionError: Handler <function download_images at 0x7f94ce18e820> for event 'env-updated' threw an exception (exception: [Errno 2] No such file or directory: '/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/checkouts/latest/docs/_video_thumbnail/657905289.jpg')

Extension error (sphinxcontrib.images):
Handler <function download_images at 0x7f94ce18e820> for event 'env-updated' threw an exception (exception: [Errno 2] No such file or directory: '/home/docs/checkouts/readthedocs.org/user_builds/rtd-dir-reproducible-example/checkouts/latest/docs/_video_thumbnail/657905289.jpg')
```