from fastapi import HTTPException, status


class BException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class PasswordNotValidException(BException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Password is not valid"


class UserNotFoundException(BException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User not found"


class WrongPasswordException(BException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Wrong password"


class InvalidTokenException(BException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Invalid token error"


class UserInactiveException(BException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "User inactive"


class ProductAlreadyExistsException(BException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Product is already exists"


class ProductNotFoundException(BException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Product not found"
