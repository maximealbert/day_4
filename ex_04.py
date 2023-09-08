from mongoengine import connect, Document, StringField, ReferenceField, ListField
import requests

# Define the MongoDB connection and database
connect('teams_api', host='localhost', port=27017)

class Student(Document):
    name = StringField(required=True)
    age = StringField()

class Message(Document):
    text = StringField(required=True)
    sender = ReferenceField(Student)

class Channel(Document):
    name = StringField(required=True)

class Chat(Document):
    name = StringField(required=True)
    members = ListField(ReferenceField(Student))
    messages = ListField(ReferenceField(Message))

def getallchannels():
    headers = {
        'Authorization': f'Bearer eyJ0eXAiOiJKV1QiLCJub25jZSI6InQ0c3g4Vms3bWIweFdZRkhyMUR1Zk04Tm1ia2dLMERBVEVEVGZrdXdCdU0iLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNjk0MTU4NDA2LCJuYmYiOjE2OTQxNTg0MDYsImV4cCI6MTY5NDI0NTEwNiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhVQUFBQW5JbFh4cWk1T00xalRYUWIvdzlEMGdSRzRiaWY5azdROTIwRzBybWM0VVM1VjhWQmFlTHBnb2JCV0xXWkI5bWJIVW5SUGsvT05IWEZjUmdjMjY5dEVhRUpPZjloQnIzckF2ekxyM3d1TndRPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiQWxiZXJ0IiwiZ2l2ZW5fbmFtZSI6Ik1heGltZSIsImlkdHlwIjoidXNlciIsImluX2NvcnAiOiJ0cnVlIiwiaXBhZGRyIjoiMTYzLjUuMjMuMzgiLCJuYW1lIjoiTWF4aW1lIEFsYmVydCIsIm9pZCI6ImRkMTNkNDQ0LTU0NGQtNGM5Yi1iMzI5LWEzN2EyZjM0ZWU1NiIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS00NTQ3NSIsInBsYXRmIjoiNSIsInB1aWQiOiIxMDAzMjAwMUM4NjkwNzJGIiwicmgiOiIwLkFYUUF5clFja0dLNEtVQ1RCdVhORDIyZmhnTUFBQUFBQUFBQXdBQUFBQUFBQUFCMEFOSS4iLCJzY3AiOiJHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCBUZWFtLlJlYWRCYXNpYy5BbGwiLCJzdWIiOiJNNUFIN0NkWWVMWE83YVFYekV4b0FndHByUWZyekRsam42SjYyeG5RNE9jIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IkVVIiwidGlkIjoiOTAxY2I0Y2EtYjg2Mi00MDI5LTkzMDYtZTVjZDBmNmQ5Zjg2IiwidW5pcXVlX25hbWUiOiJtYXhpbWUuYWxiZXJ0QGVwaXRlY2guZGlnaXRhbCIsInVwbiI6Im1heGltZS5hbGJlcnRAZXBpdGVjaC5kaWdpdGFsIiwidXRpIjoiTG5lOEQyaFU1a0s1SzdqZHpDeGtBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX3NzbSI6IjEiLCJ4bXNfc3QiOnsic3ViIjoiQTc0QVdVNkRSR1RhdHJiQWE2RExkYklueUhIazFsOTJrVTBxRWNwQ1QwQSJ9LCJ4bXNfdGNkdCI6MTQxNzgwNDg4NywieG1zX3RkYnIiOiJFVSJ9.LWOFRWqXkZn7JIqfs_io7KQlZgakcH7kAlh_Ni3FoY0RxZKeIn0d9RbNK_eTOXT3MFYDNdO5dmRUbHfYGGvMuuasKRioUEpGYLpxmARc4lrhyhxHZNt3msDzVsPEFqk3Pta4CGBhNhnBpa6qEvZ_MqQG3v9nzOF4lcDXHEt8OFTG9yWkrlmjAh0hw72cZ1iz4-kIovCQa0uiZ8pVvwl1o7vW0-Nsg3U5hxl43pMkXBaPmMlyabzjS6VEc1bUafIaLYY5LolToVvDBgTHMyLSx-wKwfvFI4c-yzqTHtpoGFfUt_XOmbaQt6xdWJnI_k7njGukMrhU2tMtwt1cLtm9Lg',
    }

    api_url = 'https://graph.microsoft.com/v1.0/me/joinedTeams'
    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        username = data.get('displayName', 'N/A')
        user_id = data.get('id', 'N/A')  # Assuming the API returns JSON data
        # print(data['value'])

        list_final = []

        for team in data['value']:


            list_final = list_final + [(team['displayName'], team['id'])]
            elementtoadd = Channel(name=team['displayName']).save()

        return list_final

    except requests.exceptions.RequestException as e:
        return 'Error'

# Create and save sample data
student1 = Student(name="John", age="22").save()
student2 = Student(name="Alice", age="21").save()
student3 = Student(name="Bob", age="23").save()
student4 = Student(name="Eve", age="20").save()

chat1 = Chat(name="Chatroom 1", members=[student1, student2], messages=[]).save()
chat2 = Chat(name="Chatroom 2", members=[student3, student4], messages=[]).save()

message1 = Message(text="Hello, World!", sender=student1).save()
message2 = Message(text="Hi there!", sender=student2).save()
message3 = Message(text="How's it going?", sender=student3).save()
message4 = Message(text="Good, thanks!", sender=student4).save()

chat1.messages.extend([message1, message2])
chat1.save()
chat2.messages.extend([message3, message4])
chat2.save()

# I only manage to get the channels from the previous requests
getallchannels()