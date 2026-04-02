"""
@Author: James Bond - The legend
"""

import hashlib

#Function for calculating hash
def calculate_sha256(plain_text):
    """
    Function to generate sha256 Hash from given plain text
    Args:
        plain_text: plain given text to hash
    Return:
        hash_value: Hashed sha256
    """
    encoded_text = plain_text.encode('utf-8')
    hash_value = hashlib.sha256(encoded_text).hexdigest()
    return hash_value