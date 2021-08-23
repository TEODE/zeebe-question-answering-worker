import unittest
from libs.reader import Reader

class TestQuestionAnswering(unittest.TestCase):

    def test_sequence_fr_inference(self):
        model = "models/camembert-base-squadFR-fquad-piaf"
        reader = Reader.get_instance(model)
        question = "Qui est Claude Monet ?"
        context = "Claude Monet, né le 14 novembre 1840 à Paris et mort le 5 décembre 1926 à Giverny, est un peintre français et l’un des fondateurs de l'impressionnisme."
        output = reader.infer(question, context)
        self.assertEqual(output["answer"], "un peintre français")
        self.assertEqual(output["score"], 0.8595070838928223)
    
    def test_sequence_ml_inference(self):
        model = "models/xlm-roberta-large-xnli"
        # forces recreate Classifier singleton
        Reader.destroy_instance()
        reader = Reader.get_instance(model)
        question = "Who is Claude Monet?"
        context = "Claude Monet, born November 14, 1840 in Paris and died December 5, 1926 in Giverny, is a French painter and one of the founders of Impressionism."
        output = reader.infer(question, context)
        self.assertEqual(output["answer"], "a French painter")
        self.assertEqual(output["score"], 0.8595070838928223)

if __name__ == '__main__':
    unittest.main()        