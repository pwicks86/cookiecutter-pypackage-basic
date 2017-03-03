import os

license_type = '{{ cookiecutter.package_license }}'

if license_type == "None":
    os.remove("LICENSE")
