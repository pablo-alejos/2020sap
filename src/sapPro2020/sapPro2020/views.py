from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import FormView

from itertools import chain
import json
from django.http import JsonResponse
from django.core import serializers

from book.models import Book
from article.models import Article, Journal
from bookChapter.models import BookChapter
from account.models import Account, Academy, Program
from tag.models import Tag
from project.models import Project


class HomeView(TemplateView):
    template_name = "sap_home.html"


class SearchView(TemplateView):
    template_name = "sap_search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['program_list'] = Program.objects.order_by('name')
        context['academy_list'] = Academy.objects.order_by('name')
        context['account_list'] = Account.objects.order_by('firstName')
        context['project_list'] = Project.objects.order_by('name')
        context['journal_list'] = Journal.objects.order_by('name')
        context['congress_list'] = Congress.objects.order_by('name')
        context['forum_list'] = Forum.objects.order_by('name')
        context['symposuim_list'] = Symposium.objects.order_by('name')
        book_list = Book.objects.all()
        bookChapter_list = BookChapter.objects.all()
        article_list = Article.objects.all()
        context['book_list'] = book_list
        context['bookChapter_list'] = bookChapter_list
        context['article_list'] = article_list
        product_list = list(chain(article_list, book_list, bookChapter_list))
        context['product_list'] = product_list
        return context


def searchAjaxView(request):
    if request.method == "POST" and request.is_ajax:
        body = json.loads(request.body)
        requestData = {}
        for item in body:
            name = item['name']
            requestData[name] = item
        keyISBN = requestData['keyISBN']['value']
        keyISBNC = requestData['keyISBN']['value']
        keyTitleC = requestData['keyTitleC']['value']
        proyect_id = requestData['proyectId']['value']
        program_id = requestData['programId']['value']
        academy_id = requestData['academyId']['value']
        keyTitle = requestData['keyTitle']['value']
        source_Id = requestData['sourceId']['value']
        sourceTipo = requestData['sourceTipo']['value']
        pubYear = requestData['pubYear']['value']
        book_list = Book.objects.all()
        bookChapter_list = BookChapter.objects.all()
        article_list = Article.objects.all()
        program_book_list = Book.objects.none()
        academy_book_list = Book.objects.none()
        program_bookChapter_list = BookChapter.objects.none()
        academy_bookChapter_list = BookChapter.objects.none()
        program_article_list = Article.objects.none()
        academy_article_list = Article.objects.none()
        if 'want_book' in requestData:
            if program_id != 'Programa educativo' and academy_id != 'Cuerpo academico':
                tagCombo_list = (
                    Tag.objects.filter(
                        name=Program.objects.get(id=program_id))
                    | Tag.objects.filter(
                        name=Academy.objects.get(id=academy_id))).distinct()
                book_list = Book.objects.filter(
                    tags__in=list(tagCombo_list)).distinct()
            elif program_id != 'Programa educativo' or academy_id != 'Cuerpo academico':
                if program_id != 'Programa educativo':
                    tagCombo_list = Tag.objects.filter(
                        name=Program.objects.get(id=program_id))
                    book_list = Book.objects.filter(
                        tags__in=list(tagCombo_list)).distinct()
                if academy_id != 'Cuerpo academico':
                    tagCombo_list = Tag.objects.filter(
                        name=Academy.objects.get(id=academy_id))
                    book_list = Book.objects.filter(
                        tags__in=list(tagCombo_list)).distinct()
            if keyTitle != '':
                book_list = book_list.filter(title__icontains=keyTitle)
            if keyPub != '':
                book_list.filter(editorial__icontains=keyPub)
        if not 'want_book' in requestData:
            book_list = Book.objects.none()

        if 'want_bookChapter' in requestData:
            if program_id != 'Programa educativo' and academy_id != 'Cuerpo academico':
                tagCombo_list = (
                    Tag.objects.filter(
                        name=Program.objects.get(id=program_id))
                    | Tag.objects.filter(
                        name=Academy.objects.get(id=academy_id))).distinct()
                bookChapter_list = BookChapter.objects.filter(
                    tags__in=list(tagCombo_list)).distinct()
            elif program_id != 'Programa educativo' or academy_id != 'Cuerpo academico':
                if program_id != 'Programa educativo':
                    tagCombo_list = Tag.objects.filter(
                        name=Program.objects.get(id=program_id))
                    bookChapter_list = BookChapter.objects.filter(
                        tags__in=list(tagCombo_list)).distinct()
                if academy_id != 'Cuerpo academico':
                    tagCombo_list = Tag.objects.filter(
                        name=Academy.objects.get(id=academy_id))
                    bookChapter_list = BookChapter.objects.filter(
                        tags__in=list(tagCombo_list)).distinct()
            if keyword != '':
                bookChapter_list = (bookChapter_list.filter(title__icontains=keyword)
                                    | bookChapter_list.filter(bookEditorial__icontains=keyword)).distinct()
        if not 'want_bookChapter' in requestData:
            bookChapter_list = BookChapter.objects.none()

        if 'want_article' in requestData:
            if program_id != 'Programa educativo' and academy_id != 'Cuerpo academico':
                account_list = Account.objects.filter(
                    program=program_id).filter(academy=academy_id)
                article_list = Article.objects.filter(
                    authors__in=list(account_list)).distinct()
            elif program_id != 'Programa educativo' or academy_id != 'Cuerpo academico':
                if program_id != 'Programa educativo':
                    account_list = Account.objects.filter(program=program_id)
                    article_list = Article.objects.filter(
                        authors__in=list(account_list)).distinct()
                if academy_id != 'Cuerpo academico':
                    account_list = Account.objects.filter(academy=academy_id)
                    article_list = Article.objects.filter(
                        authors__in=list(account_list)).distinct()
            if keyword != '':
                article_list = (article_list.filter(user__account__firstName__icontains=keyword)
                                | article_list.filter(user__account__lastNameA__icontains=keyword)
                                | article_list.filter(user__account__lastNameB__icontains=keyword)
                                | article_list.filter(title__icontains=keyword)
                                | article_list.filter(editorial__icontains=keyword)).distinct()
        if not 'want_article' in requestData:
            article_list = Article.objects.none()
        product_list = list(chain(article_list, book_list, bookChapter_list))
        data = serializers.serialize('json', product_list)
    return JsonResponse(data, safe=False)


def tagsAjaxView(request):
    if request.is_ajax:
        tag_list = Tag.objects.all()
        data = serializers.serialize('json', tag_list)
    return JsonResponse(data, safe=False)
