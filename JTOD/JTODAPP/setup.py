setup(
    name="JtoD-Converter",
    version="1.0.0",
    description="Converts json to Docxs for json files created with bookapp",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/101PANDA/nollydic-programs",
    author="Ogidi Favour",
    author_email="1ogidifavour@gmail.com",
    license="",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["JTODAPP"],
    include_package_data=True,
    install_requires=[
        "feedparser", "html2text", "importlib_resources", "typing"
    ],
    entry_points={"console_scripts": ["realpython=JTODAPP.__main__:main"]},
)