import subprocess
import os


# todo GOOD IDEA, BUT COULD YOU, IN THAT CASE NOT TO FOLLOW THAT STRICT RULES IN ORDERING/DISTREBUTION WITH THE LOOPS, DEPENDENT ON EXTENTIONS, BUT CONSIDERING OUR CURRENT PROJECT FILE SET, ITS CONTENT, TIME OF CREATION ETC., DOING THIS JOB 'MANUALLY', CONSIDERING EACH FILE WITH ITS SET OF PROPERTIES. WRIGHT THAT KIND OF SCRIPT
def run_git_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing command: {command}")
        print(stderr.decode())
    return stdout.decode()


def main():
    # Define the root directory of your project
    root_dir = os.getcwd()  # replace with the actual path

    # Define the branches
    branches = {
        'scripts': ['.bat', '.sh'],
        'src': ['.py'],
        'docs': ['.md'],
        'config': ['.json'],
    }

    # Walk through each file in the project
    for root, _, files in os.walk(root_dir):
        for file in files:
            # Get the file extension
            _, extension = os.path.splitext(file)

            # Find the branch for this file extension
            for branch, extensions in branches.items():
                if extension in extensions:
                    # Create a new branch
                    run_git_command(['git', 'checkout', '-b', f'add-{file.replace(".", "-")}'])

                    # Add the file to the branch
                    run_git_command(['git', 'add', os.path.join(root, file)])

                    # Commit the change
                    run_git_command(['git', 'commit', '-m', f'Add {file}'])

                    # Push the branch to the remote repository
                    run_git_command(['git', 'push', 'origin', f'add-{file.replace(".", "-")}'])

                    # Checkout to the main branch
                    run_git_command(['git', 'checkout', 'main'])


if __name__ == "__main__":
    main()
