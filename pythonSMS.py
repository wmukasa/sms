# import package
import africastalking


# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "24f35d9749d946fe077b295abba5f4b931f44bba634978b0b02d981ac048bd68"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
#response = sms.send("Gd afternoon, on Sunday we're having our meeting for the INTRODUCTION &WEDDING CEREMONIES OF MUKASA WILLY WAMALA.At Mengo time 2PM Dr.Tonny 0702920510", ["+256704160994"])

# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send("William!", ["+256704160994"], callback=on_finish)