; 脚本由 Inno Setup 脚本向导 生成！
; 有关创建 Inno Setup 脚本文件的详细资料请查阅帮助文档！

[Setup]
; 注: AppId的值为单独标识该应用程序。
; 不要为其他安装程序使用相同的AppId值。
; (若要生成新的 GUID，可在菜单中点击 "工具|生成 GUID"。)
AppId={{06F7D88F-8D7F-42CA-A08A-C0B9991E405E}
AppName=Clathon
AppVersion=1.20.8
;AppVerName=Clathon 1.20.8
AppPublisher=Hardy
AppPublisherURL=Clathon
AppSupportURL=Clathon
AppUpdatesURL=Clathon
DefaultDirName={autopf}\Clathon
ChangesAssociations=yes
DefaultGroupName=Clathon
AllowNoIcons=yes
LicenseFile=J:\Clathon\LICENSE
; 以下行取消注释，以在非管理安装模式下运行（仅为当前用户安装）。
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputBaseFilename=Clathon_Setup
SetupIconFile=J:\Clathon\Icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "chinesesimp"; MessagesFile: "compiler:Default.isl"
Name: "english"; MessagesFile: "compiler:Languages\English.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "turkish"; MessagesFile: "compiler:Languages\Turkish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "J:\Clathon\dist\Clathon\Clathon.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; 注意: 不要在任何共享系统文件上使用“Flags: ignoreversion”

[Registry]
Root: HKA; Subkey: "Software\Classes\.py;.cla;.spy\OpenWithProgids"; ValueType: string; ValueName: "Clathon文件.py;.cla;.spy"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\Clathon文件.py;.cla;.spy"; ValueType: string; ValueName: ""; ValueData: "Clathon 文件"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\Clathon文件.py;.cla;.spy\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\Clathon.exe,0"
Root: HKA; Subkey: "Software\Classes\Clathon文件.py;.cla;.spy\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\Clathon.exe"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\Clathon.exe\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{group}\Clathon"; Filename: "{app}\Clathon.exe"
Name: "{group}\{cm:UninstallProgram,Clathon}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Clathon"; Filename: "{app}\Clathon.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Clathon.exe"; Description: "{cm:LaunchProgram,Clathon}"; Flags: nowait postinstall skipifsilent

