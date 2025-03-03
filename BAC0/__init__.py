#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import bacpypes
except ImportError:
    # Using print here or setup.py will fail
    print("=" * 80)
    print(
        'bacpypes module missing, please install latest version using \n    $ "pip install bacpypes"'
    )
    print("\nDiscard this message if you are actually installing BAC0.")
    print("=" * 80)

try:
    from . import core
    from . import tasks
    from .scripts.Base import Base
    from .core.devices.Device import Device as device
    from .core.devices.Device import DeviceLoad as load
    from .core.devices.Trends import TrendLog as TrendLog
    from .tasks.Poll import SimplePoll as poll
    from .tasks.Match import Match as match
    from .core.utils.notes import update_log_level as log_level
    from .infos import __version__ as version

    # To be able to use the complete version pandas, flask and bokeh must be installed.
    try:
        import pandas
        import bokeh
        import flask
        import flask_bootstrap

        _COMPLETE = True
    except ImportError:
        _COMPLETE = False

    if _COMPLETE:
        from .scripts.Complete import Complete as connect
        from .scripts.Lite import Lite as lite
    else:
        from .scripts.Lite import Lite as connect

        lite = connect
        # print('All features not available as some modules are missing (flask, flask-bootstrap, bokeh, pandas). See docs for details')

except ImportError as error:
    print("=" * 80)
    print(
        'Import Error, refer to documentation or reinstall using \n    $ "pip install BAC0"\n {}'.format(
            error
        )
    )
    print("\nDiscard this message if you are actually installing BAC0.")
    print("=" * 80)
    # Probably installing the app...
