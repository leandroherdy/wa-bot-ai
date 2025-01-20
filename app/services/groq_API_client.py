import os
import logging
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class GroqAPIClient:
    """
    Client for interacting with the Groq API.
    """

    DEFAULT_MODEL = "llama-3.3-70b-versatile"

    def __init__(self, api_key: str = None, model: str = DEFAULT_MODEL):
        """
        Initializes the GroqAPIClient.

        Args:
            api_key (str): API key for authentication. Defaults to environment variable 'GROQ_API_KEY'.
            model (str): The AI model to use. Defaults to 'llama-3.3-70b-versatile'.
        """
        self.__api_key = api_key or os.getenv("GROQ_API_KEY")
        self.__model = model
        self.__client = Groq(api_key=self.__api_key)

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(self.__class__.__name__)

    def _load_instruction(self) -> str:
        """
        Loads an instruction from a specified file.

        Args:
            filename (str): The name of the file containing the instruction.

        Returns:
            str: The instruction text.

        Raises:
            FileNotFoundError: If the file is not found.
            Exception: For any other errors during file reading.
        """
        file_path = os.path.join("instructions", "instruction.txt")
        if not os.path.exists(file_path):
            self.logger.error(f"Instruction file '{file_path}' not found.")
            raise FileNotFoundError(f"Instruction file '{file_path}' not found.")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                instruction = file.read()
                self.logger.info(f"Instruction loaded from '{file_path}'.")
                return instruction
        except Exception as err:
            self.logger.error(f"Error loading instruction file: {err}")
            raise

    def process_instruction(self, text: str) -> str:
        """
        Sends an instruction loaded from a file and text to the Groq API for processing.

        Args:
            text (str): The input text to be processed.
            instruction_file (str): The name of the file containing the instruction.

        Returns:
            str: The AI-generated response.

        Raises:
            ValueError: If the input text is empty or invalid.
            Exception: For any errors during the API call.
        """
        if not text.strip():
            self.logger.error("Input text cannot be empty.")
            raise ValueError("Input text cannot be empty.")

        try:
            instruction = self._load_instruction()

            self.logger.info(f"Sending instruction to Groq API: {instruction}")
            chat_completion = self.__client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"{instruction}\n{text}",
                    }
                ],
                model=self.__model,
            )
            response = chat_completion.choices[0].message.content
            self.logger.info("Instruction processed successfully.")
            return response
        except Exception as err:
            self.logger.error(f"Error while processing instruction: {err}")
            raise
