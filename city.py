cityl = {
    'city': 'Москва',
    'temperature': 20
}
print(cityl['city'])
cityl['temperature'] = cityl['temperature'] - 5
print(cityl)
print(cityl.get('country'))
print('country' in cityl)
cityl['country'] = 'Россия'
cityl['date'] = '27.05.2019'
print(len(cityl))
