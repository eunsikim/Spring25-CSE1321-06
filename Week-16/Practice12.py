# dateTranslator(months, '2/14')
def dateTranslator(months, date):
    new_date = date.split("/")

    month = months[ int(new_date[0]) ] # 'February'

    return f"{new_date[1]} day of {month}"

def main():
    months = {
        1:'January', 
        2:'February', 
        3:'March', 
        4:'April', 
        5:'May', 
        6:'June', 
        7:'July', 
        8:'August', 
        9:'September', 
        10:'October', 
        11:'November', 
        12:'December'
    }

    print(dateTranslator(months, "2/14"))





if __name__ == "__main__":
    main()