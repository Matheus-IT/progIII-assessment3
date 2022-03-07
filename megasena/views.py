from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class UploadLotteryFileView(View):
    def get(self, request: HttpRequest):
        return render(request, 'megasena/upload_lottery_file.html')

    def post(self, request: HttpRequest):
        pass
