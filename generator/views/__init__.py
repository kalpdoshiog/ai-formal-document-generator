"""
Re-export all views so that ``from . import views`` and
``views.home``, ``views.generate_body``, etc. keep working
without touching urls.py imports.
"""

from .home import home  # noqa: F401

from .office_order import (  # noqa: F401
    generate_body,
    result_office_order,
    download_pdf,
    download_docx,
)

from .circular import (  # noqa: F401
    generate_circular_body,
    result_circular,
    download_circular_pdf,
    download_circular_docx,
)

from .policy import (  # noqa: F401
    generate_policy_body,
    result_policy,
    download_policy_pdf,
    download_policy_docx,
)
