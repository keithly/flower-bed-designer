from flower_bed_designer import create_app


def test_app_factory_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
