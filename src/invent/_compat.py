"""
Pyodide-compatible element factory functions replacing pyscript.web.

Each function creates a raw DOM element via js.document.createElement(),
sets properties from kwargs, and returns the JsProxy HTMLElement.

The `classes` kwarg accepts a list of CSS class names and adds each via
classList.add(), matching the pyscript.web factory signature.
"""
from js import document


def _make_element(tag, *args, **kwargs):
    el = document.createElement(tag)
    if args:
        for arg in args:
            if arg is None:
                continue
            if hasattr(arg, "nodeType"):
                el.appendChild(arg)
            else:
                el.appendChild(document.createTextNode(str(arg)))
    classes = kwargs.pop("classes", None)
    if classes:
        if isinstance(classes, str):
            el.classList.add(classes)
        else:
            for cls in classes:
                el.classList.add(cls)
    for k, v in kwargs.items():
        if k == "innerHTML":
            el.innerHTML = v
        elif k == "type":
            el.setAttribute("type", v)
        elif k in ("rel", "href", "src", "alt", "width", "height",
                   "datetime", "role", "for_"):
            el.setAttribute(k.rstrip("_"), v)
        else:
            setattr(el, k, v)
    return el


def div(*a, **kw): return _make_element("div", *a, **kw)
def button(*a, **kw): return _make_element("button", *a, **kw)
def input_(*a, **kw): return _make_element("input", *a, **kw)
def span(*a, **kw): return _make_element("span", *a, **kw)
def label(*a, **kw): return _make_element("label", *a, **kw)
def select(*a, **kw): return _make_element("select", *a, **kw)
def option(*a, **kw): return _make_element("option", *a, **kw)
def img(*a, **kw): return _make_element("img", *a, **kw)
def hr(*a, **kw): return _make_element("hr", *a, **kw)
def pre(*a, **kw): return _make_element("pre", *a, **kw)
def code(*a, **kw): return _make_element("code", *a, **kw)
def table(*a, **kw): return _make_element("table", *a, **kw)
def caption(*a, **kw): return _make_element("caption", *a, **kw)
def thead(*a, **kw): return _make_element("thead", *a, **kw)
def tbody(*a, **kw): return _make_element("tbody", *a, **kw)
def tr(*a, **kw): return _make_element("tr", *a, **kw)
def th(*a, **kw): return _make_element("th", *a, **kw)
def td(*a, **kw): return _make_element("td", *a, **kw)
def video(*a, **kw): return _make_element("video", *a, **kw)
def audio(*a, **kw): return _make_element("audio", *a, **kw)
def canvas(*a, **kw): return _make_element("canvas", *a, **kw)
def progress(*a, **kw): return _make_element("progress", *a, **kw)
def meter(*a, **kw): return _make_element("meter", *a, **kw)
def nav(*a, **kw): return _make_element("nav", *a, **kw)
def details(*a, **kw): return _make_element("details", *a, **kw)
def summary(*a, **kw): return _make_element("summary", *a, **kw)
def figure(*a, **kw): return _make_element("figure", *a, **kw)
def article(*a, **kw): return _make_element("article", *a, **kw)
def header(*a, **kw): return _make_element("header", *a, **kw)
def footer(*a, **kw): return _make_element("footer", *a, **kw)
def time(*a, **kw): return _make_element("time", *a, **kw)
def h2(*a, **kw): return _make_element("h2", *a, **kw)
def h3(*a, **kw): return _make_element("h3", *a, **kw)
def p(*a, **kw): return _make_element("p", *a, **kw)
def link(*a, **kw): return _make_element("link", *a, **kw)
def ul(*a, **kw): return _make_element("ul", *a, **kw)
def li(*a, **kw): return _make_element("li", *a, **kw)
def strong(*a, **kw): return _make_element("strong", *a, **kw)
