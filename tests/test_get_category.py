import pytest
from unittest.mock import Mock, MagicMock
from entity.category import Category
from services.get_category import get_all_categories

def test_get_all_categories(mocker):
    # Create a mock for the open_connection function
    open_connection_mock = mocker.patch('mysql.connector.connect', return_value=MagicMock())
    cursor_mock = mocker.MagicMock()
    cursor_mock.fetchall.return_value = [(1, 'Category 1', 'Description 1', 2)]
    open_connection_mock.return_value.cursor.return_value = cursor_mock

    # Call the function you want to test
    result = get_all_categories()

    # Assertions
    assert result == [Category(categoria='Category 1', descricao='Description 1', idtipocategoria=2)]
    cursor_mock.execute.assert_called_with("SELECT * FROM TB_CATEGORIA")
    #cursor_mock.close.assert_called_once()
    open_connection_mock.return_value.close.assert_called_once()

if __name__ == '__main__':
    pytest.main()
