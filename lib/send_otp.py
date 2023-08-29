from twilio.rest import Client
import random

def recive_otp(mob_num,num_otp):
    try:
        account_sid = 'ACbbcd58c2c530843e66b3ac0e83e177e5'
        auth_token = '4fe31b4cab450ec619ad9566ea617896'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='+18145464378',
            body=f'''
             - Parrot- {num_otp} dont share with anyone''',
        to=f'+91{mob_num}'
        )
    except Exception as e:
        print(e)
if __name__=='__main__':
    num = random.randint(10000,99999)
    print(num)
    recive_otp(9886949323,num)