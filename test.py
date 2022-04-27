from password_strength import PasswordStats
from password_strength import PasswordPolicy

  # length of required password
policy = PasswordPolicy.from_names(
    strength=0.66  # need a password that scores at least 0.5 with its strength
)









stats = PasswordStats('U8yR=6`83$LW')
print(stats.strength())  #-> Its strength is 0.585

# stats = PasswordStats('V3ryG00dPassw0rd?!')
# print(stats.strength())  #-> Its strength is 0.767