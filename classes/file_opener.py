from pathlib import Path
import os
import re
import subprocess
from typing import Union


class FileOpener:


    pref_dict = {
        'houdini': 'HOUDINI_USER_PREF_DIR',
        'maya': 'MAYA_APP_DIR',
        'nuke': 'NUKE_PATH'
    }

    
    @classmethod
    def open_file_in_app(cls, file_path: Union[Path, str], application_path: Union[Path, str], pref_path: Union[Path, str] = None, python_path: Union[Path, str] = None) -> None:
        
        
        if 'ZBrush.exe' in application_path:
            os.startfile(file_path.replace('/', '\\'))
            return
        
        
        application_name: str = re.sub(r'\d+', '', Path(application_path).name.split('.')[0].lower())
        application_args: list = [application_path, file_path]
        env: dict = os.environ.copy()
        
        if pref_path and os.path.exists(pref_path):
            pref_env_variable: str = cls.pref_dict[application_name]
            env[pref_env_variable] = str(pref_path)
            
            
        if application_name == 'maya':
            env['QT_PLUGIN_PATH'] = os.path.join(os.path.dirname(os.path.dirname(application_path)), 'plugins', 'platforms')
            
        
        subprocess.Popen(application_args, env=env)


if __name__ == '__main__':
    
    def main() -> None:
        maya_file = r'E:\Art\3D\LEARN\OSL\test_osl.ma'
        maya_path = r"C:\\Program Files\\Autodesk\\Maya2023\\bin\\maya.exe"
        
        FileOpener.open_file_in_app(file_path=maya_file, application_path=maya_path)
        
    main()
