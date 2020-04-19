# Software-Testing

## Užduotys 1 - 3.1 jau atsiskaitytos

## Užduotis 3.2 unittest su dviem registracijos formomis

Kodas faile "practice3-2.py".

Pradžioje parašomi 2 link kintamojo variantai, pirmai ir antrai registracijos formai.
Norint pasirinkti su kuria forma testuojamas kodas reikia užkomentuoti kitą varinatą.

```python

#link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

```

"setUp" funkcijoje surenkami registracijos formos laukai, tada testavimo funkcijoje "test_form" naudojamas "assertEqual" metodas,
kad patikrinti ar pirmajame formos "div" elemente yra 3 laukai (galima ir kitaip tikrinti ar naudojama teisinga forma, bet tai yra
vienas iš veikiančių metodų). Jei klaidos nerandama užpildomi formos laukai ir paspaudžiamas "submit" mygtukas,
jei randama klaida einama testas baigiamas ir gaunama klaida - "Missing or too many fields".

Galiausiai "tearDown" metodas po 2 sekundžių uždaro naršyklės langą.

```python
class TestForm(unittest.TestCase):

    def setUp(self):
        self.browser = wd.Chrome()
        self.browser.get(link)

        self.div1 = self.browser.find_element_by_class_name("first_block")
        self.input1 = self.div1.find_elements_by_class_name("form-control")

        self.div2 = self.browser.find_element_by_class_name("second_block")
        self.input2 = self.div2.find_elements_by_class_name("form-control")
        self.button = self.browser.find_element_by_class_name("btn-default")

    def test_form(self):
        self.assertEqual(len(self.input1), 3, msg="Missing or too many fields")
        self.input1[0].send_keys("Vardenis")
        self.input1[1].send_keys("Paverdenis")
        self.input1[2].send_keys("VardPav@RealMail.net")
        self.input2[0].send_keys("123546789")
        self.input2[1].send_keys("adress st. 1-23")
        self.button.click()

    def tearDown(self):
        time.sleep(2)
        self.browser.quit()
```

Rezultatai su http://suninjuly.github.io/registration1.html:

image here later

Rezultatai su http://suninjuly.github.io/registration2.html:

image here later


## Užduotis 4
Kodas aplanko "practice4" faile "test_form.py".

Kitaip nei praeitoje užduotyje nuorodos kintamieji išrašomi be komentavimo, nes šį kartą bus atliekami abu testai vienu metu.

```python

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

```

iš pradžių naudojamas @pytest.fixture metodas kad gauti "browser" kintamajį, tada atveriama klasė "TestForm()" su funkcijomis:
* "collect_fields" - surenka registracijos formos įvedimo laukų ir mygtuko html elementus naudojant browse fixture.
* "send_keys" - užpildo laukus registracijos formoje, išrašyta funkcijoje, kad nereikėtų kartoti kodo.
* "test_correct_form" - atliekamas testas su forma kuri turėtų veikti.
* "test_incorrect_form" - atliekamas testas su forma kuri turėtų neveikti.

```python
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test")
    browser = wd.Chrome()
    yield browser
    print("\nquit browser")
    time.sleep(2)
    browser.quit()

class TestForm():
    def collect_fields(self, browser, link):
        browser.get(link)
        self.div1 = browser.find_element_by_class_name("first_block")
        self.input1 = self.div1.find_elements_by_class_name("form-control")

        self.div2 = browser.find_element_by_class_name("second_block")
        self.input2 = self.div2.find_elements_by_class_name("form-control")
        self.button = browser.find_element_by_class_name("btn-default")
    
    def send_keys(self):
        self.input1[0].send_keys("Vardenis")
        self.input1[1].send_keys("Paverdenis")
        self.input1[2].send_keys("VardPav@RealMail.net")
        self.input2[0].send_keys("123546789")
        self.input2[1].send_keys("adress st. 1-23")
        self.button.click()

    def test_correct_form(self, browser):
        print("start test with correct link")
        self.collect_fields(browser, link1)

        assert len(self.input1) == 3, "Missing or too many fields"
        self.send_keys()
    
    def test_incorrect_form(self, browser):
        print("start test with incorrect link")
        self.collect_fields(browser, link2)

        assert len(self.input1) == 3, "Missing or too many fields"
        self.send_keys()
```

Rezultatai:

image here later


## Užduotis 5 - kolkas tokia pati kaip ir užduotis 4
