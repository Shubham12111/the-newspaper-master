from django.shortcuts import render
from datetime import datetime

from .utils import *
from .models import *
import ast
# Create your views here.

def create_news(source, issue, date, news_title, news_image, news_content):
    News.objects.create(
        source=source,
        issue=issue,
        date=date,
        news_title=news_title,
        news_image=news_image,
        news_content=news_content
    )

def homepage(request):
    today_date = datetime.now()
    formatted_date = today_date.strftime("%A, %d %B, %Y")
    if not News.objects.filter(date=formatted_date).exists():
        # get trt world homepage news
        news_title, _, news_image = get_main_news_title_image()
        news_content = get_main_news_content()
        news_content = news_content[:-1]
        total_records = News.objects.count()
        create_news("trtworld", total_records+1, formatted_date, news_title, news_image, news_content)

        # get marvel universe news
        mcu_news = get_marvel_news()
        first_mcu_news = mcu_news["news"][0]
        second_mcu_news = mcu_news["news"][1]

        first_mcu_content = get_summarization(str(first_mcu_news["text"]))
        second_mcu_content = get_summarization(str(second_mcu_news["text"]))

        mcu_news = {
            "first_mcu_news_title": first_mcu_news["title"],
            "first_mcu_news_content": first_mcu_content,
            "first_mcu_news_image": first_mcu_news["image"],
            "second_mcu_news_title": second_mcu_news["title"],
            "second_mcu_news_content": second_mcu_content,
            "second_mcu_news_image": second_mcu_news["image"]
        }

        create_news("mcu_1", total_records+1, formatted_date, first_mcu_news["title"], first_mcu_news["image"], first_mcu_content)
        create_news("mcu_2", total_records+1, formatted_date, second_mcu_news["title"], second_mcu_news["image"], second_mcu_content)

        # get harry potter universe news
        hp_news = get_hp_news()
        first_hp_news = hp_news["news"][0]
        second_hp_news = hp_news["news"][1]

        first_hp_content = get_summarization(str(first_hp_news["text"]))
        second_hp_content = get_summarization(str(second_hp_news["text"]))

        hp_news = {
            "first_hp_news_title": first_hp_news["title"],
            "first_hp_news_content": first_hp_content,
            "first_hp_news_image": first_hp_news["image"],
            "second_hp_news_title": second_hp_news["title"],
            "second_hp_news_content": second_hp_content,
            "second_hp_news_image": second_hp_news["image"]
        }

        create_news("hp_1", total_records+1, formatted_date, first_hp_news["title"], first_hp_news["image"], first_hp_content)
        create_news("hp_2", total_records+1, formatted_date, second_hp_news["title"], second_hp_news["image"], second_hp_content)

        return render(request, 'index.html', {
            "issue": total_records+1,
            "date": formatted_date,
            "title": news_title,
            "image": news_image,
            "content": news_content,
            "hp_news": hp_news,
            "mcu_news": mcu_news
        })
    else:
        trt_source, mcu1_source, mcu2_source, hp1_source, hp2_source = "trtworld", "mcu_1", "mcu_2", "hp_1", "hp_2"
        # get trt world news
        trt_matching_records = News.objects.filter(source=trt_source, date=formatted_date)
        trt_world_news = trt_matching_records.first()
        news_issue = trt_world_news.issue
        news_date = trt_world_news.date
        news_title = trt_world_news.news_title
        news_image = trt_world_news.news_image
        news_content = trt_world_news.news_content
        news_content_list = ast.literal_eval(news_content)

        # get mcu news
        mcu_1_matching_records = News.objects.filter(source=mcu1_source, date=formatted_date)
        mcu_1_news = mcu_1_matching_records.first()
        mcu_1_news_title = mcu_1_news.news_title
        mcu_1_news_image = mcu_1_news.news_image
        mcu_1_news_content = mcu_1_news.news_content
        mcu_1_news_content = mcu_1_news_content.split('>, <')
        mcu_1_news_content = [s.replace("Sentence: ", "").replace(">", "").replace("<", "").replace("[", "").replace("]", "") for s in mcu_1_news_content]


        mcu_2_matching_records = News.objects.filter(source=mcu2_source, date=formatted_date)
        mcu_2_news = mcu_2_matching_records.first()
        mcu_2_news_title = mcu_2_news.news_title
        mcu_2_news_image = mcu_2_news.news_image
        mcu_2_news_content = mcu_2_news.news_content
        mcu_2_news_content = mcu_2_news_content.split('>, <')
        mcu_2_news_content = [s.replace("Sentence: ", "").replace(">", "").replace("<", "").replace("[", "").replace("]", "") for s in mcu_2_news_content]

        mcu_news = {
            "first_mcu_news_title": mcu_1_news_title,
            "first_mcu_news_content": mcu_1_news_content,
            "first_mcu_news_image": mcu_1_news_image,
            "second_mcu_news_title": mcu_2_news_title,
            "second_mcu_news_content": mcu_2_news_content,
            "second_mcu_news_image": mcu_2_news_image
        }

        # get hp news
        hp_1_matching_records = News.objects.filter(source=hp1_source, date=formatted_date)
        hp_1_news = hp_1_matching_records.first()
        hp_1_news_title = hp_1_news.news_title
        hp_1_news_image = hp_1_news.news_image
        hp_1_news_content = hp_1_news.news_content
        hp_1_news_content = hp_1_news_content.split('>, <')
        hp_1_news_content = [s.replace("Sentence: ", "").replace(">", "").replace("<", "").replace("[", "").replace("]", "") for s in hp_1_news_content]

        hp_2_matching_records = News.objects.filter(source=hp2_source, date=formatted_date)
        hp_2_news = hp_2_matching_records.first()
        hp_2_news_title = hp_2_news.news_title
        hp_2_news_image = hp_2_news.news_image
        hp_2_news_content = hp_2_news.news_content
        hp_2_news_content = hp_2_news_content.split('>, <')
        hp_2_news_content = [s.replace("Sentence: ", "").replace(">", "").replace("<", "").replace("[", "").replace("]", "") for s in hp_2_news_content]

        hp_news = {
            "first_hp_news_title": hp_1_news_title,
            "first_hp_news_content": hp_1_news_content,
            "first_hp_news_image": hp_1_news_image,
            "second_hp_news_title": hp_2_news_title,
            "second_hp_news_content": hp_2_news_content,
            "second_hp_news_image": hp_2_news_image
        }

        return render(request, 'index.html', {
            "issue": news_issue,
            "date": news_date,
            "title": news_title,
            "image": news_image,
            "content": news_content_list,
            "hp_news": hp_news,
            "mcu_news": mcu_news
        })
