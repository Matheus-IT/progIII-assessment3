from django.urls import path
from .views import LotteryDetailView, UploadLotteryFileView, ListLotteryRecords


urlpatterns = [
    path(
        'loadfile/',
        UploadLotteryFileView.as_view(),
        name='upload-lottery-file',
    ),
    path('megasena/', ListLotteryRecords.as_view(), name='list-records'),
    path(
        'megasena/<int:pk>/',
        LotteryDetailView.as_view(),
        name='detail-records',
    ),
]
