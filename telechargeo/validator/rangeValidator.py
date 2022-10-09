from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.document import Document

class RangeValidator(Validator):

    def validate(self, document: Document) -> None:
        text = document.text
        """
            Validate user input if it is include in the range of [1-5]
        """
        if text and text not in ['1', '2', '3', '4', '5']:

            raise ValidationError(message='The value should be one of the following (1, 2, 3, 4, 5)')