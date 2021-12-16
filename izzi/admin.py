from datetime import datetime

from django.contrib import admin
from django.forms import forms
from django.shortcuts import redirect, render
from django.urls import path

from izzi.models import User


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    change_list_template = "users_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        """ We can also upgrade the parser, and handle errors, for example,
            if the incoming data file is not valid,
            but for the simplicity of the project, I did it as it is  """

        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            users_list = [data.decode('utf-8').split(',') for data in csv_file][1:]
            user_data = [
                {
                    'first_name': user[0],
                    'last_name': user[1],
                    'birthday': datetime.strptime(user[2], '%Y/%m/%d'),
                    'date_of_registration': datetime.strptime(user[3][:-1], '%Y/%m/%d')
                }
                for user in users_list
            ]
            User.objects.bulk_create([User(**user) for user in user_data])
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "csv_form.html", payload
        )
