import unittest

from prompt_validation import validate_prompt


class PromptValidationTests(unittest.TestCase):
    def test_trims_surrounding_whitespace(self):
        self.assertEqual(validate_prompt("  Explain CI/CD.\n"), "Explain CI/CD.")

    def test_preserves_internal_whitespace_and_unicode(self):
        self.assertEqual(validate_prompt("解释 CI\n和 CD"), "解释 CI\n和 CD")

    def test_rejects_empty_input(self):
        for prompt in ("", "   ", "\n\t"):
            with self.subTest(prompt=prompt):
                with self.assertRaises(ValueError):
                    validate_prompt(prompt)

    def test_rejects_non_string_input(self):
        for prompt in (None, 123, ["hello"]):
            with self.subTest(prompt=prompt):
                with self.assertRaises(TypeError):
                    validate_prompt(prompt)

    def test_accepts_input_at_limit(self):
        self.assertEqual(validate_prompt("abcd", max_chars=4), "abcd")

    def test_rejects_input_over_limit(self):
        with self.assertRaises(ValueError):
            validate_prompt("abcde", max_chars=4)

    def test_rejects_invalid_limit(self):
        for limit in (0, -1):
            with self.subTest(limit=limit):
                with self.assertRaises(ValueError):
                    validate_prompt("hello", max_chars=limit)
        for limit in (True, "10", 1.5):
            with self.subTest(limit=limit):
                with self.assertRaises(TypeError):
                    validate_prompt("hello", max_chars=limit)


if __name__ == "__main__":
    unittest.main()
