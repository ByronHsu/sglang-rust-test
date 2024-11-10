from setuptools import setup, find_packages
from setuptools_rust import Binding, RustExtension

setup(
    name="sglang-rust-test",
    version="0.1.0",
    packages=find_packages(where="py_src"),
    package_dir={"": "py_src"},
    rust_extensions=[
        RustExtension(
            "hello_world_rs",
            path="Cargo.toml",
            binding=Binding.PyO3,
            debug=False,
        )
    ],
    zip_safe=False,
    python_requires=">=3.7",
)