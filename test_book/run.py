import pytest
from test_book.common.utils import *

t=get_time()
pytest.main(['-v',f'--html={report_path}/{t}.html',case_path])