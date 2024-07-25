
env = {}
"""This Dict is set by internal.check_env_vars and contains a subset of the environment relevant to this
application.  If a value isn't provided in the environment, check_env_vars will populate a reasonable
default.  In turn, components of this application can refer to env[] to retrieve global settings to
bootstrap. 
"""