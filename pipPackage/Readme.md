# Webshell_write
This is a pip package when installed will write php webshell to the `/var/www/html` webroot directory

## Setup
Install the dependency for `Python3`
```
python3 -m pip install --user --upgrade setuptools wheel
```
Build the package
```
python3 setup.py sdist bdist_wheel
```
> NOTE: The command will also try to create a webshell at `/var/www/html` and might throw some error if the user does not have permission to write to the directory or the file has already exist

After running the command, you will find a file with the name of `webshell_write-0.0.0.tar.gz` under `dist`.

If a user install the file using `pip install webshell_write-0.0.0.tar.gz` a PHP webshell will be installed on the machine if that user has permission to write to `/var/www/html`
