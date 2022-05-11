def test_incomes_list(client):
    """
    Given:
    When:
    Then
    """
    response = client.get("v1/incomes/")
    assert response.status_code == 200
