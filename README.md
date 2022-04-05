# Автоматизация тестирования сервиса https://guldog.ru
___

Так как на руках нет документации с требованиями по проекту,
тестовые сценарии написаны на интуитивной основе.

Далее в описании ТС = тестовый сценарий, ОР = ожидаемый результат.

Автоматизированы три первых сценария, запуск осуществляется с помощью PyTest.
Последовательное выполнение автоматизированных кейсов занимает 8-9 сек.
** Отчет о прохождении ТК находится в файле report.html **

---

#### ТС № 1. Проверка переключателя и рассчета цены при изменении "Количества собак".<br/>
Цель: Проверить переключение формы при включении/выключении "Первая пробная прогулка" 
и изменение цены при установке различных значений параметра "Количество собак"
1. Переключить параметр "Количество собак" от 1 до 4<br/>
   ОР: "Цена от":<br/>
   1 собака = 645р.<br/>
   2 собаки = 895р.<br/>
   3 собаки = 1145р.<br/>
   4 собаки = 1395р.<br/>
2. Включить "Первая пробная прогулка"<br/>
   ОР: Длительность прогулки - 25 минут, "Цена от" = 190р.<br/>
3. Выключить "Первая пробная прогулка"<br/>
   ОР: Происходит возврат на форму со значениями установленными на шаге 1.<br/>

---
#### ТС № 2. Проверка отправки формы при нажатии "Узнать точную цену" (негативный сценарий).<br/>
Цель: Проверить обязательность заполнения полей при нажатии на "Указать точную цену"
1. Нажать "Указать точную цену" (поля должны быть пусты).<br/>
   ОР: Отправка не произошла. Под полями "Телефон" и "E-mail для отчета" появились сообщения о необходимости к заполнению.
2. Вписать в поле "Телефон" символы отличные от цифр.
   ОР: В поле "Телефон" возможен ввод только цифр, буквенные/спецсимволы игнорируются.
3. Частично заполнить поле "Телефон" и нажать на "Узнать точную цену"<br/>
   ОР: Отправка не произошла, поле "Телефон" очистилось. Под полями "Телефон" и "E-mail для отчета" появились сообщения о необходимости к заполнению.
4. Заполнить поле "Телефон" корректным значением и нажать на "Узнать точную цену".<br/>
   ОР: Отправка не произошла. Под полем "E-mail для отчета" появилось сообщение о необходимости к заполнению. Под полем "Телефон" ошибка отсутствует.
5. Ввести некорректный email в поле "E-mail для отчета"
   ОР: Появилось сообщение об ошибке "Укажите корректный e-mail адрес"
---
#### ТС № 3. Проверка перехода по ссылкам на форме.
Цель: Проверить, что происходит переход по ссылкам "Подробнее о бонусной программе" и "Пользовательское соглашение"
1. Нажать на ссылку "Подробнее о бонусной программе"
   ОР: Осуществлен переход на адрес https://guldog.ru/bonus_program
2. Нажать на ссылку "Пользовательское соглашение"
   ОР: Осуществлен переход на адрес https://guldog.ru/termsofuse

---
#### ТС № 4. Проверка корректного поведения ползунка диапазона
(для автоматизации необходим скрипт применяемый при движении ползунка).<br/>
Цель: Убедиться, что изменяется значение "Цена от" при изменении положения ползунка диапазона "Кол-во выгулов".
1. Перейти к форме "Стоимость выгула".
2. Установить параметр "Количество собак" = 1
3. Переместить ползунок на значение 1.
   ОР: Значение "Цена от:" равна 645 р.
4. Переместить ползунок на значение 30.
   ОР: Значение "Цена от:" равна 19350 р.
5. Переместить ползунок на значение 60.
   ОР: Значение "Цена от:" равна 38700 р.
