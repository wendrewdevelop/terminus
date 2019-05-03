# -*- coding: utf-8 -*-

__name__ = 'kwconfig'
__author__ = 'Richard Wen'
__email__ = 'rrwen.dev@gmail.com'
__version__ = '1.1.7'
__license__ = 'MIT'
__description__ = 'A Python module for managing config files in keyword style json format.'
__keywords__ = [
  'manage',
  'config',
  'keyword',
  'key',
  'word',
  'value',
  'keyvalue',
  'json',
  'file',
  'path',
  'module']
__url__ = 'https://github.com/rrwen/kwconfig'
__download_url__ = 'https://github.com/rrwen/kwconfig/archive/master.zip'
__packages__ = ['kwconfig']

from os.path import isfile
from pprint import pprint

import argparse
import json

class manage:
  """Manage configuration files in keyword style JSON format.
  
  Notes:
    Creates a configuration file with the ``defaults`` if the ``file_path`` does not exist.
    
  Args:
    file_path (str):
      Path to the configuration file in JSON format.
    defaults (dict):
      Dictionary of a default keyword dict.
  
  Attributes:
    file_path (str):
      Path to the configuration file in JSON format.
  
  Examples::
    
    # Import the kwconfig module
    import kwconfig
    
    # Specify a file path for creating config object
    config = kwconfig.manage('config.json', defaults={'key0': 'value0'})
    
    # Update the config file with a key and value dict
    config.update({'key1': 'value1', 'key2': 'value2'})
    
    # Add a keyword dict to existing config file
    # If a key exists, it will be updated
    # If a key does not exist, it will be added
    other_config = {'key3': 'value3'}
    other_config = config.add(other_config)
    
    # Write new values using keyword dict
    config.overwrite({
      'new_key1': 'new_value1',
      'new_key2': 'new_value2'
    })
    
    # Obtain a dict of the config file contents
    kw = config.read()
    
    # Remove the key named "key1"
    config.remove('key1')
    
    # Reset to defaults
    config.reset()
    
    # Send commands to run
    
    # Set default key and value
    config.command(['-s', 'new_key1=newvalue1'], i=0)
    
    # Remove default key
    config.command(['-r', 'new_key1'], i=0)
    
    # Print defaults
    config.command(['-v'], i=0)
    
    # Reset defaults
    config.command(['-d'], i=0)
  """
  def __init__(
    self,
    file_path, 
    defaults={}):
    self.file_path = file_path
    self.defaults = defaults
    if not isfile(file_path):
      self.reset()
      
  def add(self, other_config):
    """Add default arguments to another configuration dictionary.
    
    Adds the default arguments from :class:`kwconfig.manage`.file_path 
    to another configuration dictionary if it is not already set.
    
    Args:
      other_config (dict):
        The other configuration dictionary of keyword arguments.
        
    Return:
      A dict of the combined and updated config file. 
    """
    for k, v in self.read().items():
      if k not in other_config:
        other_config[k] = v
    return other_config
    
  def command(self, argv, i=0, doc='', quit=True, silent=False):
    """Consume a list of arguments and execute commands.
    
    Runs a kwconfig method based on item ``i`` in ``argv``:
    
    * ``['-h']`` or ``[]``: show ``doc`` text
    * ``['-s', '<arg>=<value>']``: set default optional arguments
    * ``['-r', '<arg>']``: remove default arguments
    * ``['-v']``: view default arguments
    * ``['-d']``: reset default arguments
    
    Args:
      argv (listof str):
        A list of str arguments to execute commands (e.g. from the command line).
      doc (str):
        String containing the help documentation to print out on the command line interface when using
        ``-h`` or not entering any commands or arguments.
      quit (bool):
        Whether to quit if a command is executed (if a command is not found, it will not exit).
      silent (bool):
        Whether to suppress messages (True) or allow them (False).
    """
    consumed = False
    
    # (command) Execute methods
    if len(argv) > 1:
      if argv[i] == '-h':
        print(doc) # show help
        consumed = True
      elif argv[i] == '-s': # set defaults
        k, v = argv[i+1].split("=", 1)
        self.update({k: v})
        print('\n Set "' + k + '" default to ' + '"' + v + '"')
        consumed = True
      elif argv[i] == '-r': # remove defaults
        self.remove(argv[i+1])
        print('\n Removed "' + argv[i+1] + '" default')
        consumed = True
      elif argv[i] == '-v': # show defaults
        print('\n Config file at: \n ' + self.file_path + '\n\n ')
        pprint(self.read())
        exit()
      elif argv[i] == '-d': # reset defaults
        self.reset()
        print('\n Reset defaults')
        consumed = True
    else:
      print(doc)
      exit()
      
    # (end) End commands with messsage and quit if command
    if consumed and quit:
      exit()
  
  def overwrite(self, new_config):
    """Overwrite default arguments for configuration file.
    
    Overwrites the contents of :class:`kwconfig.manage`.file_path with ``new_config``.
    
    Args:
      new_config (dict):
        The new default arguments as a keyword dictionary.
    """
    with open(self.file_path, 'w') as out_file:
      json.dump(new_config, out_file)
      
  def read(self):
    """Read default arguments from configuration file.
    
    Reads the configuration file content into a keyword dictionary.
    
    Returns:
      A dict of the default arguments from :class:`kwconfig.manage`.file_path.
    """
    with open(self.file_path, 'r') as in_file:    
      config = json.load(in_file)
    return config
  
  def remove(self, k):
    """Remove keys from configuration file.
    
    Removes a key from :class:`kwconfig.manage`.file_path.
    
    Args:
      k (str):
        The key to remove from :class:`kwconfig.manage`.file_path.
    """
    config = self.read()
    config.pop(k, None)
    self.overwrite(config)
    
  def reset(self):
    """Reset keyword values for configuration file.
    
    Resets the contents of :class:`kwconfig.manage`.file_path with :class:`kwconfig.manage`.defaults.
    """
    with open(self.file_path, 'w') as out_file:
      json.dump(self.defaults, out_file)
    
  def update(self, arguments):
    """Update keyword values for configuration file.
    
    Updates the contents of :class:`kwconfig.manage`.file_path with ``arguments``.
    
    Args:
      arguments (dict):
        Keyword dict to use as an update.
    """
    config = self.read()
    config.update(arguments)
    self.overwrite(config)
    
def parse(argv):
  """Parse optional list of keyword arguments into a dict.
  
  Parses a list of keyword arguments defined by a leading ``--`` and separated by ``=`` (for example, --key=value).
  
  Args:
    argv (listof str):
      Keyword dict to use as an update.
  
  Examples::
  
    # Import the kwconfig module
    import kwconfig
    
    # Create a sample list of keyword arguments
    argv = ['--key1=value1', '--key2=value2']
    
    # Parse into a keyword dict
    kwdict = kwconfig.parse(argv)
    
    # View the values of key1 and key2
    print('key1: ' + kwdict['key1'])
    print('key2: ' + kwdict['key2'])
  """
  kwdict = {}
  for kv in argv:
    k, v = kv.split('=', 1)
    kwdict[k.strip('-')] = v
  return(kwdict)
    
