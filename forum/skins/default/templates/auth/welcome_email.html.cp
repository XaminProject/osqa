# -*- coding: utf-8 -*-
{% load i18n extra_tags email_tags %}

{% declare %}
    prefix = settings.EMAIL_SUBJECT_PREFIX
    app_name = settings.APP_SHORT_NAME

    exclude_greeting = True
    exclude_finetune = True
{% enddeclare %}

{% email %}
    {% subject %}{% blocktrans %}{{ prefix }} Welcome to {{ app_name }}{% endblocktrans %}{% endsubject %}

    {% htmlcontent notifications/base.html %}
        <p style="{{ p_style }}">
            {% blocktrans %}Howdy and welcome to {{ app_name }}. We know you're busy, so we'll keep this real simple.{% endblocktrans %},
        </p>

        <p style="{{ p_style }}">{% trans "Here's your login info (store it in a cool dry place):" %}</p>

        <p style="{{ p_style }}">{% trans "Username: " %} {{ recipient.username }}<br />
        <b>{% trans "Password: As IF we would send your password in cleartext!" %}</b></p>

        <p style="{{ p_style }}">{% trans "The following link will help us verify your email address:" %}</p>

        <p style="{{ p_style }}"><a  style="{{ a_style }}" href="{% fullurl auth_validate_email user=recipient.id,code=validation_code %}">{% trans "Validate my email address" %}</a></p>

        <p style="{{ p_style }}">{% trans "If the above link is not clickable, copy and paste this url into your web browser's address bar:" %}</p>

        <p style="{{ p_style }}">{% fullurl auth_validate_email user=recipient.id,code=validation_code %}</p>
    {% endhtmlcontent %}

{% textcontent notifications/base_text.html %}
{% blocktrans %}سلام

به سیستم پرسش و پاسخ زمین خوش آمدید. نام کاربری شما.{% endblocktrans %},

{% tras "نام کاربری : " %} {{ recipient.username }}

{% fullurl auth_validate_email user=recipient.id,code=validation_code %}

{% trans "اگر نتوانستید بر روی این لینک کلیک کنید می توانید با کپی کردن لینک فوق در نوار آدرس مرورگر خود، آن را مشاهده نمایید

:" %}

{% fullurl auth_validate_email user=recipient.id,code=validation_code %}
{% endtextcontent %}

{% endemail %}

