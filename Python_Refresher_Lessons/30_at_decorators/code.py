# Function tools library
import functools

# A user who is a 'guest' who should not be able to access the admin password.
user = {"username": "Jose", "access_level": "guest"}

# 'make_secure' is a decorator function
def make_secure(func):
  @functools.wraps(func)
  def secure_function(*args, **kwargs): # use args and/or kwargs if the func requires arguments. (We don't need any here in this example)
    if user["access_level"] == "admin":
      return func()
    else: 
      return f"No admin permissions for {user['username']}."

  return secure_function

# @make_secure is the same as make_secure(get_admin_password())
@make_secure
def get_admin_password():
  return "1234"

print(get_admin_password.__name__) # get_admin_password, the @functools.wraps gives us the original func name, get_admin_password
print("Not an admin: ", get_admin_password())

user = {"username": "Sam", "access_level": "admin"}
print("Sam as an admin: ", get_admin_password())