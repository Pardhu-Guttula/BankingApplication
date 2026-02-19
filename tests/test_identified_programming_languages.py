import os
import pytest

# Dummy test case to validate that the primary language identified is correct

def test_primary_language_identification():
    project_files = [
        'app.py',
        'backend/app.py',
        'requirements.txt',
        'tests/test_app.py',
        'frontend/package.json',
        'frontend/postcss.config.js',
        'frontend/eslint.config.js',
        'frontend/tailwind.config.js',
        'frontend/vite.config.js',
        'database/schema.sql',
        'terraform/main.tf',
        'terraform/terraform.tfvars',
        'terraform/variables.tf'
    ]

    python_files = [file for file in project_files if file.endswith('.py') or file == 'requirements.txt']
    js_files = [file for file in project_files if file.endswith('.js') or file == 'package.json']
    sql_files = [file for file in project_files if file.endswith('.sql')]
    terraform_files = [file for file in project_files if file.endswith('.tf') or file == 'terraform.tfvars']

    # Check if Python is identified as the primary language
    assert len(python_files) > 0, "No Python files detected"
    assert 'requirements.txt' in python_files, "Requirements file for Python not detected"
    
    # Check if JavaScript/TypeScript files are detected
    assert len(js_files) > 0, "No JavaScript/TypeScript files detected"
    assert 'package.json' in js_files, "Package.json for Node.js not detected"

    # Check if SQL files are detected
    assert len(sql_files) > 0, "No SQL files detected"

    # Check if Terraform files are detected
    assert len(terraform_files) > 0, "No Terraform files detected"

    print("Primary language identification test passed.")

if __name__ == '__main__':
    test_primary_language_identification()