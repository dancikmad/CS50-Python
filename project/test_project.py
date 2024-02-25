import os
import unittest
from unittest.mock import patch

from project import Personalized, generic, write_message


class TestContextManagers(unittest.TestCase):
    def test_personalized(self):
        sender_name = "John"
        receiver_name = "Alice"
        with Personalized(sender_name, receiver_name) as p:
            msg = "I am so proud of you!\n"
            msg += "Being your friend for all these years has been nothing but a blessing\n"
            msg += "I don’t say it often, but I just wanted to let you know "
            msg += "that you inspire me and I love you!\nAll the best."
            msg += "\nAlways \n\n"
            p.write(msg)

        # Check if the file was created
        self.assertTrue(os.path.exists(f"{sender_name}_personalized.txt"))

        # Read the content of the file and assert
        with open(f"{sender_name}_personalized.txt", "r") as f:
            content = f.read()
            self.assertIn(f"Dear {receiver_name}", content)
            self.assertIn(msg, content)
            self.assertIn(f"Sincerely, \n\n{sender_name}", content)

        # Clean up
        os.remove(f"{sender_name}_personalized.txt")

    def test_generic(self):
        sender_name = "John"
        recipient = "Alice"
        card_type = "happy_bday.txt"  # assuming you have a template file

        with generic(card_type, sender_name, recipient) as g:
            g.write("This is a generic message.")

        # Check if the file was created
        self.assertTrue(os.path.exists(f"{sender_name}_generic.txt"))

        # Read the content of the file and assert
        with open(f"{sender_name}_generic.txt", "r") as f:
            content = f.read()
            self.assertIn(f"Dear {recipient}", content)
            self.assertIn("This is a generic message.", content)
            self.assertIn(f"Sincerely, \n\n{sender_name}", content)

        # Clean up
        os.remove(f"{sender_name}_generic.txt")


class TestWriteMessage(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=["line 1", "line 2", "", "line 3", "", "line 4", ""],
    )
    def test_input_multiline(self, mocked_input):
        expected_message = "line 1\nline 2\n\nline 3\n\nline 4\n"
        self.assertEqual(write_message(), expected_message)

    # Test Ctrl + C for continuing the program and saving the lines after applying it.
    @patch("builtins.input", side_effect=["line 1", "line 2", KeyboardInterrupt])
    def test_input_multiline(self, mocked_input):
        expected_message = "line 1\nline 2"
        self.assertEqual(write_message(), expected_message)


if __name__ == "__main__":
    unittest.main()
