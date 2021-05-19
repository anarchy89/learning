# Before you can use the jobs API, you need to set up an access token.
# Log in to the IBM Q experience. Under "Account", generate a personal 
# access token. Replace 'PUT_YOUR_API_TOKEN_HERE' below with the quoted
# token string. Uncomment the APItoken variable, and you will be ready to go.

APItoken = ''

config = {
    'url': 'https://quantumexperience.ng.bluemix.net/api',

    # If you have access to IBM Q features, you also need to fill the "hub",
    # "group", and "project" details. Replace "None" on the lines below
    # with your details from Quantum Experience, quoting the strings, for
    # example: 'hub': 'my_hub'
    # You will also need to update the 'url' above, pointing it to your custom
    # URL for IBM Q.
    'hub': None,
    'group': None,
    'project': None
}

if 'APItoken' not in locals():
raise Exception('Please set up your access token. See Qconfig.py.')

#APItoken = '9ea741f16ed5905d42f3978ea8b6ccc678649090519cfd59b490f5a10c5d08deb63c13f8177541fb04df206d67634f27c30b9bd9b75d0f202f82aeef14f841d3'

#config = {
#    'url': 'https://quantumexperience.ng.bluemix.net/api',
    # The following should only be needed for IBM Q users.
#    'hub': 'MY_HUB',
#    'group': 'MY_GROUP',
#    'project': 'MY_PROJECT'
#}
