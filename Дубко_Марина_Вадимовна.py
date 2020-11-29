import pandas as pd
import matplotlib.pyplot as plt

b='https://raw.githubusercontent.com/seagull-larus/Sirius21/main/Boys.csv'
g='https://raw.githubusercontent.com/seagull-larus/Sirius21/main/Girls.csv'

boys_table = pd.read_csv(b, error_bad_lines=(False), sep=';', low_memory=(False), encoding='windows-1251')
girls_table = pd.read_csv(g, error_bad_lines=(False), sep=';', low_memory=(False), encoding='windows-1251')

def get_last_letters_distribution(table, quantity):
    result_table = {}
    
    for row in table.to_dict(orient="records"):
        trimmed_name = row["Name"].strip().lower()
        last_letters = trimmed_name[-quantity:]
        
        result_table[last_letters] = result_table.get(last_letters, 0) + 1
        
    return result_table

def get_keys_values(dict):
    keys = []
    values = []
    
    for key, value in dict.items():
        keys.append(key)
        values.append(value)
        
    return keys, values

def show_letters_plot(letters, values):
    x_pos = [i for i, _ in enumerate(letters)]
    
    plt.bar(x_pos, values, color='green')
    plt.xlabel("Буквы")
    plt.ylabel("Количество имен")
    plt.title("Зависимость количества имен от буквы, на которую они заканчиваются")
    
    plt.xticks(x_pos, letters)
    
    plt.show()
    
boys_letters, boys_values = get_keys_values(get_last_letters_distribution(boys_table, 1))
show_letters_plot(boys_letters, boys_values)


girls_letters, girls_values = get_keys_values(get_last_letters_distribution(girls_table, 1))
show_letters_plot(girls_letters, girls_values)  

def guess_gender(name: str):
    gender = "Уважаемый"
    name = name.lower()

    for i in range(1, len(name) + 1):
        boys_distribution = get_last_letters_distribution(boys_table, i)
        girls_distribution = get_last_letters_distribution(girls_table, i)
        
        last_letters = name[-i:]
        
        boys_names_count = boys_distribution.get(last_letters, 0)
        girls_names_count = girls_distribution.get(last_letters, 0)

        if boys_names_count == 0 and girls_names_count != 0:
            return "Уважаемая"

        if boys_names_count != 0 and girls_names_count == 0:
            return "Уважаемый"
        
        if boys_names_count == 0 and girls_names_count == 0:
            return gender
        
        if boys_names_count >= girls_names_count:
            gender = "Уважаемый"
            continue
        
        if boys_names_count <= girls_names_count:
            gender = "Уважаемая"
            continue
        return gender
    
    
name = input()
print(guess_gender(name), name)



