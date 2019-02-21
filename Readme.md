# haip.config

haip.config is a simple configuration handling module for Python 3.6+. You define your project configuration in yaml-files and haip.config handles the rest for you.

### Features: 

* **directory based**: place your config in multiple files in your configuration directory. haip.config will merge them automatically.
* **environment overlay**: place your environment specific configuration in a subdirectory. haip.config will overwrite the base configuration.
* **attribute-style**: access your config like a.b.c instead of a['b']['c']

## Getting Started

### Installing

```
pip install haip.config
```
or from source:
```
git clone https://github.com/haipdev/config.git
```
### Example:

#### config-files:

/path-to-my-config-dir/databases.yml
```
databases:
    test:
        username: testuser        
        host: 127.0.0.2
```
/path-to-my-config-dir/dev/databases.yml
```
databases:
    test:
        password: testpassword        
```
#### python implementation

```
import haip.config as config

config.load('/path-to-my-config-dir', 'dev')
cfg = config.get('databases', 'test', username=config.MANDATORY, password=config.MANDATORY,  host='127.0.0.1', port=3306)

username = cfg.databases.test.username   # <-- 'testuser' from base-config
password = cfg.databases.test.password   # <-- 'testpassword' from dev subdir
host = cfg.databases.test.host           # <-- '127.0.0.2' from base-config (default not used)
port = cfg.databases.test.port           # <-- 3306 from default
```

## Running the tests

Tests are written using pytest and located in the "tests" directory.
```
pytest tests
```

## Contributing

Feel free to use and enhance this project. Pull requests are welcome.

## Authors

* **Reinhard Hainz** - *Initial work* - [haipdev](https://github.com/haipdev)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* https://github.com/hackebrot/poyo 