

## Build rust

```
$ cargo build
```


## Build python binding

1. build wheel first

```bash
$ pip install  --index-url="https://pypi.org/simple/" setuptools-rust wheel build
$ python -m build
```


2. Once you get the wheel, you can install the wheel by

```bash
$ pip install <path to wheel>
```

3. If you want to develop python code in editable mode, you can do 

```bash
$ pip install -e .
```

Note that every time you change rust, you have to build the wheel again


### Setting up Python Binding and CI

The CI consists of three steps

1. Build wheels

- We use cibuildwheel to build a manylinux x86_64 pkg which can work on major Linux OS (Ubuntu, Centos, etc)
- To support other OS / architecture, we can add more configs 

Reference: https://cibuildwheel.pypa.io/en/stable/

2. Build source distribution

- Create source distribution which contains raw and unbuilt code
- This allows `pip` to build pacakge from source if there are no prebuilt wheels

3. Publish to PyPi

The CI setup is refered from https://github.com/openai/tiktoken/blob/63527649963def8c759b0f91f2eb69a40934e468/.github/workflows/build_wheels.yml#L1