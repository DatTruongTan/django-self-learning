from django.shortcuts import render


def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')


def variable_view(request):
    # my_app/templates/my_app/variable.html

    my_var = {
        'first_name': 'tan dat',
        'last_name': 'truong',
        'some_list': [1, 2, 3],
        'some_dict': {'inside_key': 'inside_value'},
        'user_logged_in': True,
    }

    return render(request, 'my_app/variable.html', context=my_var)