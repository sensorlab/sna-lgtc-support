from distutils.core import setup

setup(
    name='VidekClient',
    version='0.1dev',
    packages=['videkrestclient',],
    scripts = ['videk-client'],
    data_files = [('/etc/videk', ['api.key'])]
)
