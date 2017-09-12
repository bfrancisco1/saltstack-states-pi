{% for user, args in pillar['groups'].iteritems() %}
{{ user }}:
  user.present:
    - fullname: {{ args['fullname'] }}
    - password: {{ args['password'] }}
{% endfor %}