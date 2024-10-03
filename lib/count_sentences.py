#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value=''):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value

    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    string = self._value
    # delimiters = ["?", ".", "!"]
    count = 0

    # Split the string into potential sentences.
    potential_sentences = re.split('[?.!]', string)
 
    # count non-empty sentences
    for sentence in potential_sentences:
      if sentence.strip():
        count += 1
    
    return count

# simple_string = MyString("one. two. three?")
# empty_string = MyString()
# complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")

# simple_string.count_sentences()
# empty_string.count_sentences()
# complex_string.count_sentences()