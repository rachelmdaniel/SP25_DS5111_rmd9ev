# SP25_DS5111_rmd9ev
Repository for Software and Automation Skills Class Spring 2025 - UVA MSDS

## Setting Up the VM

After connecting to the VM, run the following within the command line to update package information:
* sudo apt update

### Create SSH key and connect VM to your github:
* Paste the following line with the command line to create a new SSH key: 
    - ssh-keygen -t ed25519 -C your_email@example.com
* Press Enter to accept default file location and Enter again to not add a passphrase
* Sign-in to your Github account and click on your avatar.
* Click on Settings, then click on "SSH and GPG Keys" within the left-hand side menu.
* Click on "New SSH key" on the top right of the screen.
* Name the SSH key so that it matches your VM, for example, mine is called 25SP_rachel_rmd9ev.
* To view the SSH key, go back to your VM, and cat the contents of the pub side of the key:
    - cat id_ed25519.pub
* Paste the contents to the SSH key field and click "Add SSH key" below the Key field.
* Test that the SSH was successfully created using the following line:
    - ssh -T -i ed25519 gitgithub.com
    - You should see a message similar to this with your github username:
        - Hi rachelmdaniel! You've successfully authenticated, but GitHub does not provide shell access. 

### Set up global git credentials so you can git pull/push/clone:
* Execute the commands within the setup_git_global_creds shell file to set your global git credentials. Be sure to replace the USER and NAME with your email and git username


### Now that your github is connected to your VM, clone my repository to access scripts:
* git clone git@github.com:rachelmdaniel/SP25_DS5111_rmd9ev.git

* Checks:
    - use the ls command to make sure the repo was cloned
    - Run git config --global --list to make sure that your username and email are connected

### Run the init.sh script to finish setting up the VM:
* ./init.sh

