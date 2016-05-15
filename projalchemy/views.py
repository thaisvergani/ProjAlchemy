import cgi
import re
from docutils.core import publish_parts

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )
from pyramid.renderers import render_to_response

from pyramid.view import view_config

from .models import (
    DBSession,
    Page,
    )

# regular expression used to find WikiWords
wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

@view_config(route_name='view_home')
def view_home(request):
    return render_to_response(
        renderer_name='projalchemy:templates/home.pt',
        value='',
        request=request,
        package=None,
        response=None
    )
