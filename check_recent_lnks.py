import os, glob

recent_dir = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Recent")
print("Recent directory:", recent_dir)

try:
    import win32com.client
    shell = win32com.client.Dispatch("WScript.Shell")
    for pattern in ["*dev*", "*main*"]:
        for f in glob.glob(os.path.join(recent_dir, pattern)):
            shortcut = shell.CreateShortCut(f)
            print(f"{os.path.basename(f)} -> {shortcut.Targetpath}")
except Exception as e:
    print("Error:", e)
