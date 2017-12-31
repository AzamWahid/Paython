favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
peoples = ['jen','sarah','azam','kashif']

for people in peoples:
    if people in favorite_languages.keys():
        print(people.title() + ' '+ 'thanks for responding')
    else:
        print(people.title()+' '+'inviting You to take the poll')