from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name="alerta-monitis",
    version=version,
    description='Alerta webhook for Monitis',
    url='https://github.com/dsmatilla/alerta-contrib',
    license='MIT',
    author='Daniel S. Matilla',
    author_email='daniel@esdis.es',
    packages=find_packages(),
    py_modules=['alerta_monitis'],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'monitis = alerta_monitis:MonitisWebhook'
        ]
    }
)