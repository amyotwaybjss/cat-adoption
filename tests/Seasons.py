class Season:
    def __init__(self, name, emoji, colour):
        self.name = name
        self.emoji = emoji
        self.colour = colour

spring = Season('Spring', '🌸', '#FFB6C1')
summer = Season('Summer', '☀️', '#32CD32')
autumn = Season('Autumn', '🍂', '#F4A460')
winter = Season('Winter', '❄️', '#87CEFA')
unknown = Season('N/a', '✨', '#DDA0DD')