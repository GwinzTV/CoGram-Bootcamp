# if a folder called new_folder exists in the current directory, make another folder called if_folder
if [ -d new_folder ]; then
    mkdir if_folder
fi
# if a folder called if_folder exists in the current directory, make a new folder called hyperionDev
# else if not, make a new folder called new-projects
if [ -d if_folder ]; then
    mkdir hyperionDev
else
    mkdir new-projects
fi