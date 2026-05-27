from src.nginx_config_validator import validate_nginx_configs


def test_nginx_validation():
    results = validate_nginx_configs("config")

    assert results["passed"] is True
    assert results["missing_headers"] == []
    assert results["missing_directives"] == []