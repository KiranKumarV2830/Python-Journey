# Virtual Environment : A virtual Environment is an isolated, self-contained Python setup for a specific project. It has its own copy of Python and its own separate set of installed packages, completely separate from your system-wide Python and from other project's environments . 

# Why it matters : Imagine Project A needs pandas version 1.0 but Project B needs pandas version 2.0 without virtual enviornments, installing one would break the other, since there'd only be one shared version on your system . Virtual enviornments solve this by giving each project its own isolated "bubble"

# Creating a Virtual Environment - venv : venv is python built-in module for creating virtual environments . No installlation needed - it ships with python

# Example(in terminal)
# python -m venv myenv

# Activating a Virtual Environment : Activating 'switches into" the virtual environment , so any package you install or python command you run uses that environment instead of your system python

# myenv\Scripts\activate

# Deactivating a Virtual Environment : Exists the virtual environment and returns you to your normal system Python . 

# deactivate

# pip : pip is python's package installer - it downloads and installs third-party libraries(like numpy,pandas,requests) from PyPI(Python Package Index), so you can import them in your code.

# pip install requests

# import requests
# response = requests.get("https://google.com")

# Installing a Specific Version : You can pin a package to an exact version, useful when your project depends on specific behaviour that might break in newer version 

# pip install pandas==2.0

# Uninstalling a Package : Removes an installed package from your current environment . 

# pip uninstall requests

# Listing Installed Packages : Shows every package currently installed in your active environment, along with version numbers.

# pip list

# requirements.txt : A text file listing all the packages(and versions) a project needs. This lets anyone else- or you, on a different machine -recreate the exact same environment with one command .

# pip freeze > requirements.txt

# and to install in the new machine 

# pip install -r requirements.txt

