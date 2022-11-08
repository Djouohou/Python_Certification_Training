class CustomException(Exception):
    def _init_(self, message):
        self.message = message

try:
    raise CustomException('This is my custom exception')
except CustomException as ex:
    print(ex)
