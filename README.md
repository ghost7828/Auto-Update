# Auto-Update
with this script is possible to update specific folder from remote host

**Version python used 3.11.4**

**1**-Install with your prompt the requirements:
 pip install -r requirements.txt

Important!! For use Cx freeze you need install Microsoft C++ Build Tools (Install the package Development app with C++)

**2**-Write your host address in the Update.py (You can use xaamp or hostweb)

**3**-Open PowerShell as administrator and write this in the folder where you have the setup.py :

python setup.py build  (Important you need cx_Freeze)

**4**-Copy the build files and folders:
lib
share
python3.dll
python311.dll
Update.exe

**5**-Put the folders and files in your folders to update


**6**-Compressed your files with Compressor zip.bat (You need install 7-zip)
