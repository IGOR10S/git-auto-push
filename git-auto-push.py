import subprocess

class color:
    OK = '\033[92m'       # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'     # RED
    OUT = '\033[90m'      # GRAY
    RESET = '\033[0m'     # RESET COLOR

def run_command(command):
    """Execute a shell command and return the output."""
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("\n" + color.FAIL + "ERROR: " + color.RESET + f"{e.stderr}")
        print("COMMAND: " + color.OUT + f"{e.cmd}" + color.RESET)
        print("\n" + color.WARNING + "WARNING: Error Code " + f"{e.returncode}" + color.RESET + f"\n{e.stdout}")
        return None
    
def git_status_files():
    """Returns a list of files."""
    print("Checking the status of files with '" + color.OUT + "git status --porcelain" + color.RESET + "'...")
    status_output = run_command(["git", "status", "--porcelain"])

    if not status_output:
        print(color.WARNING + "No files to add or edit." + color.RESET)
        return []

    # Extract files from state
    modified_files = []
    for line in status_output.splitlines():
        # The first two columns represent the file’s status (for example, 'M' for modified, '??' for untracked)
        status, file_path = line[:2], line[3:]
        
        # Consider files modified (M), added (A), deleted (D), renamed (R), copied (C), unmerged/conflicted (U), untracked (??)
        if status.strip() in ['M', 'A', 'D', 'R', 'C', 'U', '??', 'AD']:  # Add other states if necessary
            modified_files.append(file_path)

    if modified_files:
        print("Files modified or not tracked found:")
        for file in modified_files:
            print("\t" + color.OK + f"{file}" + color.RESET)
    else:
        print(color.WARNING + "No files edited or not tracked." + color.RESET)
    
    return modified_files

def git_add_files(file_paths):
    """Adds the specified files to commit."""
    for file in file_paths:
        # print("\t" + color.OK + f"\u2713 Added: {file}" + color.RESET) # For debugging checks
        run_command(["git", "add", file])

def git_commit_push(commit_message):
    """Create the commit and send it to the remote repository."""
    # Create the commit
    print(color.RESET + f"Creation of the commit: '{commit_message}'...")
    run_command(["git", "commit", "-m", commit_message])

    # Runs the push
    print("Running the push...")
    run_command(["git", "push", "origin", "main"])  # Make sure the branch is correct (e.g. 'main' or 'master')

def git_pull():
    """Pull the repository from remote to local."""
    print("Pull from the remote repository...")
    run_command(["git", "pull", "origin", "main"])  # Make sure the branch is correct

if __name__ == "__main__":
    # Runs the pull
    git_pull()
    
    # Get files from the git state
    file_paths = git_status_files()

    # If there are files, add them and commit
    if file_paths:    
        # Add the specified files
        git_add_files(file_paths)
        
        # Request the commit message
        commit_message = input("Message of the commit: " + color.OUT)
        
        # Create the commit and push
        git_commit_push(commit_message)
    else:
        print(color.WARNING + "No files to commit." + color.RESET)
