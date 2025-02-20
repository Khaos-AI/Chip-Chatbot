import unittest
from src.core.chip import ChipBot
from src.utils.config_loader import load_config

class TestChip(unittest.TestCase):
    def setUp(self):
        self.config = load_config()
        self.chip = ChipBot(self.config)
    
    def test_basic_response(self):
        response = self.chip.process_input("Who is Kaito?")
        self.assertIsNotNone(response)
