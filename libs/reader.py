import logging, os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv() # Loading env vars
logging.basicConfig(format='%(levelname)s:%(message)s', 
   level=int(os.environ["LOGGING_LEVEL"]))

class Reader:
   
   __instance = None
   
   @staticmethod 
   def get_instance(model: str=None):
      """ Static access method. """
      if Reader.__instance == None:
          logging.debug("QuestionAnswering.get_instance: instanciate the singleton Classifier") 
          if model:  
            Reader(model)
          else:
            Reader()
      logging.debug("QuestionAnswering.get_instance: retrieve the singleton Classifier instance")
      return Reader.__instance
   
   @staticmethod 
   def destroy_instance():
      Reader.__instance = None
      logging.debug("QuestionAnswering.destroy_instance: destroy the singleton Classifier") 


   def __init__(self, model: str=None):
      """ Virtually private constructor. """
      if Reader.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         """
         Hugging Face question answering pipeline
         """ 
         logging.debug("QuestionAnwsering.__init__: pipeline creation...")
         self.pipeline = pipeline("question-answering", 
                        model=model,
                        tokenizer=model)
         logging.debug("QuestionAnswering.__init__: created!")   
         Reader.__instance = self
   

   def infer(self, question: str, context: str) -> str:
        """
        Hugging Face question answering inference
        """   
        logging.info("QuestionAnswering.infer: infering for \"" + question + "\"...") 
        result = self.pipeline(question, context)
        logging.info("QuestionAnswering.infer: answer=\"" + str(result["answer"]) + "\" (score=" 
         + str(result["score"]) + ")")

        return result