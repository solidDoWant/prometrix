from prometrix import PrometheusConfig, get_custom_prometheus_connect


def test_client_cert_is_set_on_session():
    prom = get_custom_prometheus_connect(
        PrometheusConfig(
            url="https://prometheus.example.com", client_cert=("/tmp/cert", "/tmp/key")
        )
    )
    assert prom._session.cert == ("/tmp/cert", "/tmp/key")


def test_no_client_cert_by_default():
    prom = get_custom_prometheus_connect(
        PrometheusConfig(url="https://prometheus.example.com")
    )
    assert prom._session.cert is None
