---
layout: page
title: "Publications"
permalink: /publications/
---

Below is a list of my publications. For full details, see each entry.

{% for pub in site.publications %}
- [{{ pub.title }}]({{ pub.url }}) ({{ pub.date | date: '%Y' }})
{% endfor %} 