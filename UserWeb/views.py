from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    cards = [
        {
            'image_url': 'UserWeb/assets/cssper.png',
            'alt_text': 'kategori Kelas',
            'title': 'Pengenalan CSS Dasar',
            'materi_count': 24,
            'rating': 4.6,
            'review_count': 6,
            'price': 'Gratis'
        },
         {
            'image_url': 'UserWeb/assets/cssper.png',
            'alt_text': 'kategori Kelas',
            'title': 'Pengenalan CSS Dasar',
            'materi_count': 24,
            'rating': 4.6,
            'review_count': 6,
            'price': 'Gratis'
        },
          {
            'image_url': 'UserWeb/assets/cssper.png',
            'alt_text': 'kategori Kelas',
            'title': 'Pengenalan CSS Dasar',
            'materi_count': 24,
            'rating': 4.6,
            'review_count': 6,
            'price': 'Gratis'
        },
           {
            'image_url': 'UserWeb/assets/cssper.png',
            'alt_text': 'kategori Kelas',
            'title': 'Pengenalan CSS Dasar',
            'materi_count': 24,
            'rating': 4.6,
            'review_count': 6,
            'price': 'Gratis'
        },
            {
            'image_url': 'UserWeb/assets/cssper.png',
            'alt_text': 'kategori Kelas',
            'title': 'Pengenalan CSS Dasar',
            'materi_count': 24,
            'rating': 4.6,
            'review_count': 6,
            'price': 'Gratis'
        },
     
    ]
    
    context = {
        'title': 'Dashboard',
        'LokStyle' : 'UserWeb/css/style.css',
        'Scripts' : 'UserWeb/js/index.js',
        'cards': cards  
    }
    
    return render(request, 'UserWeb/dashboard_user.html', context)

def about(request):
    context = {
        'title': 'About',
        'LokStyle' : 'UserWeb/css/about.css',
        'Scripts' : 'UserWeb/js/about.js',
    }
    
    return render(request, 'UserWeb/about.html', context)
@login_required
def kategoriBack(request):
    gambarCards = [
        {
            'gambar' : 'UserWeb/assets/pengback.png',
            'judul' : 'Pengenalan Back-End',
            'jumlahMateri' : '3 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },
        {
            'gambar' : 'UserWeb/assets/node.png',
            'judul' : 'Pengenalan Node.js',
            'jumlahMateri' : '4 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },
        {
            'gambar' : 'UserWeb/assets/php.png',
            'judul' : 'Pengenalan PHP untuk Back-End',
            'jumlahMateri' : '4 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },
        {
            'gambar' : 'UserWeb/assets/pengsql.png',
            'judul' : 'Pengenalan SQL',
            'jumlahMateri' : '6 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },
        {
            'gambar' : 'UserWeb/assets/mysql.png',
            'judul' : 'Pengenalan MySQL',
            'jumlahMateri' : '3 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },
          {
            'gambar' : 'UserWeb/assets/crud.png',
            'judul' : 'Manipulasi Data SQL (CRUD)',
            'jumlahMateri' : '3 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },
    ]
    context = {
        'title': 'Kategori Back End',
        'LokStyle': 'UserWeb/css/style.css',
        'Scripts': 'UserWeb/js/kategori.js',
        'gambarCards': gambarCards
    }

    return render(request, 'UserWeb/kategori/kategori_back.html', context)
@login_required
def kategoriFront(request):
    gambarCardsFront = [
        {
            'gambar' : 'UserWeb/assets/htmlper.png',
            'judul' : 'Pengenalan Dasar HTML',
            'jumlahMateri' : '3 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },
        {
            'gambar' : 'UserWeb/assets/cssper.png',
            'judul' : 'Pengenalan CSS Dasar',
            'jumlahMateri' : '4 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },
        {
            'gambar' : 'UserWeb/assets/cssper.png',
            'judul' : 'Flexbox dan Grid Layout',
            'jumlahMateri' : '5 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },
        {
            'gambar' : 'UserWeb/assets/bootstrap.png',
            'judul' : 'Responsive Web Design',
            'jumlahMateri' : '6 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },
        {
            'gambar' : 'UserWeb/assets/js.png',
            'judul' : 'JavaScript untuk Front-End',
            'jumlahMateri' : '3 Materi',
            'ulasan' : '4.6 (6 Ulasan)' 
        },

    ]
    context = {
        'title' : 'Kategori Front End',
        'LokStyle' : 'UserWeb/css/style.css',
        'Scripts' : 'UserWeb/js/kategori.js',
        'gambarCardsF' : gambarCardsFront
    }
    return render(request, 'UserWeb/kategori/kategori_front.html', context)
    
