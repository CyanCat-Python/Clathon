; �ű��� Inno Setup �ű��� ���ɣ�
; �йش��� Inno Setup �ű��ļ�����ϸ��������İ����ĵ���

[Setup]
; ע: AppId��ֵΪ������ʶ��Ӧ�ó���
; ��ҪΪ������װ����ʹ����ͬ��AppIdֵ��
; (��Ҫ�����µ� GUID�����ڲ˵��е�� "����|���� GUID"��)
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
; ������ȡ��ע�ͣ����ڷǹ���װģʽ�����У���Ϊ��ǰ�û���װ����
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
; ע��: ��Ҫ���κι���ϵͳ�ļ���ʹ�á�Flags: ignoreversion��

[Registry]
Root: HKA; Subkey: "Software\Classes\.py;.cla;.spy\OpenWithProgids"; ValueType: string; ValueName: "Clathon�ļ�.py;.cla;.spy"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\Clathon�ļ�.py;.cla;.spy"; ValueType: string; ValueName: ""; ValueData: "Clathon �ļ�"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\Clathon�ļ�.py;.cla;.spy\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\Clathon.exe,0"
Root: HKA; Subkey: "Software\Classes\Clathon�ļ�.py;.cla;.spy\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\Clathon.exe"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\Clathon.exe\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{group}\Clathon"; Filename: "{app}\Clathon.exe"
Name: "{group}\{cm:UninstallProgram,Clathon}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Clathon"; Filename: "{app}\Clathon.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Clathon.exe"; Description: "{cm:LaunchProgram,Clathon}"; Flags: nowait postinstall skipifsilent

