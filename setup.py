from cx_Freeze import setup, Executable

setup(name = "Sumon",
	version = "0.2" ,
	description = "CS150 MP2: SUMOn",
	executables = [Executable("sumon.py")],)