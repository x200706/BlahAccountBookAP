"""
URL configuration for FirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from myapp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', views.AccountView.as_view()),
    path('accounts/<id>', views.AccountView.as_view()),
    path('itemkinds/', views.ItemKindsView.as_view()),
    path('itemkinds/<kind>', views.ItemKindsView.as_view()),
    # 因為希望在Swagger上呈現，所以還是把所有路徑刻出來，說實話這邊並不RESTful
    path('canva/CurrentMonthPie', views.CanvaView.as_view().current_month_pie),
    path('canva/ExpenditureBar', views.CanvaView.as_view().expenditure_bar),
    path('canva/IncomeBar', views.CanvaView.as_view().income_bar),
    path('canva/TopTenList', views.CanvaView.as_view().top_ten_list),
    path('canva/TotalAssets', views.CanvaView.as_view().total_assets)
]
