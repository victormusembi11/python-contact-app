"""Utilities for the config package."""
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_env_variable(var_name) -> str or None:
    """Get an environment variable or raise an exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise Exception(error_msg)


def get_bool_env(env_var) -> bool:
    """Parse 'boolean' environment variable strings."""
    return os.getenv(env_var, "False") == "True"
