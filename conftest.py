import pytest
from py.xml import html

# Создание дополнительных столбцов
def pytest_html_results_table_header(cells):
	cells.insert(1, html.th('Drop'))		# Заголовок 1-го столбца
	cells.insert(2, html.th('Expected results'))			# Заголовок 2-го столбца
	cells.pop()

def pytest_html_results_table_row(report, cells):
	cells.insert(1, html.td(report.description))	# Содержимое 1-го столбца для конкретного теста
	cells.insert(2, html.td(report.expected_results))		# Содержимое 2-го столбца для конкретного теста
	cells.pop()

# hook для перехвата и модификации данных результатов тестов
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
	pytest_html = item.config.pluginmanager.getplugin('html')
	outcome = yield
	report = outcome.get_result()
	# Добавление значений в таблицу - значения берем из атрибута __doc__ функции и глобальных переменных
	report.description = str( item.function.__doc__ )
	report.expected_results = str(item.module.log['expected_results'])
	# Добавление html и image блоков в результат - значения берем из глобальных переменных
	extra = getattr(report, 'extra', [])
	if report.when == 'call':
		# вставляем html-блок
		if item.module.log_html != 'none':
			extra.append(pytest_html.extras.html(item.module.log_html))
		# вставляем img-блок (картинка будет встроена в отчет)
		# if item.module.log_img != 'none':
		# 	extra.append(pytest_html.extras.image(item.module.log_img, mime_type='image/jpg', extension='jpg'))
		# # вставляем img-блок с url-ссылкой
		# if item.module.log_img_url != 'none':
		# 	extra.append(pytest_html.extras.image(item.module.log_img_url))
		report.extra = extra