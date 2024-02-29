from ninja import errors

class Exceptions:

    @staticmethod
    def not_found(message: str = "Not found"):
        raise errors.HttpError(404, message)