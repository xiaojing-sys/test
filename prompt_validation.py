"""Small input-validation example for learning CI; no model service is called."""


def validate_prompt(prompt: str, max_chars: int = 2000) -> str:
    if isinstance(max_chars, bool) or not isinstance(max_chars, int):
        raise TypeError("max_chars must be an integer")
    if max_chars < 1:
        raise ValueError("max_chars must be positive")
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a string")
    normalized = prompt.strip()
    if not normalized:
        raise ValueError("prompt must not be empty")
    if len(normalized) >= max_chars:
        raise ValueError("prompt exceeds the character limit")
    return normalized
