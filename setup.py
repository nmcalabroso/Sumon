from cx_Freeze import setup, Executable

includefiles = ['avbin.dll','assets/','docs/']
includes = []
excludes = ['Tkinter']
packages = []

exe = Executable(script = "sumon.py",
				base = "Win32Gui",
				copyDependentFiles = True,
				icon = "favicon.ico",
				targetName = "sumon.exe")

setup(name = "Sumon",
	version = "0.3" ,
	description = "CS150 MP2: SUMOn",
	author = "Vertex",
	options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
	executables = [exe])