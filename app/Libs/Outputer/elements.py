from colorama import Fore, Back, Style

class Color:
    def __init__(self, fore, back) -> None:
        self.fore = fore
        self.back = back

class _Element:
    def __init__(self, text, color=None, id=0) -> None:
        self.id = id

        if color == None:
            self.color = Color(Fore.BLACK, Back.WHITE)

        else:
            self.color = color

        self.text = str(text)

    def to_console(self):
        return f"{self.color.back}{self.color.fore}{self.text}{Style.RESET_ALL}"

    def to_server(self):
        def get_fore_color(objColor):
            if objColor == Fore.GREEN:
                return "text-success "
            
            elif objColor == Fore.RED:
                return "text-danger "

            elif objColor == Fore.YELLOW:
                return "text-warning "

            elif objColor == Fore.BLACK:
                return "text-dark "

            elif objColor == Fore.WHITE:
                return "text-white "
            
            else:
                return ""

        def get_back_color(objColor):
            if objColor == Back.GREEN:
                return "bg-success "
            
            elif objColor == Back.RED:
                return "bg-danger "

            elif objColor == Back.YELLOW:
                return "bg-warning "

            elif objColor == Back.BLACK:
                return "bg-dark "

            elif objColor == Back.WHITE:
                return "bg-white "
            
            else:
                return ""
        
        self.text = self.text.replace("\n", "<br/>")

        return f'<li class="py-1 text-break"><div class="badge text-wrap fs-6 text-start text-break {get_fore_color(self.color.fore)}{get_back_color(self.color.back)}p-2"><span class="text-break">{self.text}</span></div></li></div>'

class FlashElement(_Element):
    def __init__(self, text, color=None, id=0) -> None:
        super().__init__(text, color, id)

    def to_console(self):
        return super().to_console()

    def to_server(self):
        return super().to_server()

class TextElement(_Element):
    def __init__(self, text, color=None, id=0) -> None:
        super().__init__(text, color, id)
        # self.text = f"{self.color.back}{self.color.fore}{text}{Style.RESET_ALL}"

    def to_console(self):
        return super().to_console()

    def to_server(self):
        return super().to_server()