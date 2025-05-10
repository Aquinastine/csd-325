#Luttrell, Jason Module 9.2 APIs
#Establishes a connection to an API and prints the response

import requests,sys,json

def main():
    response = requests.get("http://api.open-notify.org/astros")
    
    status = response.status_code
    
    #Check to see if the request was a success. if not provide a message
    #and exit.
    if not str(status)[0] =='2':
        print(f"There was a problem with the API, the Error Code is: {status}")
        print("Goodbye")
        sys.exit()

    #Print the raw Response
    #print(response.json())
    
    #print the formatted response
    jprint(response.json())


#Print a JSON in a format that separates each element in a new line
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# If this program was run (instead of imported), run it:
if __name__ == '__main__':
    main()