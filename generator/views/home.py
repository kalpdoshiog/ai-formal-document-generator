"""
Home view.
"""
from django.shortcuts import render

from ..data.constants import DESIGNATION_MAP
from ..services.data_loader import get_circular_data


def home(request):
    circular = get_circular_data()
    return render(request, "generator/home.html", {
        "designations": DESIGNATION_MAP.keys(),
        "people": circular.get("people", []),
    })
