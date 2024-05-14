PyTest'te Dekoratörler Hakkında Notlar

Giriş:

PyTest, test kodunuzu organize etmenize ve yürütmenize yardımcı olan popüler bir Python kütüphanesidir.
Dekoratörler, PyTest'te testlerinizi tanımlamak ve özelleştirmek için güçlü bir araçtır.
Bu belge, PyTest'teki yaygın dekoratörleri ve kullanımlarını kapsamaktadır.

PyTest, Python'daki testlerin otomatik çalıştırılmasını sağlayan bir test çerçevesidir.
Decoratorler, test işlevlerine ek özellikler eklemek için kullanılır.

Temel Dekoratörler:

@pytest.mark.parametrize: Farklı argüman değerleri ile bir testi birden çok kez çalıştırmanızı sağlar.
@pytest.fixture: Testlerinize tekrar kullanılabilir veri ve nesneler sağlayan bir fonksiyon tanımlar.
@pytest.skip: Belirli bir testi atlamanızı sağlar.
@pytest.xfail: Bir testin beklenen şekilde başarısız olmasını bekler ve bu durumda başarısızlığı atlar.
Gelişmiş Dekoratörler:

@pytest.hookimpl: PyTest'in test yürütme kancasına özel kod eklemenizi sağlar.
@pytest.fixture_scope: Bir fikstürün kapsamını (örneğin, 'fonksiyon', 'modül') belirlemenizi sağlar.
@pytest.mark.usefixtures: Bir teste bir veya birden fazla fikstür uygulamanızı sağlar.
@pytest.raises: Bir testin belirli bir istisna türünü yükseltmesini bekler.
Dekoratör Örnekleri:

1. Parametrize Edilmiş Testler:

Python
@pytest.mark.parametrize("x,y", [(1,2), (3,4)])
def test_sum(x, y):
    assert x + y == sum(x, y)
Use code with caution.



2. Fikstürler:

Python
@pytest.fixture
def setup_db():
    # Veritabanı bağlantısını kurun ve test verilerini ayarlayın
    pass

def test_user_login(setup_db):
    # Kullanıcı giriş testini gerçekleştirin
    pass
Use code with caution.



3. Testleri Atlamak:

Python
@pytest.mark.skip("Bu test henüz tamamlanmadı")
def test_advanced_feature():
    # Gelişmiş özelliği test edin
    pass
Use code with caution.



4. Beklenen Başarısız Testler:

Python
@pytest.mark.xfail(raises=ValueError)
def test_invalid_input():
    # Hatalı girdi ile bir işlevi çağırın ve ValueError hatası almasını bekleyin
    pass
Use code with caution.


5. Test Kancaları:

Python
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    # Her test çalıştırıldığında özel kod çalıştırın
    yield
Use code with caution.



Notlar:

Bu belge PyTest'teki tüm dekoratörleri kapsamaz.
Dekoratörler hakkında daha fazla bilgi için PyTest belgelerine başvurun: https://docs.pytest.org/en/7.1.x/contents.html
Dekoratörleri sorumlu bir şekilde kullanın ve test kodunuzu karmaşıklaştırmaktan kaçının.

Sonuç:

PyTest'teki dekoratörler, test kodunuzu daha organize, okunabilir ve bakımı kolay hale getirebilir.
Bu notlar, PyTest'te dekoratörlerin temellerini anlamanıza ve testlerinizi daha etkili bir şekilde yazmanıza yardımcı olacaktır.
