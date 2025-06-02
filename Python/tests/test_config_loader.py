def test_config_loader(tmp_path):
    # Vorbereitung: Temporäre JSON-Datei
    config_content = {"key": "value"}
    config_path = tmp_path / "test.json"
    config_path.write_text('{"key": "value"}', encoding="utf-8")

    # Monkeypatch CONFIG_DIR, um den tmp_path zu verwenden
    import config.config_loader as config_loader
    original_config_dir = config_loader.CONFIG_DIR
    config_loader.CONFIG_DIR = tmp_path

    try:
        result = config_loader.load_config("test")
        assert result == config_content
    finally:
        config_loader.CONFIG_DIR = original_config_dir
