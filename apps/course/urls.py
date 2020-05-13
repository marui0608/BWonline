from django.urls import path,re_path
from .views import CourseListView,CourseDetailView,CourseInfoView,CommentsView,AddCommentsView,VideoPlayView


# 要写上 app 的名字

app_name = "course"

urlpatterns = [
    path("list/",CourseListView.as_view(),name='course-list'),
    re_path('course/(?P<course_id>\d+)/',CourseDetailView.as_view(),name='course-detail'),
    # 课程章节信息页
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course-info"),
    #课程评论
    re_path('comment/(?P<course_id>\d+)/', CommentsView.as_view(), name="course-comments"),
    #添加评论
    path('add_comment/', AddCommentsView.as_view(), name="add-comment"),
    # 课程视频播放页
    path('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name="video-play"),
]