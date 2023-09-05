# Authors: Rodrigo Leite <drigols.creative@gmail.com>
#
# License: MIT
# ============================================================================
"""Testing file."""
from __future__ import annotations

from jsp.database.connections import get_engine_connection

if __name__ == "__main__":
    pass

    # Testing connection.
    engine = get_engine_connection()
    print("Testing connection:")
    print("Returned value:", engine)
    print("Returned value type:", type(engine))
