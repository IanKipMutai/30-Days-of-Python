def count_lines_and_words(path):
    
    with open(path,  encoding = 'utf-8') as f :
        lines = f.read()
        no_lines =len( lines.splitlines())
        no_words = len(lines.split())
        return [
            f'Number of lines = {no_lines}'
            
            f'Number of words = {no_words}'
        ]
            

print(count_lines_and_words('C:/Users/hp/Desktop/30 Days of Python/michelle_obama_speech.txt'))