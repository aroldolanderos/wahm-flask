class IncomeResponse:
    @staticmethod
    def success(msg, status_code):
        return {'data': msg}, status_code

    @staticmethod
    def error(msg, status_code):
        return {'error': msg}, status_code
