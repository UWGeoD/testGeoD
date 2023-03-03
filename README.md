# GitHub Tutorial
repository tutorial
check [github skills](https://skills.github.com/)

## Repository: organizes single project
### *creating a repository*
  1. Use "+" to create "New repository"
  2. Enter name
  3. Write description
  4. Add README file [(uses Markdown language)](https://www.markdownguide.org/cheat-sheet/)
  5. Select Public or Private
  6. Create repository
  
## Branch: different versions of repository
  - Default main branch
  - Allows for copy to be made for editing
  - Can later be merged to main branch
  - Create a new branch for unrelated changes
### *creating a branch*
  1. Click code tab or repository
  2. Click dropdown menu "main"
  3. Type new branch name
  4. Click "Create branch: ... from main"
### *making and committing  changes*
  1. Select file
  2. Edit file
  3. Write message in Commit changes box to describe change
  4. Click Commit changes
  
## Pull Requests: proposing changes and requesting review
  - Contributions to be merged into a branch
  - Changes are shown in different colors
  - Can open a pull request even before code is done, once a commit is made
  - @mention targets people for feedback
### *opening a pull request*
  1. Click on Pull requests tab
  2. Click New pull request
  3. Select branches to be compare in Example Comparisons box
  4. Look over changes and click Create pull request
  5. Give request a title and description, option to assign options on right
  6. Click Create pull request
### *merging a pull request*
  1. Resolve conflicts if any
  2. Click Merge pull request and Confirm merge
  3. Click Delete branch
  
## Set up [Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
will allow us to store repositories locally on computer and push commits and pull requests
### *cloning a repository (downloads to local files)*
  1. open GitBash
  2. type "git clone <HTTPS URL>"
  3. the folder will be copied to the current directory
### *updating main branch*
  1. git init "directory"
  2. cd "directory"
  3. git remote add origin https:// (remote respository allows for variable name connection to website)
  4. git add "file"
  5. git commit -m "add file commit"
  6. git push --set-upstream origin(remote) main(branch)
### *creating a branch for pull request*
  1. git init "directory"
  2. cd "directory"
  3. git remote add origin https:// (remote respository allows for variable name connection to website)
  4. git branch newBranch (creates new branch)
  5. git checkout newBranch (changes to newBranch)
  6. git add "file"
  7. git commit -m "add file commit"
  8. git push --set-upstream origin newBranch
  9. git remote remove origin (to remove name "origin" from connection)
### *updating local files from GitHub repository*
  1. git init "directory"
  2. cd "directory"
  3. git remote add origin https:// (remote respository allows for variable name connection to website)
  4. git pull origin main
  
### *[Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo?tool=webui)*
  - Allows you to clone a repository from Github on browser and locally
  - Can set to sync with upstream repository
  
## Sharing an environment
### *creating an environment*
  1. open anaconda prompt
  2. conda create --name myenv
  3. conda install -n myenv python (list packages and versions)
  4. conda env list (to see all environments)
  5. conda activate myenv
  6. conda list (to see packages in environment)
### *exporting an environment*
  1. conda activate myenv
  2. conda env export > environment.yml (creates environment file in base directory)
  OR
  2. conda env export --from-history > allPlatformsEnvironment.yml (to only include added packages) *better method*
### *importing an environment*
  1. conda env create -f environment.yml (or local path name)
  2. conda activate myenv
  

## Communicating
  1. GitHub Issues
    - tasks, bugs, specific feedback
  2. Pull requests
    - propose specific changes
  3. GitHub Discussions
    - open forum between repositories
  4. Team discusssions
    - team conversation between projects

## Look at codespaces for integration with spyder
