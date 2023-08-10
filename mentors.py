courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

def get_names(list_of_list):
    all_list = []
    for m in list_of_list:
        all_list.extend(m) 
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = list(set(all_names_list))
    all_names_sorted = sorted(unique_names)
    all_names_final = ', '.join(all_names_sorted)
    return all_names_final




def get_top_3(list_of_mentors):
    all_list = []
    for m in range(len(list_of_mentors)):
        all_list += mentors [m] 
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = list(set(all_names_list))

    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)]) 
    popular.sort(key=lambda x:x[1], reverse=True)
    top_3 = popular[0:3:1]
    return top_3


def get_course_duration(list_of_courses, list_duration):
    courses_list = []
    for title, duration in zip(list_of_courses, list_duration):
        course_dict = {"title": title,"duration": duration}
        courses_list.append(course_dict)
    min_c =  min(list_duration)
    max_c = max(list_duration)
    maxes = []
    minis = []
    for index, duration in enumerate(courses_list):
        if duration == max_c:
           maxes.append(index)
        elif duration == min_c:
            minis.append(index)
    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]['title']) # допишите код, который берет по id нужный курс из courses_list и получает название курса из ключа "title"
        for id in maxes:
            courses_max.append(courses_list[id]['title']) # по аналогии допишите такой же код для курсов максимальной длительности
    result = f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_c} месяца(ев), Самый длинный курс(ы): {", ".join(courses_max)} - {max_c} месяца(ев)'
    return result

import requests
import pprint

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url = files_url, headers = headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url = upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path = disk_file_path).get("href", "")
        response = requests.put(href, data = open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        return response.status_code
    def get_names_files(self):
        data = self.get_files_list()
        data_list = data["items"]
        name_list = []
        for element in data_list:
            name_list.append(element['name'])
        
        return name_list

TOKEN = "y0_AgAAAAA0Fa5UAADLWwAAAADg1gteBrYmb7mbQUuqKjPjaxcerAdhaDA"



if __name__ == '__main__':
	names = get_names(mentors)
	print(names)
	top = get_top_3(mentors)
	print(top)
	courseduration = get_course_duration(courses, durations)
	print(courseduration)
    


if __name__ == '__main__':
  ya = YandexDisk(token=TOKEN)
  data_disk = ya.get_files_list()
  ya.upload_file_to_disk('testfoto_for_dztests.jpg', 'testfoto.jpg')