from pathlib import Path
import os
import re
import subprocess
from typing import Union


class FileOpener:
    """
    A class to handle the opening of files in specific 3D or digital content creation applications.
    It can also set environment variables based on user preferences for applications such as Maya, Houdini, and Nuke.

    Attributes
    ----------
    pref_dict : dict
        A dictionary mapping application names to their corresponding environment variable names for user preferences.
    """


    __pref_dict: dict = {
        'houdini': 'HOUDINI_USER_PREF_DIR',
        'maya': 'MAYA_APP_DIR',
        'mari': 'MARI_PATH',
        'nuke': 'NUKE_PATH'
    }

    
    @classmethod
    def open_file_in_app(cls, file_path: Union[Path, str], application_path: Union[Path, str], pref_path: Union[Path, str] = None, python_path: Union[Path, str] = None) -> None:
        """
        Opens a file in the specified application, optionally setting the application's preference directory or Python path.

        Parameters
        ----------
        file_path : Union[Path, str]
            The path to the file to be opened.
        application_path : Union[Path, str]
            The path to the application's executable file.
        pref_path : Union[Path, str], optional
            The path to the application's preference directory. If provided, this will be set as an environment variable (default is None).
        python_path : Union[Path, str], optional
            The path to the application's Python executable, if needed for certain applications (default is None).

        Notes
        -----
        - If ZBrush is detected, the file will be opened using `os.startfile()` for Windows-specific behavior.
        - Environment variables are set for Maya, Houdini, Mari and Nuke based on the application's preference path if provided.
        - Maya has an additional environment variable for `QT_PLUGIN_PATH` that is configured if necessary.
        """
        
        if 'ZBrush.exe' in application_path:
            os.startfile(file_path.replace('/', '\\'))
            return
        
        application_name: str = re.sub(r'\d+', '', Path(application_path).name.split('.')[0].lower())
        application_args: list = [application_path, file_path]
        env: dict = os.environ.copy()
        
        if pref_path and os.path.exists(pref_path):
            pref_env_variable: str = cls.__pref_dict[application_name]
            env[pref_env_variable] = str(pref_path)
            
        if python_path:
            env['PYTHONPATH'] = str(python_path)
            
        if application_name == 'maya':
            env['QT_PLUGIN_PATH'] = os.path.join(os.path.dirname(os.path.dirname(application_path)), 'plugins', 'platforms')
            
        subprocess.Popen(application_args, env=env)
        

def main() -> None:
    maya_file = r'E:\Art\3D\LEARN\OSL\test_osl.ma'
    maya_path = r"C:\\Program Files\\Autodesk\\Maya2023\\bin\\maya.exe"
    FileOpener.open_file_in_app(file_path=maya_file, application_path=maya_path)


if __name__ == '__main__':
    main()
