# # merge - inner, outer ... 

# # view and edit

# home/<workspaceID>/merge/inner, outer...

#view and edit : 
# user uploads excel in frontend, -> save in database - backend 
#                                 ->show in tabular form in frontend -> edit by user->send 
#                                   back new data in csv form-> save in database- backend 

from django.urls import path
from .views import InnerMergeView, OuterMergeView, IntersectionMergeView, CountSubSheetsView, ExcelToCsvView

urlpatterns = [
    path('merge/inner', InnerMergeView.as_view(), name='inner-merge'),
    path('merge/outer', OuterMergeView.as_view(), name='outer-merge'),
    path('merge/intersection', IntersectionMergeView.as_view(), name='intersection'),
    path('merge/count',CountSubSheetsView.as_view(), name='count-sheets' ),
    path('view-edit/store-csv', ExcelToCsvView.as_view(), name='excel-to-csv'),

]
