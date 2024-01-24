import ascii_art
import random

wartosc_kart=0
karty_gracza = ['szostka', 'krol']
for karty in karty_gracza:
    wybrana_karta_nazwa=karty
    wybrana_karta=getattr(ascii_art, wybrana_karta_nazwa)
    wartosc_kart+=wybrana_karta.get('value')

print(wartosc_kart)


#ponizej kod na drukowanie kart obok siebie:

#karty = ['aas', 'dwojka', 'trojka']
#for karta in karty:
#    selected_dict_name = karta
#    selected_dict = getattr(ascii_art, selected_dict_name)
#    ascii_arts.append(selected_dict.get('art'))
#
## Split the ASCII art strings into lines
#lines_list = [art.strip().split('\n') for art in ascii_arts]
#
## Ensure all ASCII arts have the same number of lines (pad with empty lines if needed)
#max_lines = max(len(lines) for lines in lines_list)
#for lines in lines_list:
#    lines.extend([''] * (max_lines - len(lines)))
#
## Print the combined ASCII art
#for i in range(max_lines):
#    combined_line = '  '.join(lines[i] for lines in lines_list)
#    print(combined_line)
