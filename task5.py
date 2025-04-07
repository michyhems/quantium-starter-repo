from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

from task4 import app

def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#header", "Sales of Pink Morsels over time", timeout=4)

def test_visualisation(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#example-graph", timeout=4)

def test_region_picker(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radio", timeout=4)
