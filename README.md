# Caesar Cipher Brute Force Decryption

This Python script attempts to decrypt a text that has been encrypted using the Caesar cipher. The script tries all possible shifts and provides the decrypted text for each shift. Additionally, it includes functionality to automatically detect the most probable correct decryption based on the presence of common English words.

## Features

- **Brute Force Decryption**: Tries all possible shifts (0-25) and displays the corresponding decrypted text.
- **Automatic Text Recognition**: Identifies the most likely correct decryption by checking for common English words.
- **Custom Word Delimiter Support**: Allows for the input of a custom word delimiter (e.g., spaces, hyphens).
- **Result Export**: Saves all possible decryption results to a text file for further analysis.

## Getting Started

### Prerequisites

- Python 3

### Installation

1. Clone the repository or download the script file.
2. Ensure you have Python 3.x installed on your system.

### Usage

1. Run the script using Python:

    ```bash
    python caesar_brute_force.py
    ```

2. Input the encrypted text when prompted.
3. Specify the word delimiter (press Enter to use a space by default).
4. The script will display possible decrypted messages for each shift.
5. The script will also attempt to recognize the correct text automatically and display it.
6. All results will be saved to `caesar_brute_force_results.txt` in the working directory.

### Customization

You can customize the list of common words used for automatic text recognition by modifying the `common_words` list in the script.

