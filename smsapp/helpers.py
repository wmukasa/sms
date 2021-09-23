import africastalking

class SMS:
    def init (self):
        self.username = 'sandbox'
        self.api_key ='24f35d9749d946fe077b295abba5f4b931f44bba634978b0b02d981ac048bd68'
        #initialize the SDK
        africastalking.initialize(self.username, self.api_key)
        #Get the SMS service
        self.sms = africastalking.SMS

    def send(self,*phones):
        
        recipients = phones
        message = "Gd afternoon, on Sunday we're having our meeting for the INTRODUCTION &WEDDING CEREMONIES OF MUKASA WILLY WAMALA.At Mengo time 2PM Dr.Tonny 0702920510"
        try:
            response = self.sms.send(message,recipients)
            return response
        except Exception as e:
            print(f'Encountered an error while sending:{e}')