#String
def manipulate_sentence():
    # Original string
    sentence = "Learning Python is fun and rewarding."

    # Extract the substring "Python is fun" using negative slicing
    substring = sentence[-30:-15]
    print(f"Extracted Substring: {substring}")

    # Modify the original string by replacing "rewarding" with "exciting"
    modified_sentence = sentence.replace("rewarding", "exciting")
    print(f"Modified Sentence: {modified_sentence}")

    # Insert the phrase " Keep practicing!" after "exciting"
    insertion_phrase = " Keep practicing!"
    position = modified_sentence.find("exciting") + len("exciting")
    final_sentence = modified_sentence[:position] + insertion_phrase + modified_sentence[position:]
    print(f"Sentence after Insertion: {final_sentence}")

    # Capitalize the first letter of each word in the final output
    capitalized_sentence = final_sentence.title()
    print(f"Final Output: {capitalized_sentence}")

# Call the function to execute the tasks
manipulate_sentence()
