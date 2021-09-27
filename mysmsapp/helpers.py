import africastalking

class SMS:
    def init (self):
        self.username = 'wmukasa'
        self.api_key ='db6816cf46dde48c18b17055b769e8f75e253ba08cc5db8e93e0a8923300fc09'
        #initialize the SDK
        africastalking.initialize(self.username, self.api_key)
        #Get the SMS service
        self.sms = africastalking.SMS

    def send(self,*phones):
        
        recipients = phones
        message = "Hello Love, Sorry for continous Messages, am testing my application for sending sms to people"
        try:
            response = self.sms.send(message,recipients)
            return response
        except Exception as e:
            print(f'Encountered an error while sending:{e}')