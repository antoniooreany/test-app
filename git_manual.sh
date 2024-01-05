#!/bin/bash
# todo does this work on windows?

# # Convert all the script files to unix format
# for file in $(find . -name "*.sh"); do
#     dos2unix $file



# Create a new branch for the script files
git checkout -b add-scripts

# Add and commit the script files
git add add_python_to_path.bat
git commit -m "Add add_python_to_path.bat script"

git add install_pyenv.sh
git commit -m "Add install_pyenv.sh script"

git add run_all_steps.sh
git commit -m "Add run_all_steps.sh script"

git add run_steps.sh
git commit -m "Add run_steps.sh script"

git add set_pycharm_interpreter.py
git commit -m "Add set_pycharm_interpreter.py script"

git add setup_env.sh
git commit -m "Add setup_env.sh script"