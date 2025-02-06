#!/bin/bash

# Clean previous coverage data
echo "Cleaning previous coverage data..."
coverage erase

# Run tests with coverage
echo "Running tests with coverage..."
pytest

# Generate reports
echo "Generating coverage reports..."
coverage html
coverage xml

# Display coverage report in terminal
echo -e "\nCoverage Summary:"
coverage report

# Open HTML report if on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    open coverage_html/index.html
fi

echo -e "\nCoverage reports generated:"
echo "- HTML report: coverage_html/index.html"
echo "- XML report: coverage.xml"
echo "- Terminal report displayed above"
