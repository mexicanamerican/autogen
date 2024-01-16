from importlib.metadata import version as lib_version
from datetime import datetime
import os
import autogen
import json


def init():
    """Helper function to initialize logging in a testbed scenario.
    Specifically, write timestamp and version information, then
    initialize autogen logging.

    Args:
        None

    Returns:
        None
    """

    # Check and create necessary files and directories for logging functionality
    with open("timestamp.txt", "wt") as f:
        f.write("Timestamp: " + datetime.now().isoformat() + "\n")
        f.write("pyautogen version: " + lib_version("pyautogen") + "\n")


def finalize(logger, agents):
    """Helper function to finalize logging in a testbed scenario.
    Calling this function will save all the chat completions logged
    by Autogen to disk, and will save the messages dictionaries of
    all agents passed via the agents argument.

    Args:
        agents (list): a list of the agents whose messages will be logged to disk.

    Returns:
        None
    """

    script_dir = os.path.dirname(os.path.realpath(__file__))
    try:
        os.mkdir(os.path.join(script_dir, 'logs'))
    except Exception as e:
        logger.exception('An error occurred while creating the logs directory')

    def messages_to_json(agent):
        messages = dict()
        for item in agent.chat_messages.items():
            messages[item[0].name] = item[1]
        return json.dumps(messages, indent=4)

    for agent in agents:
        fname = agent.name + "_messages.json"
        with open(os.path.join(script_dir, fname), "wt") as fh:
            fh.write(messages_to_json(agent))
