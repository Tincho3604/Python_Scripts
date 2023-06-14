import subprocess
import os

def execute_command(command, cwd=None):
    subprocess.Popen(command, shell=True, cwd=cwd)

def open_terminals_and_execute(frontend_path, frontend_command, backend_path, backend_command):

    execute_command("start cmd /k " + frontend_command, cwd=frontend_path)

    execute_command("start cmd /k " + backend_command, cwd=backend_path)

frontend_path = "C:\\Users\\Martin\\Desktop\\timesheet\\frontend"
frontend_command = "yarn start" 

backend_path = "C:\\Users\\Martin\\Desktop\\timesheet\\backend"
backend_command = "npm run dev" 

open_terminals_and_execute(frontend_path, frontend_command, backend_path, backend_command)
