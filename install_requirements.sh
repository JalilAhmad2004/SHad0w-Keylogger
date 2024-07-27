#!/bin/bash

# Function to check if a Python package is installed
is_package_installed() {
    python3 -c "import pkg_resources; pkg_resources.require('$1')" &> /dev/null
}

# List of required Python packages
REQUIRED_PACKAGES=("pynput" "requests" "pyfiglet")

# Install missing packages
for package in "${REQUIRED_PACKAGES[@]}"; do
    if ! is_package_installed "$package"; then
        echo "Installing $package..."
        pip3 install "$package"
    else
        echo "$package is already installed."
    fi
done

# Run the Python script
python3 key.py
