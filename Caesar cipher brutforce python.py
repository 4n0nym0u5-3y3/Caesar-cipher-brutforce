import string

def decrypt_caesar_cipher(ciphertext, shift):

    #Decrypts a Caesar cipher encrypted text using a given shift.

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            plaintext += new_char
        else:
            plaintext += char
    return plaintext

def brute_force_caesar(ciphertext, word_delimiter=' '):


    #Attempts to decrypt a Caesar cipher by trying all possible shifts.

    common_words = ['e', 'di', 'il', 'la', 'che', 'a', 'un', 'per', 'con', 'una', 'sono', 'in', 'ma', 'non']
    potential_results = []
    
    for shift in range(26):
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        potential_results.append((shift, decrypted_text))
        word_list = decrypted_text.split(word_delimiter)
        score = sum(1 for word in word_list if word.lower() in common_words)
        if score > 0:
            print(f"Possibile testo riconosciuto con shift {shift}: {decrypted_text} (Punteggio: {score})")
    
    return potential_results

def save_results_to_file(results, filename="caesar_brute_force_results.txt"):

    #Saves decryption results to a text file.

    with open(filename, 'w') as file:
        for shift, text in results:
            file.write(f"Shift {shift}: {text}\n")
    print(f"Risultati salvati in {filename}")

# Funzione principale

def main():
    ciphertext = input("Inserisci il testo cifrato: ")
    word_delimiter = input("Inserisci il delimitatore di parole (spazio di default): ") or ' '
    
    # Decifratura a forza bruta
    results = brute_force_caesar(ciphertext, word_delimiter)
    
    # Salvataggio dei risultati
    save_results_to_file(results)


if __name__ == "__main__":
    main()