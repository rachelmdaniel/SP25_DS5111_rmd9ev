# SP25_DS5111_rmd9ev
Repository for Software and Automation Skills Class Spring 2025 - UVA MSDS

## Setting Up the VM

After connecting to the VM, run the following within the command line to update package information:
* sudo apt update

### Create SSH key and connect VM to your github:
* Paste the following within the command line to create a new SSH key: 
    - `ssh-keygen -t ed25519 -C your_email@example.com`
* Press Enter to accept default file location and Enter again to not add a passphrase
* Sign-in to your Github account and click on your avatar.
* Click on Settings, then click on "SSH and GPG Keys" within the left-hand side menu.
* Click on "New SSH key" on the top right of the screen.
* Name the SSH key so that it matches your VM, for example, mine is called 25SP_rachel_rmd9ev.
* To view the SSH key, go back to your VM, and cat the contents of the pub side of the key:
    - `cat id_ed25519.pub`
* Paste the contents to the SSH key field and click "Add SSH key" below the Key field.
* Test that the SSH was successfully created using the following line:
    - `ssh -T -i ed25519 gitgithub.com`
    - You should see a message similar to this with your github username:
        - Hi rachelmdaniel! You've successfully authenticated, but GitHub does not provide shell access. 

### Set up global git credentials so you can git pull/push/clone:
* Execute the following commands to set up your global git credentials. Be sure to replace the USER and NAME with your email and git username.
	- ```bash
	  !#/usr/bin/bash

	  USER=rachelmdaniel3@gmail.com
	  NAME=rachelmdaniel

	  git config --global --list

	  git config --global user.email ${USER} 
	  git config --global user.name  ${NAME} 

	  git config --global –list
	  ``` 

### Now that your github is connected to your VM, clone my repository to access my scripts for future steps found within my scripts directory:
* `git clone git@github.com:rachelmdaniel/SP25_DS5111_rmd9ev.git`

* Checks:
    - use the `ls` command to make sure the repo was cloned
    - Run `git config --global --list` to make sure that your username and email are connected

### Execute the init.sh script within the scripts directory to finish initiating the VM:
* `./init.sh`

### Add tools and functionality for pipeline:
* Install Chrome headless browser within your VM using the code found within the install_chrome_headless.sh script. Check that it’s working correctly using example.com, using the script provided at the bottom of the shell file.
* A makefile and requirement.txt file can be found within the scripts directory also. They will be used to set up automation.
	- Optional: Enter `make` within the command line to get an overview of the file
	- Enter `make update` to update the dependencies using the requirement.txt file (only need pandas and lxml for now).

### Testing Chrome headless browser:
* Enter your environment by entering the following on the command line (there should be a space in between the period and the e):
	- `. env/bin/activate`
* To test the headless browser, run one (or both) of the following lines:
	- `make ygainers.csv` 
	- `make wjsgainers.csv`
	- Note: an example of the ygainers.csv file can be found within the sample_data directory 
* The csv files (along with the html files) should appear within your list of files in your remote repository when you use the ls command.
* Lastly, run the following line to see the structure of your repository: `tree <path to your project repo> -I env`
	- You should see a tree similar to this:
	- ```bash
	   ├── LICENSE
	   ├── README.md
	   ├── google-chrome-stable_current_amd64.deb
	   ├── init.sh
	   ├── install_chrome_headless.sh
	   ├── makefile
	   ├── requirements.txt
	   ├── setup_git_global_creds.sh
	   ├── wsjgainers.csv
	   ├── wsjgainers.html
	   ├── ygainers.csv
	   └── ygainers.html
	  ```	

 
