from django.contrib.auth.models import User
import os

#############  GENERAL CONFIG #############
users = [
    {
        'first_name': 'Admin',
        'username': 'admin',
        'last_name': 'Growtech',
        'password': '+grow2020',
        'email': 'admin@growtechnologies.com.br',
        'is_superuser': True,
    },
]
##########################################

# Cria super usuario, developer, reviewer e tenant.
for user in users:
    # verifica se usuario ja existe
    if User.objects.filter(username=user['username']).exists():
        print('\nUsername "%s" is already in use.' % user['username'])
    else:
        new_user = User.objects.create_superuser(first_name=user['first_name'], last_name=user['last_name'],
                                            password=user['password'], email=user['email'], username=user['username'])
        new_user.save()
        print('\nUser "%s" created!' % user['username'])