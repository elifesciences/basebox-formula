echo 'hello, world':
    cmd.run

{% set process = "tester" %}

/opt/{{ process }}.py:
    file.managed:
        - source: salt://basebox/config/test.py

{{ process }}-template:
    file.managed:
        - name: /lib/systemd/system/{{ process }}@.service
        - source: salt://basebox/config/lib-systemd-system-test.service
        - template: jinja
        - context:
            process: {{ process }}
        - require:
            - /opt/{{ process }}.py
