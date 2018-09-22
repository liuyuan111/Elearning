from django.db import models
from datetime import datetime
from django.conf import settings


# Banner
class Banner(models.Model):
    text_info1 = models.CharField('信息1', max_length=50, default='')
    text_info2 = models.CharField('信息2', max_length=50, default='')
    text_info3 = models.CharField('信息3', max_length=50, default='')
    cover = models.ImageField('轮播图', upload_to='static/assets/images/banner', default=None)
    link_url = models.URLField('图片链接', max_length=100)
    idx = models.IntegerField('索引')
    # is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info1

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


# 明星学员
class StarStudent(models.Model):
    name = models.CharField('姓名', max_length=50)
    company = models.CharField('公司', max_length=50)
    head_img = models.ImageField('头像', upload_to='static/assets/images/students')
    comment = models.CharField('评论',  max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '明星学员'
        verbose_name_plural = '明星学员'


# 分类(Android 学院 / iOS 学院 / HTML5 学院 / JavaEE 学院/ Python 学院)
class Category(models.Model):
    title = models.CharField('标题', max_length=100)
    infor = models.TextField('简介', max_length=500)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ('学院')
        verbose_name_plural = verbose_name


# 讲师
class Teacher(models.Model):
    name = models.CharField('姓名', max_length=20)
    face = models.ImageField('头像', upload_to='static/assets/images/teacher')
    title = models.CharField('头衔', max_length=20)
    infor = models.TextField('简介', max_length=300, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ('讲师')
        verbose_name_plural = verbose_name


# 课程（Java 基础 Java 网络编程）
class Course(models.Model):
    title = models.CharField('标题', max_length=50)
    body = models.TextField('课程简介', max_length=200)
    cover = models.ImageField('课程封面', upload_to='static/assets/images/courses', default=None)
    runtime = models.IntegerField('时长', default=0)
    pub_date = models.DateField('发布日期',auto_now_add=True)
    attachment = models.FileField('课程资料包', blank=True)
    is_free = models.BooleanField('是否免费', default=False)
    teacher = models.ForeignKey(Teacher,verbose_name='讲师', on_delete=True)
    category = models.ForeignKey(Category,verbose_name='分类', on_delete=True)
    learn_num = models.IntegerField('学习人数',default=100)
    comment_num = models.IntegerField('评论数',default=987)

    # 等级
    JUNIOR = '初级'
    MIDDLE = '中级'
    ADVANCED = '高级'

    LEVELS = (
        (JUNIOR, '初级'),
        (MIDDLE, '中级'),
        (ADVANCED, '高级'),
    )

    level = models.CharField('等级', max_length=20, choices = LEVELS, default=JUNIOR)

    # 星级
    star = models.IntegerField('星级',default=5)
    # 价格
    price = models.IntegerField('价格', default=100)
    # 是否推荐
    recommend = models.BooleanField('是否推荐', default=True)
    # 是否已经发布
    published = models.BooleanField('是否发布', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('课程')
        verbose_name_plural = verbose_name


# 章节
class Section(models.Model):
    title = models.CharField('标题',max_length=100)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ('章节')
        verbose_name_plural = verbose_name

# 视频
class Video(models.Model):
    title = models.CharField('标题',max_length=100)
    video = models.FileField('视频文件', upload_to='static/video')
    play_time = models.CharField('播放时长',max_length=20)
    is_free = models.BooleanField('是否免费',default=False)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=True)
    section = models.ForeignKey(Section,verbose_name='章节',on_delete=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ('视频')
        verbose_name_plural = verbose_name




#########################################################################################################




# 博客分类
class BlogCategory(models.Model):
    name = models.CharField('分类名称', max_length=20, default='')
    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'

    def __str__(self):
        return self.name

# 标签
class Tags(models.Model):
    name = models.CharField('标签名称', max_length=20, default='')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name

# 博客
class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=True)
    category = models.ForeignKey(BlogCategory, verbose_name='博客分类', default=None, on_delete=True)
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    pub_date = models.DateTimeField('发布日期', default=datetime.now)
    cover = models.ImageField('博客封面', upload_to='static/assets/images/blog')
    views = models.IntegerField('浏览数', default=0)
    recommend = models.BooleanField('推荐博客', default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'

# 评论
class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='博客', on_delete=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=True)
    pub_date = models.DateTimeField('发布时间')
    content = models.TextField('内容')

    def __str__(self):
        return self.content
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'


# 合作机构
class Org(models.Model):
    name = models.CharField('名称', max_length=20)
    cover = models.ImageField('博客封面', upload_to='static/assets/images/org', default=None)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '合作机构'
        verbose_name_plural = '合作机构'
