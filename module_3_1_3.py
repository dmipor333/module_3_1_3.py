calls = 0
def count_calls():
    global calls
    calls = calls + 1
    count_calls()
    def string_info(string):
        string1 = {len(string), string.upper(), string.lower()}
        print(string1)
    string_info('Copibara')
    print(string_info('Copibara'))
    count_calls()
    def is_contains(string, list_to_search):
        print(string in list_to_search)
        is_contains('Urban', ['Urban', 'BaNaN', 'ban'])
    count_calls()
print(calls)