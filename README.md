# Diary App

This application is built using Django and QuillJS.

Features:

1. Create note.
2. View Bunch of notes.
3. View individual notes.

## Snapshots

![Productivity Chart](https://i.ibb.co/vvM5ggN/Screenshot-from-2019-10-20-00-29-35.png)
![Nothing to Show](https://i.ibb.co/Vv1RYb2/Screenshot-from-2019-10-20-00-30-12.png)
![Add Note](https://i.ibb.co/WWdrn16/Screenshot-from-2019-10-19-19-48-38.png)
![View Bunch of Notes](https://i.ibb.co/F6P7CyQ/Screenshot-from-2019-10-19-19-48-49.png)
![View Individual Notes](https://i.ibb.co/Cv6tpXW/Screenshot-from-2019-10-19-19-49-06.png)
{% extends 'entry/base.html' %}
{% load staticfiles %}
{% block content %}

    <div class="container">
        <div class="row">
            {% for diary in diaries %}

                <div class="card col-md-3 m-3">
                    <div class="card-body">
                        <h5 class="card-title">{{ diary.note }}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">{{ diary.posted_date }}</h6>
                        <p class="card-text">
                            {# To render HTML contents without escaping. #}
                            {% autoescape off %}
                                {{ diary.summary }}
                            {% endautoescape %}
                        </p>

                    </div>
                    <div class="card-footer">
                        <a href="{% url 'detail' diary.id %}" class="card-link btn btn-primary btn-block btn-lg">Read
                            More</a>
                    </div>
                </div>

            {% endfor %}
        </div>
        {% if icon %}
            <div class="text-center">
                <p class="text-muted">There's nothing to show</p>
                <img height="300" src="{% static 'icons/empty-easter-basket.jpg' %}" alt="Nothing to Show">
            </div>
        {% endif %}
    </div>

{% endblock %}
{% extends 'entry/base.html' %}
{% block content %}

    <div class="container contact-form">
        <form method="post" action="{% url 'entry' %}" class="mt-5">
            {% csrf_token %}
            {{ addform }}
            <button class="btn btn-primary btn-block btn-lg mt-3" type="submit">Add Entry</button>
        </form>
    </div>

{% endblock %}
{% load staticfiles %}
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Include Quill stylesheet -->
    <link href="https://cdn.quilljs.com/1.0.0/quill.snow.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Vollkorn&display=swap" rel="stylesheet">
    <!-- Include Bootstrap stylesheet -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Add Entry</title>
    <style>
        html body div.container.contact-form form.mt-5 div.ql-container.ql-snow {
            height: 300px;
        }

        body {
            font-family: 'Vollkorn', serif;
        }
    </style>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="{% url 'entry' %}">Diary App</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link mr-3 {% if add_highlight %}
                    active
                {% endif %} " href="{% url 'productivity' %}">
                    <hr class="d-xl-none d-lg-none">
                    <img src="{% static 'icons/chart-line-solid.svg' %}" height="30" width="30"
                         alt="Productivity Chart">
                    <span class="d-xl-none d-lg-none"> &nbsp; Productivity Chart</span>
                    <hr class="d-xl-none d-lg-none">
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link mr-3 {% if add_highlight %}
                    active
                {% endif %} " href="{% url 'entry' %}">
                    <img src="{% static 'icons/plus-square-solid.svg' %}" height="30" width="30" alt="Add Diaries">
                    <span class="d-xl-none d-lg-none"> &nbsp; Add Diaries</span>
                    <hr class="d-xl-none d-lg-none">
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link {% if show_highlight %}
                    active
                {% endif %} " href="{% url 'show' %}">
                    <img src="{% static 'icons/book-solid.svg' %}" height="30" width="30" alt="Show Diaries">
                    <span class="d-xl-none d-lg-none"> &nbsp; Show Diaries</span>
                    <hr class="d-xl-none d-lg-none">
                </a>
            </li>
        </ul>
    </div>
</nav>

<div class="jumbotron jumbotron-fluid text-center">
    <div class="container">
        <h1 class="display-4">{{ title }}</h1>
        <p class="lead">{{ subtitle }}</p>
    </div>
</div>

{% block content %}

{% endblock %}

<a class="fixed-bottom" href="https://github.com/theArjun/diary-app" target="_blank">
    <button class="btn btn-light rounded text-dark float-right">
        <img class="mb-1" height="30"
             src="https://i.pinimg.com/originals/3e/b2/ed/3eb2edd1e1079c1c7891543f3f50ce06.png">
        &nbsp;Developed and Designed by <span class="font-weight-bold">Arjun Adhikari</span>
    </button>

</a>
<!-- Include the Quill library -->
<script src="https://cdn.quilljs.com/1.0.0/quill.js"></script>
<script src="{% static 'js/quill.js' %}"></script>

<!-- Initialize Quill editor -->
<script>
    (function () {
        quilljs_textarea('.quilljs-textarea', {
            modules: {
                toolbar: [
                    ['bold', 'italic', 'underline'],        // toggled buttons
                    [{'list': 'ordered'}, {'list': 'bullet'}],
                    [{'header': [1, 2, 3, 4, 5, 6, false]}],
                    [{'color': []}, {'background': []}],          // dropdown with defaults from theme
                    [{'align': []}],
                ]
            },
            theme: 'snow',
        });
    })();
</script>


<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        crossorigin="anonymous"></script>
</body>
</html>
{% extends 'entry/base.html' %}
{% load staticfiles %}
{% block content %}
    <div class="container">
        {% autoescape off %}
            {{ diary.content }}
        {% endautoescape %}
    </div>


{% endblock %}
{% extends 'entry/base.html' %}
{% load staticfiles %}
{% block content %}
    <div class="container">
        {% if icon %}
            <div class="text-center">
                <p class="text-muted">There's nothing to show</p>
                <img height="300" src="{% static 'icons/empty-easter-basket.jpg' %}" alt="Nothing to Show">
            </div>
        {% else %}
            <canvas id="myChart" width="450" height="200"></canvas>
            <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script>
            <script>
                var ctx = document.getElementById('myChart').getContext('2d');
                var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: [
                            {% for datum in data %}
                                '{{ datum.date_for_chart }}' ,
                            {% endfor %}
                        ],
                        datasets: [{
                            data: [
                                {% for datum in data %}
                                    {{ datum.productivity }} ,
                                {% endfor %}
                            ],
                            label: "Productivity",
                            borderColor: "#eb3477",
                            fill: false
                        }
                        ]
                    },
                    options: {
                        title: {
                            display: true,
                            text: 'In range of 1 to 10'
                        }
                    }
                });
            </script>
        {% endif %}
    </div>
{% endblock %}
