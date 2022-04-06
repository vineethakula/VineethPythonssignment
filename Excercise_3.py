import json

 

def test_exercise3(json_string):

    with open(r'../payloads/IM/test.json') as f:

        data = json.loads(f.read())

        data.pop(json_string)

        new_data = json.dumps(data)

        print(new_data)

       

    with open(r'../payloads/IM/test.json','w') as f:

        f.write(json.dumps(new_data))

        f.close      

                     

test_exercise3("images")
