from all_riddles import riddles_json

print("hi") 
def main():
    riddles_list = riddles_json['riddle']

    for riddle in riddles_list:
        print(riddle["id"])



main()
