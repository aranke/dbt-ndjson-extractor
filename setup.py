from setuptools import setup


setup(
    name='dbt-random-node',
    version='1',
    py_modules=['dbt_random_node'],
    entry_points={
        'dbt.custom_node': ['randomizer=dbt_random_node:RandomNode'],
    },
)
