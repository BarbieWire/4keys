from rest_framework.exceptions import APIException


class InvalidCredentialsProvidedException(APIException):
    default_detail = "Invalid credentials provided"
    status_code = 400
    default_code = "invalid_credentials"


class UserDoesNotExistException(APIException):
    default_detail = "User does not exist"
    status_code = 400
    default_code = "user_does_not_exist"


class PasswordIncorrectException(APIException):
    default_detail = "Password Incorrect"
    status_code = 400
    default_code = "password_incorrect"


class AccountDeactivatedException(APIException):
    default_detail = "Access allowed only for active accounts"
    status_code = 403
    default_code = "account_inactive"


class AlreadySignedInException(APIException):
    default_detail = "Already signed in"
    status_code = 403
    default_code = "signed_in_already"
    

class VerificationFailedException(APIException):
    default_detail = "Link is invalid"
    status_code = 403
    default_code = "link_invalid"