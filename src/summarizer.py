from transformers import pipeline

class TextSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        """
        Initialize the TextSummarizer with a specific model.

        Args:
            model_name (str): The name of the model to be used for summarization.
        """
        self.model_name = model_name
        self.summarizer = pipeline("summarization", model=self.model_name)

    def summarize(self, text, max_length=10000, min_length=5):
        """
        Summarize the given text using the loaded model.

        Args:
            text (str): The text to be summarized.
            max_length (int): The maximum length of the summarized text.
            min_length (int): The minimum length of the summarized text.

        Returns:
            str: The summarized text, or an error message if an exception occurs.
        """
        try:
            summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"An error occurred: {e}"