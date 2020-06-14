# Sons_Of_Ritz-Drones against fires
**Our team**

We are a group of year 1 students from multiple Schools, 2 from TP, 2 from NP and 1 from ACJC. This competition was a way we found to give back to the community whilst improving our coding skillset along the way as we are new to the coding scene and need the experience. Our team name is a homage to our first Computing and Programming teacher in secondary school which we always considered our coding 'father' of sorts as he never hesitated to offer us help when we needed it.

**Problem we are tackling**

With the rising tensions around global warming and its effect on the environment due to the recent wild/forest fires in australia, our team has decided to focus on the 'Preventing The Spread'. Specifically, we are tackling the issue of wild/forest fires that many believe will never hit Singapore. To do this, we will be utilising government data sets in python scripts to predict the months of the year that are more prone to fires and also configure drones with IBM visual recognition which patrol Singapores forest to detect fires as well as humans which are within the danger zone to assist the SCDF in their operations and help them carry them out more efficiently.

**Architecture of proposed solution**

https://photos.app.goo.gl/vwm6AguPoAmRy9LG6

**detailed solution**

https://docs.google.com/document/d/1XJRgSJeuc-ZwSZ1oMwl2mwZv7-DtSCtfE-PS7lufmJU/edit?ts=5ee4e98b

**Getting started**

To run the Python scripts, you will need to install python and the 'Requests' module
1. Install the latest version of python from https://www.python.org/downloads/
2. Use the shortcut 'Windows-R' and type in 'cmd' then press enter to open the command prompt
3. type in the command 'pip install requests' into the command prompt and wait for the 'Request' module to install
4. right click the python file and select 'edit with idle' then press F5 to save and run the program

To run the IBM Visual Recognition,you will need to go to https://dataplatform.cloud.ibm.com/home?context=wdp
1. Create a new project by clicking "New project*
2. "Create Project from existing files
3. Compile the files from Visual Recognition (assets, assettypes and project.json) into a zip file and drag and drop them into the page
4. Name the project and project description. Once done, hit create !
5. Go to settings and look for "Associated Service"
6. Click add service --> Watson -- Visual Recognition
7. Hit Test and now you can drag and drog any image for the trained AI to detect if there are any of the 3 labels (Fires, Smoke or Humans) in the picture.

**what our team used to build our solution**

1. Python
2. IBM Visual Recognition
3. Waze Navigation software
