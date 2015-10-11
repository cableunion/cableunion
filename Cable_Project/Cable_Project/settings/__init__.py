import platform
if platform.uname()[0] == 'Windows':
    from dev import *
elif platform.uname()[0] == 'Mac':
    from dev import *
else:
    from prod import *
