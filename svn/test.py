import pysvn

def login(realm, username, may_save):
    username = raw_input("Please enter username: ")
    password = raw_input("Please enter your password: ")
    return True, username, password, False

client = pysvn.Client()
client.callback_get_login = login

# this will work when I am in the repo
#file_content = client.cat("build.gradle")
#print(file_content)

svnRoot = "https://rgbusvn.us.oracle.com/svn/rgbucwi/locate/branches/chris_locate_16_1/Source%20Code"
headrev = client.revpropget("revision", url=svnRoot)[0].number
print(headrev)
