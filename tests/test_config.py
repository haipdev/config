import os.path
import pytest
import haip.config as config

base_dir = os.path.dirname(__file__)

def test_no_dir():
    with pytest.raises(config.HaipConfigException):            
        config.load('/no_directory_')

def test_no_env_dir():
    config_dir = os.sep.join((base_dir, 'etc_ok'))
    with pytest.raises(config.HaipConfigException):            
        config.load(config_dir, 'abc')

def test_load_notok():
    config_dir = os.sep.join((base_dir, 'etc_notok'))
    with pytest.raises(config.HaipConfigException):
        config.load(config_dir)

def test_load_ok():
    config_dir = os.sep.join((base_dir, 'etc_ok'))
    cfg = config.load(config_dir)
    assert cfg.lastname == 'Hainz'

def test_load_ok_overwrite():
    config_dir = os.sep.join((base_dir, 'etc_ok_overwrite'))
    cfg = config.load(config_dir, 'dev')
    assert cfg.lastname == 'Hainz2'

def test_get_section():
    config_dir = os.sep.join((base_dir, 'etc_ok'))
    config.load(config_dir)
    cfg = config.get('A', 'B', 'C')
    assert cfg.key1 == 'value1'

def test_get_option():
    config_dir = os.sep.join((base_dir, 'etc_ok'))
    config.load(config_dir)
    cfg = config.get('A', 'B', 'C', key1=config.MANDATORY)
    assert cfg.key1 == 'value1'

def test_get_option_notset():
    config_dir = os.sep.join((base_dir, 'etc_ok'))
    config.load(config_dir)
    with pytest.raises(config.HaipConfigException):
        config.get('A', 'B', 'C', key3=config.MANDATORY)    


