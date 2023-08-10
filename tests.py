import requests
import unittest
from unittest import TestCase
from mentors import get_names, get_top_3 , get_course_duration
from mentors import YandexDisk

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


class TestGetName(TestCase):
    def test_get_names(self):
        expected = 'Адилет , Азамат , Александр , Алексей , Алена , Анатолий , Анна , Антон , Вадим , Валерий , Владимир , Денис , Дмитрий , Евгений , Елена , Иван , Илья , Кирилл , Константин , Максим , Михаил , Никита , Николай , Олег , Павел , Ринат , Роман , Сергей , Татьяна , Тимур , Филипп , Эдгар , Юрий'
        result = get_names(mentors)
        self.assertEqual(result, expected)

    def test_get_top_3(self):
        expected = [['Александр', 10], ['Евгений', 5], ['Максим', 4]]
        result = get_top_3(mentors)
        self.assertEqual(result, expected)

    def test_get_course_duration(self):
        expected = 'Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев), cамый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)'
        result = get_course_duration(courses, durations)
        self.assertEqual(result, expected)


TOKEN = "y0_AgAAAAA0Fa5UAADLWwAAAADg1gteBrYmb7mbQUuqKjPjaxcerAdhaDA"
ya = YandexDisk(token=TOKEN)
# data_disk = ya.get_files_list()
# ya.upload_file_to_disk('testfoto_for_dztests.jpg', 'testfoto.jpg')


class TestYandexDisc(TestCase):
    def test_status_upload_file_to_disk(self):
        expected = 201
        result = ya.upload_file_to_disk('testfoto_for_dztests.jpg', 'testfoto.jpg')
        self.assertEqual(result, expected)

    @unittest.expectedFailure
    def test_fuls_status_upload_file(self):
        expected = 404
        result = ya.upload_file_to_disk('testfoto_for_dztests.jpg', 'testfoto.jpg')
        self.assertEqual(result, expected)

    def test_name_file_in_disk(self):
        a = 'testfoto.jpg'
        list = ya.get_list_names_files()
        self.assertIn(a,list)