@Echo off
@ECHO %3
@ECHO "Uninstalling Old Application......."
@ECHO.           
@ECHO.
adb -d uninstall  %2
@ECHO.           
@ECHO.
@ECHO "Installing New Application......."
@ECHO.           
@ECHO.
adb install %3
@ECHO.           
@ECHO.
@ECHO Start Testing...........................
@ECHO.           
@ECHO.
@ECHO "Application Forground for 15 Second -- Sending First Event......."
@ECHO.           
@ECHO.
adb shell am start -n %1
TIMEOUT  15
@ECHO.           
@ECHO.
@ECHO "Application Background for 30 Second"
@ECHO.           
@ECHO.
adb shell input keyevent 3
TIMEOUT  30
@ECHO.           
@ECHO.
@ECHO "Application Forground for 45 Second"
@ECHO.           
@ECHO.
adb shell am start -n %1
TIMEOUT  45
@ECHO.           
@ECHO.
@ECHO "Application Background for 20 Second"
@ECHO.           
@ECHO.
adb shell input keyevent 3
TIMEOUT  20
@ECHO.           
@ECHO.
@ECHO "KILLING APPLICATION AND WAIT FOR 50 Seconds"
@ECHO.           
@ECHO.
adb shell am force-stop %2
TIMEOUT  50
@ECHO.           
@ECHO.
@ECHO "Application On Forground -- Sending Second Event"
adb shell am start -n %1
TIMEOUT  10
@ECHO.           
@ECHO.
@ECHO "First Application testing Finishing"
adb shell am force-stop %2
@ECHO.           
@ECHO.
move %4 "completed apps"


