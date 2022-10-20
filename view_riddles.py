from all_riddles import riddles_json

print("hiii") 
def main():
    riddles_list = riddles_json['riddles']

    for riddle in riddles_list:
        print(riddle["question"])



main()
