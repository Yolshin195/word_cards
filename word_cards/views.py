from django.shortcuts import render, redirect, get_object_or_404

from .forms import WordCardForm, WordCardFilterForm
from .models import WordCard
from .services import parse_word


def index(request):
    filter_form = WordCardFilterForm(request.GET)
    front = filter_form.data.get('front', None)
    if front:
        ward_cards = WordCard.objects.filter(front__icontains=front)
    else:
        ward_cards = WordCard.objects.all()
    context = {
        "filter_form": filter_form,
        "word_cards": ward_cards
    }
    return render(request, "word_cards/index.html", context)


def update(request, pk=None):
    if pk:
        word_card = get_object_or_404(WordCard, pk=pk)
        form = WordCardForm(request.POST or None, instance=word_card)
    else:
        form = WordCardForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('word_card_detail', pk=form.instance.id)

    context = {
        "form": form
    }
    return render(request, "word_cards/update.html", context)


def detail(request, pk=None):
    word_card = get_object_or_404(WordCard, pk=pk)
    context = {
        "word_card": word_card
    }
    return render(request, "word_cards/detail.html", context)


def delete(request, pk=None):
    context = {

    }
    return render(request, "word_cards/delete.html", context)


def translate(request, pk=None):
    word_card = get_object_or_404(WordCard, pk=pk)
    parse_result = parse_word(word=word_card.front)
    word_card.back = parse_result.translate
    word_card.save()
    return redirect('word_card_detail', pk=word_card.id)
