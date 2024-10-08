import logging
import sys

        
class Logger:
    
    LOGGER_NAME = 'Logger'
    FORMAT_DEFAULT = "[%(asctime)s][%(name)s][%(levelname)s] %(message)s"
    FILE_FORMAT_DEFAULT = "[%(asctime)s][%(name)s][%(levelname)s] %(message)s"
    SECONDS_FMT_DEF = r"%Y-%m-%d %H:%M:%S"
    LEVEL_DEFAULT = logging.DEBUG
    LEVEL_WRITE_DEFAULT = logging.WARNING
    PROPAGATE_DEFAULT = False
    
    _logger = None
    
    
    @classmethod
    def logger(cls):
        
        if not cls._logger:
            
            if cls.logger_exists():
                cls._logger = logging.getLogger(cls.LOGGER_NAME)
                
            else:
                cls._logger = logging.getLogger(cls.LOGGER_NAME)
                cls._logger.setLevel(cls.LEVEL_DEFAULT)
                cls._logger.propagate = cls.PROPAGATE_DEFAULT
            
                formatter = logging.Formatter(cls.FORMAT_DEFAULT, cls.SECONDS_FMT_DEF)

                handler = logging.StreamHandler(sys.stderr)
                handler.setFormatter(formatter)
                
                cls._logger.addHandler(handler)
        
        return cls._logger
    
    
    @classmethod
    def logger_exists(cls):
        return cls.LOGGER_NAME in logging.Logger.manager.loggerDict.keys()
    
    
    @classmethod
    def set_level(cls, level):
        cls.logger().setLevel(level)
    
        
    @classmethod
    def set_propagate(cls, propagate):
        cls.logger().propagate = propagate
    
       
    @classmethod
    def debug(cls, msg, *args, **kwargs):
        cls.logger().debug(msg, *args, **kwargs)
    
        
    @classmethod
    def info(cls, msg, *args, **kwargs):
        cls.logger().info(msg, *args, **kwargs)
    
        
    @classmethod
    def warning(cls, msg, *args, **kwargs):
        cls.logger().warning(msg, *args, **kwargs)
    
        
    @classmethod
    def error(cls, msg, *args, **kwargs):
        cls.logger().error(msg, *args, **kwargs)
    
        
    @classmethod
    def critical(cls, msg, *args, **kwargs):
        cls.logger().critical(msg, *args, **kwargs)
    
        
    @classmethod
    def log(cls, level, msg, *args, **kwargs):
        cls.logger().log(level, msg, *args, **kwargs)
    
        
    @classmethod
    def exception(cls, msg, *args, **kwargs):
        cls.logger().exception(msg, *args, **kwargs)
    
        
    @classmethod
    def write_to_file(cls, path, level = LEVEL_WRITE_DEFAULT):
        file_handler = logging.FileHandler(path)
        file_handler.setLevel(level)
        
        formatter = logging.Formatter(cls.FILE_FORMAT_DEFAULT, cls.SECONDS_FMT_DEF)
        file_handler.setFormatter(formatter)
        
        logger = cls.logger()
        logger.addHandler(file_handler)



def main() -> None:
    log_path: str = 'test.log'
    Logger.LOGGER_NAME = f'{__file__}'
    Logger.write_to_file(path=log_path, level=logging.DEBUG)
    Logger.info('info')
    Logger.critical("critical")
    Logger.warning('warning')
    Logger.debug("debug")
    

if __name__ == '__main__':
    main()
    
    """
    Outputs:
    
    [2024-09-13 14:28:41][e:\Art\3D\Dev\Utils\classes\logger.py][INFO] info
    [2024-09-13 14:28:41][e:\Art\3D\Dev\Utils\classes\logger.py][CRITICAL] critical
    [2024-09-13 14:28:41][e:\Art\3D\Dev\Utils\classes\logger.py][WARNING] warning
    [2024-09-13 14:28:41][e:\Art\3D\Dev\Utils\classes\logger.py][DEBUG] debug
    """
