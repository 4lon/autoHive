# autoHive
 A python script to automatically make 3D models compatible with the Hive Evo storage system

## Steps
### 0. Purchase
This project is built of Daniel O'Connell's Hive Evo design, this script will not work without the relevant cad files when you purchase his design: https://cults3d.com/en/3d-model/home/the-hive-evo

### 1. Installation
Run this script to install the necessary dependency:
    pip install --upgrade pywin32==225

Note: I'm not sure why it has to be this version, it's possible it would work with others however mine would not

## Credits
### u/dable82 
For the basic Autodesk Inventor API script that started this project:
https://www.reddit.com/r/InventorAPI/comments/b6ihwq/using_python_with_inventor_api/

### Mod the Machine
A lot of the Inventor API resources I used are from this website. Specifically this page https://modthemachine.typepad.com/my_weblog/2009/03/running-commands-using-the-api.html although written for VBA I managed to translate it into Python and get some of these features working