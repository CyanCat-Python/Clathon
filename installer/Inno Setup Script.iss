; 脚本由 Inno Setup 脚本向导 生成！
; 有关创建 Inno Setup 脚本文件的详细资料请查阅帮助文档！

[Setup]
; 注: AppId的值为单独标识该应用程序。
; 不要为其他安装程序使用相同的AppId值。
; (若要生成新的 GUID，可在菜单中点击 "工具|生成 GUID"。)
AppId={{7DA78FD6-5C1D-4C31-AC16-00FF7AE7485D}
AppName=Clathon
AppVersion=1.20.7
;AppVerName=Clathon 1.20.6
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
OutputDir=J:\Clathon\installer
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
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "J:\Clathon\dist\Clathon\Clathon.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_asyncio.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_ctypes.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_decimal.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_elementtree.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_multiprocessing.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_overlapped.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_queue.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\_tkinter.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-console-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-datetime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-debug-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-errorhandling-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-file-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-file-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-file-l2-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-handle-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-interlocked-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-libraryloader-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-localization-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-memory-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-namedpipe-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-processenvironment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-processthreads-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-processthreads-l1-1-1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-profile-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-rtlsupport-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-synch-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-synch-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-sysinfo-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-timezone-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-core-util-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-conio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-convert-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-environment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-filesystem-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-locale-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-math-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-private-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-process-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-runtime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-stdio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-time-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\api-ms-win-crt-utility-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\Clathon.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\libcrypto-1_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\libffi-8.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\libssl-1_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\python311.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\tcl86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\tk86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\ucrtbase.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "J:\Clathon\dist\Clathon\VCRUNTIME140_1.dll"; DestDir: "{app}"; Flags: ignoreversion
; 注意: 不要在任何共享系统文件上使用“Flags: ignoreversion”

[Registry]
Root: HKA; Subkey: "Software\Classes\.py;.pyw;.cla\OpenWithProgids"; ValueType: string; ValueName: "Clathon文件.py;.pyw;.cla"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\Clathon文件.py;.pyw;.cla"; ValueType: string; ValueName: ""; ValueData: "Clathon 文件"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\Clathon文件.py;.pyw;.cla\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\Clathon.exe,0"
Root: HKA; Subkey: "Software\Classes\Clathon文件.py;.pyw;.cla\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\Clathon.exe"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\Clathon.exe\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{group}\Clathon"; Filename: "{app}\Clathon.exe"
Name: "{autodesktop}\Clathon"; Filename: "{app}\Clathon.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Clathon.exe"; Description: "{cm:LaunchProgram,Clathon}"; Flags: nowait postinstall skipifsilent

