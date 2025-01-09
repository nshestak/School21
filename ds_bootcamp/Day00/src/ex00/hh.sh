#!/bin/sh

# Выполнение запроса к API HeadHunter для получения вакансий по запросу "data-science"
# Результат запроса будет сохранен в файл hh.json
curl -k -H 'Authorization: Bearer USERH26FQMQLAGVSJAFFMI7GOTPH3SKBSL8EB38NJKLQH1I7HS4HM05CAVEAPQ6I' \
     -H 'User-Agent: api-test-agent' \
     'https://api.hh.ru/vacancies?text=data-science&per_page=20' | jq . > hh.json

# Вывод сообщения о успешном сохранении данных
echo "Данные успешно сохранены в hh.json"
