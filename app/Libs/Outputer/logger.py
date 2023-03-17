from enum import Enum
from colorama import Fore, Style, Back
from ..Design.Patterns import Singleton
from .elements import Color, FlashElement, TextElement

class LoggerTypes(Enum):
    console = 0x01
    server = 0x02
    in_file = 0x03

class LoggerColor(Enum):
    success = 0x00
    negative = 0x01
    warn = 0x02
    inverted = 0x03
    GREEN = 0x04
    RED = 0x05
    YELLOW = 0x06

@Singleton
class __Logger:
    def __init__(self) -> None:
        self.type = LoggerTypes.server

        self._output = []

        self._flash_elements = {
            
        }
        self.__print = print
        self.__serverInstance = None

    def __call__(self, *args, **kwargs) -> None:
        # if len(args) == 0 and len(kwargs.keys()) > 0:
        #     self.__print( kwargs.keys())
        #     if "serverInstance" in kwargs.keys():
        #         self.init_server(instance=kwargs["serverInstance"])

        if len(args) > 0:
            # if isinstance(args[0], LoggerTypes):
            #     self.change_type(args[0])

            if callable(args[0]):
                return args[0](self)

            elif "is_flash" in kwargs.keys() and "id" in kwargs.keys():
                if "type" in kwargs.keys():
                    if kwargs['type'] == LoggerColor.success:
                        color = Color(Fore.BLACK, Back.GREEN)

                    elif kwargs['type'] == LoggerColor.negative:
                        color = Color(Fore.BLACK, Back.RED)

                    elif kwargs['type'] == LoggerColor.warn:
                        color = Color(Fore.BLACK, Back.YELLOW)

                    elif kwargs['type'] == LoggerColor.inverted:
                        color = Color(Fore.BLACK, Back.WHITE)

                    elif kwargs['type'] == LoggerColor.GREEN:
                        color = Color(Fore.GREEN, Back.BLACK)

                    elif kwargs['type'] == LoggerColor.RED:
                        color = Color(Fore.RED, Back.BLACK)

                    elif kwargs['type'] == LoggerColor.YELLOW:
                        color = Color(Fore.YELLOW, Back.BLACK)

                else:
                    color = Color(Fore.BLACK, Back.WHITE)

                element = FlashElement(str(args[0]), color, id=kwargs["id"])
                
                if element.id not in self._flash_elements:
                    self._flash_elements[kwargs['id']] = element
                    self.log(element)
                else:
                    self._flash_elements[kwargs['id']].text = str(args[0])

            elif not isinstance(args[0], TextElement):
                if 'type' in kwargs.keys():
                    if kwargs['type'] == LoggerColor.success:
                        self.log(TextElement(args[0], Color(Fore.BLACK, Back.GREEN)))

                    elif kwargs['type'] == LoggerColor.negative:
                        self.log(TextElement(args[0], Color(Fore.BLACK, Back.RED)))

                    elif kwargs['type'] == LoggerColor.warn:
                        self.log(TextElement(args[0], Color(Fore.BLACK, Back.YELLOW)))

                    elif kwargs['type'] == LoggerColor.inverted:
                        self.log(TextElement(args[0], Color(Fore.BLACK, Back.WHITE)))

                    elif kwargs['type'] == LoggerColor.GREEN:
                        self.log(TextElement(args[0], Color(Fore.GREEN, Back.BLACK)))

                    elif kwargs['type'] == LoggerColor.RED:
                        self.log(TextElement(args[0], Color(Fore.RED, Back.BLACK)))

                    elif kwargs['type'] == LoggerColor.YELLOW:
                        self.log(TextElement(args[0], Color(Fore.YELLOW, Back.BLACK)))

                else:
                    self.log(TextElement(args[0]))

            else:
                self.log(args[0])
                
                # self.change_type(args[0])

        if len(self._output) > 0:
            if self.type == LoggerTypes.console:
                element = self._output.pop(0)
                self.__print(element.to_console())
                # with self.lock:

            elif self.type == LoggerTypes.server:
                _loggs_ = ""
                
                for elem in self._output:
                    # self.__print(elem.to_server())
                    _loggs_ += elem.to_server()

                return _loggs_

    # def init(self, type):
    #     self.type = type

    def init_server(self, serverInstance):
        self.__serverInstance = serverInstance

    def log(self, elem):
        if len(self._output):
            elem.id = self._output[-1].id + 1

        # if self.type == LoggerTypes.server:
        #     if self.__serverInstance != None:
        #         self.__serverInstance.update_logs(elem)

        self._output.append(elem)

    def change_type(self, type):
        self.type = type

    def get_logger_type(self):
        # self.__print(self.type)
        return self.type

@__Logger()
def init(obj, *args, **kwargs):
    ''' Logger initializer '''
    return obj.init_server

@__Logger()
def change_type(obj):
    return obj.change_type

@__Logger()
def print(obj):
    ''' Function to call __Logger '''
    return obj 

# # @__Logger
# def get_type():
#     return __Logger().get_logger_type()

# @__Logger.init
# def init(*args):
#     ''' Function to init __Logger '''
#     pass