import json
from pathlib import Path
from typing import Union


class JsonFile:
    
    
    def __init__(self, path: Union[str, Path]) -> None:
        self._path = Path(path) 
        self._name = self._path.name


    @property
    def path(self) -> Path:
        return self._path
    
    
    @path.setter
    def path(self, new_path: Union[str, Path]) -> None:
        self._path = Path(new_path)
        self._name = self._path.name
    
    
    @property
    def name(self) -> str:
        return self._name


    def json_to_dict(self) -> dict:
        with open(self._path, 'r', encoding='utf-8') as file:
            dico = json.load(file)
        return dico


    def dict_to_json(self, dictionary: dict) -> None:
        dictionary = {key: str(value) if isinstance(value, Path) else value for key, value in dictionary.items()}
        with open(self._path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, indent=4, ensure_ascii=False)
        return
    
    
    def get_value(self, key: str, return_path: bool = False) -> Union[bool, int, float, str, list, dict, Path, None]:
        value = self.json_to_dict().get(key)
        return Path(value) if return_path and isinstance(value, str) else value
    
    
    def set_value(self, key: str, value: Union[bool, int, float, str, list, dict, Path, None]) -> None:
        value = str(value) if isinstance(value, Path) else value
        dictionnary = self.json_to_dict()
        dictionnary[key] = value
        self.dict_to_json(dictionnary)
