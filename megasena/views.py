from datetime import datetime
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import pandas as pd
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from megasena.forms import UploadLotteryFile
from megasena.models import Draw


class UploadLotteryFileView(View):
    def get(self, request: HttpRequest):
        form = UploadLotteryFile()
        return render(request, 'megasena/upload_lottery_file.html', locals())

    def post(self, request: HttpRequest):
        form = UploadLotteryFile(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponse('Erro: Submeter formulário novamente!')

        data = form.cleaned_data

        if data['start_from_scratch']:
            self.delete_everything()

        df = pd.read_csv(data['file'], sep='\t')

        for line in df.to_records():
            date = self.convert_date(line[2])

            Draw.objects.create(
                id=line[1],
                date=date,
                ball1=line[3],
                ball2=line[4],
                ball3=line[5],
                ball4=line[6],
                ball5=line[7],
                ball6=line[8],
            )
        return redirect('admin:index')

    def delete_everything(self):
        Draw.objects.all().delete()

    def convert_date(self, date: str) -> str:
        """Coverts DD/MM/YYYY to YYYY-MM-DD"""
        return datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d')


class ListLotteryRecords(ListView):
    model = Draw
    paginate_by = 20

    def get_queryset(self, *args, **kwargs):
        #  Return in reverse id order
        draws = super().get_queryset(*args, **kwargs).order_by('-id')
        return draws


class LotteryDetailView(DetailView):
    model = Draw
