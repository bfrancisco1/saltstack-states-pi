{% for user, args in pillar['users'].iteritems() %}
{{ user }}:
  user.present:
    - fullname: {{ args['fullname'] }}
    - password: {{ args['password'] }}
    - hash_password: false
{% endfor %}