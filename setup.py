from setuptools import setup


setup(
    name="dbt-ndjson-extractor",
    version="1",
    py_modules=["dbt_ndjson_extractor"],
    entry_points={
        "dbt.extractor": ["dbt-ndjson-extractor=dbt_ndjson_extractor:NDJSONExtractor"],
    },
    install_requires=["agate"],
)
