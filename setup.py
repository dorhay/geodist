import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geodist",
    version="0.1",
    author="Dor Hay",
    author_email="dorhay@gmail.com",
    description="GeoDist Package",
    url="https://github.com/dorhay/geodist",
    packages=setuptools.find_packages(),
    install_requires=["pyproj", "shapely"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
    ],
    python_requires='>=3.7',
)
