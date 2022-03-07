from django.urls import path
from .views import UploadLotteryFileView


urlpatterns = [
    path(
        'loadfile/',
        UploadLotteryFileView.as_view(),
        name='upload-lottery-file',
    ),
]
