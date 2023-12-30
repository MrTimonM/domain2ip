import os

def upload_to_github():
    # Get the repository URL from the user
    repo_url = input("Enter the GitHub repository URL: ")

    # Configure Git user identity globally
    os.system('git config --global user.name "MrTimonM"')
    os.system('git config --global user.email "notarealemail@hehe.com"')

    # Initialize Git repository
    os.system("git init")

    # Add all files in the current directory
    os.system("git add .")

    # Commit changes
    os.system('git commit -m "Initial commit"')

    # Add remote repository
    os.system(f"git remote add origin {repo_url}")

    # Push changes to GitHub
    os.system("git push -u origin master")

if __name__ == "__main__":
    upload_to_github()

    # Keep the script running until the user presses Enter
    input("Press Enter to exit...")
