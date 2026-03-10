"""
The core classes, objects and utility functions of the Invent framework.

Based on original pre-COVID work by [Nicholas H.Tollervey.](https://ntoll.org/)

Copyright (c) 2019-present Invent contributors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from invent._compat import link
from js import document
from .channels import Message, subscribe, publish, unsubscribe, when
from .datastore import DataStore, IndexDBBackend
from .i18n import _, load_translations
from .media import Media, set_media_root, get_media_root
from .app import App
from .utils import show_page, is_micropython

__all__ = [
    "Message",
    "subscribe",
    "publish",
    "unsubscribe",
    "when",
    "datastore",
    "_",
    "load_translations",
    "Media",
    "set_media_root",
    "get_media_root",
    "App",
    "show_page",
    "is_micropython",
    "go",
    "init",
    "marked",
]


#: Default instance of the application's datastore.
datastore = None
#: The default name for the datastore
datastore_name = "invent"


async def start_datastore(_backend=None, **kwargs):
    """
    Ensure the datastore is started and referenced properly.
    """
    global datastore
    if not datastore:
        if _backend is None:
            backend_instance = None
        elif _backend == IndexDBBackend:
            # IndexDBBackend not available in Pyodide runtime; fall back to default.
            backend_instance = None
        else:
            backend_instance = _backend()
        datastore = DataStore(_backend=backend_instance, **kwargs)


#: The marked JavaScript module for parsing markdown.
marked = None
#: The DOMPurify JavaScript module for sanitising HTML.
purify = None
#: The leaflet JavaScript module for mapping.
leaflet = None
#: The chart.js JavaScript module for charting.
chart_js = None


async def load_js_modules():
    """
    No-op in Pyodide runtime. JS modules are loaded externally.
    """
    return


#: The root from which all media files can be found.
media = Media([], "media")


async def setup(_databackend=None, **kwargs):
    """
    Setup all the things required by the Invent framework (e.g. datastore).

    Takes optional start values for the datastore. The _databackend argument
    can be used to specify the storage backend for the datastore. If not
    provided, the default storage backend is used. Any other keyword arguments
    are passed to the datastore's start method as initial values to seed the
    datastore.
    """
    await start_datastore(_databackend, **kwargs)


def go():
    """
    Start the app.
    """
    App.app().go()
