from django.test import TestCase, override_settings
from django.core.exceptions import FieldDoesNotExist
from django.utils.translation import activate

from sample.models import Continent

from tests.sample import create_samples


class TranslatableQuerySetTest(TestCase):
    """Tests for `TranslatableQuerySet`."""

    @override_settings(LANGUAGE_CODE='de')
    def test_apply_translations_level_0_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        continents = Continent.objects.all()
        continents.apply_translations()
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Germany'
        )
        self.assertEqual(
            germany.denonym,
            'German'
        )
        self.assertEqual(
            cologne.name,
            'Cologne'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korean'
        )
        self.assertEqual(
            seoul.name,
            'Seoul'
        )
        self.assertEqual(
            seoul.denonym,
            'Seouler'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_apply_translations_level_1_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1 = ('countries',)

        continents = Continent.objects.all()
        continents.apply_translations(*lvl_1)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Cologne'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seoul'
        )
        self.assertEqual(
            seoul.denonym,
            'Seouler'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_apply_translations_level_2_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_2 = ('countries__cities',)

        continents = Continent.objects.all()
        continents.apply_translations(*lvl_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Germany'
        )
        self.assertEqual(
            germany.denonym,
            'German'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korean'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_apply_translations_level_1_2_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.all()
        continents.apply_translations(*lvl_1_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    def test_apply_translations_level_0_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        continents = Continent.objects.all()
        continents.apply_translations(lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Germany'
        )
        self.assertEqual(
            germany.denonym,
            'German'
        )
        self.assertEqual(
            cologne.name,
            'Cologne'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korean'
        )
        self.assertEqual(
            seoul.name,
            'Seoul'
        )
        self.assertEqual(
            seoul.denonym,
            'Seouler'
        )

    def test_apply_translations_level_1_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1 = ('countries',)

        continents = Continent.objects.all()
        continents.apply_translations(*lvl_1, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Cologne'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seoul'
        )
        self.assertEqual(
            seoul.denonym,
            'Seouler'
        )

    def test_apply_translations_level_2_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_2 = ('countries__cities',)

        continents = Continent.objects.all()
        continents.apply_translations(*lvl_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Germany'
        )
        self.assertEqual(
            germany.denonym,
            'German'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korean'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    def test_apply_translations_level_1_2_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.all()
        continents.apply_translations(*lvl_1_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_apply_translations_prefetched_level_0_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations()
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Germany'
        )
        self.assertEqual(
            germany.denonym,
            'German'
        )
        self.assertEqual(
            cologne.name,
            'Cologne'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korean'
        )
        self.assertEqual(
            seoul.name,
            'Seoul'
        )
        self.assertEqual(
            seoul.denonym,
            'Seouler'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_apply_translations_prefetched_level_1_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1 = ('countries',)
        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Cologne'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seoul'
        )
        self.assertEqual(
            seoul.denonym,
            'Seouler'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_apply_translations_prefetched_level_2_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_2 = ('countries__cities',)
        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Germany'
        )
        self.assertEqual(
            germany.denonym,
            'German'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korean'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_apply_translations_prefetched_level_1_2_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    def test_apply_translations_prefetched_level_0_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Germany'
        )
        self.assertEqual(
            germany.denonym,
            'German'
        )
        self.assertEqual(
            cologne.name,
            'Cologne'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korean'
        )
        self.assertEqual(
            seoul.name,
            'Seoul'
        )
        self.assertEqual(
            seoul.denonym,
            'Seouler'
        )

    def test_apply_translations_prefetched_level_1_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1 = ('countries',)
        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Cologne'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seoul'
        )
        self.assertEqual(
            seoul.denonym,
            'Seouler'
        )

    def test_apply_translations_prefetched_level_2_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_2 = ('countries__cities',)
        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Germany'
        )
        self.assertEqual(
            germany.denonym,
            'German'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korean'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    def test_apply_translations_prefetched_level_1_2_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europa'
        )
        self.assertEqual(
            europe.denonym,
            'Europäisch'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asien'
        )
        self.assertEqual(
            asia.denonym,
            'Asiatisch'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    def test_apply_translations_invalid_simple_relation(self):
        create_samples(
            continent_names=['europe'],
            continent_fields=['name', 'denonym'],
            langs=['de']
        )

        continents = Continent.objects.all()

        with self.assertRaises(FieldDoesNotExist) as error:
            continents.apply_translations('wrong')

        self.assertEqual(
            error.exception.args[0],
            "Continent has no field named 'wrong'"
        )

    def test_apply_translations_invalid_nested_relation(self):
        create_samples(
            continent_names=['europe'],
            country_names=['germany'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            langs=['de']
        )

        continents = Continent.objects.all()

        with self.assertRaises(FieldDoesNotExist) as error:
            continents.apply_translations('countries__wrong')

        self.assertEqual(
            error.exception.args[0],
            "Country has no field named 'wrong'"
        )

    def test_apply_translations_invalid_lang(self):
        create_samples(
            continent_names=['europe'],
            continent_fields=['name', 'denonym'],
            langs=['de']
        )

        continents = Continent.objects.all()

        with self.assertRaises(ValueError) as error:
            continents.apply_translations(lang='xx')

        self.assertEqual(
            error.exception.args[0],
            'The language code `xx` is not supported.'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_update_translations_level_0_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        # change
        europe.name = 'Europe Name'
        europe.denonym = 'Europe Denonym'
        germany.name = 'Germany Name'
        germany.denonym = 'Germany Denonym'
        cologne.name = 'Cologne Name'
        cologne.denonym = 'Cologne Denonym'
        asia.name = 'Asia Name'
        asia.denonym = 'Asia Denonym'
        south_korea.name = 'South Korea Name'
        south_korea.denonym = 'South Korea Denonym'
        seoul.name = 'Seoul Name'
        seoul.denonym = 'Seoul Denonym'
        continents.update_translations()

        # reapply
        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europe Name'
        )
        self.assertEqual(
            europe.denonym,
            'Europe Denonym'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asia Name'
        )
        self.assertEqual(
            asia.denonym,
            'Asia Denonym'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_update_translations_level_1_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1 = ('countries',)
        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        # change
        europe.name = 'Europe Name'
        europe.denonym = 'Europe Denonym'
        germany.name = 'Germany Name'
        germany.denonym = 'Germany Denonym'
        cologne.name = 'Cologne Name'
        cologne.denonym = 'Cologne Denonym'
        asia.name = 'Asia Name'
        asia.denonym = 'Asia Denonym'
        south_korea.name = 'South Korea Name'
        south_korea.denonym = 'South Korea Denonym'
        seoul.name = 'Seoul Name'
        seoul.denonym = 'Seoul Denonym'
        continents.update_translations(*lvl_1)

        # reapply
        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europe Name'
        )
        self.assertEqual(
            europe.denonym,
            'Europe Denonym'
        )
        self.assertEqual(
            germany.name,
            'Germany Name'
        )
        self.assertEqual(
            germany.denonym,
            'Germany Denonym'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asia Name'
        )
        self.assertEqual(
            asia.denonym,
            'Asia Denonym'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea Name'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korea Denonym'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_update_translations_level_2_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_2 = ('countries__cities',)
        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        # change
        europe.name = 'Europe Name'
        europe.denonym = 'Europe Denonym'
        germany.name = 'Germany Name'
        germany.denonym = 'Germany Denonym'
        cologne.name = 'Cologne Name'
        cologne.denonym = 'Cologne Denonym'
        asia.name = 'Asia Name'
        asia.denonym = 'Asia Denonym'
        south_korea.name = 'South Korea Name'
        south_korea.denonym = 'South Korea Denonym'
        seoul.name = 'Seoul Name'
        seoul.denonym = 'Seoul Denonym'
        continents.update_translations(*lvl_2)

        # reapply
        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europe Name'
        )
        self.assertEqual(
            europe.denonym,
            'Europe Denonym'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Cologne Name'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologne Denonym'
        )
        self.assertEqual(
            asia.name,
            'Asia Name'
        )
        self.assertEqual(
            asia.denonym,
            'Asia Denonym'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seoul Name'
        )
        self.assertEqual(
            seoul.denonym,
            'Seoul Denonym'
        )

    @override_settings(LANGUAGE_CODE='de')
    def test_update_translations_level_1_2_relation_no_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        # change
        europe.name = 'Europe Name'
        europe.denonym = 'Europe Denonym'
        germany.name = 'Germany Name'
        germany.denonym = 'Germany Denonym'
        cologne.name = 'Cologne Name'
        cologne.denonym = 'Cologne Denonym'
        asia.name = 'Asia Name'
        asia.denonym = 'Asia Denonym'
        south_korea.name = 'South Korea Name'
        south_korea.denonym = 'South Korea Denonym'
        seoul.name = 'Seoul Name'
        seoul.denonym = 'Seoul Denonym'
        continents.update_translations(*lvl_1_2)

        # reapply
        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2)
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europe Name'
        )
        self.assertEqual(
            europe.denonym,
            'Europe Denonym'
        )
        self.assertEqual(
            germany.name,
            'Germany Name'
        )
        self.assertEqual(
            germany.denonym,
            'Germany Denonym'
        )
        self.assertEqual(
            cologne.name,
            'Cologne Name'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologne Denonym'
        )
        self.assertEqual(
            asia.name,
            'Asia Name'
        )
        self.assertEqual(
            asia.denonym,
            'Asia Denonym'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea Name'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korea Denonym'
        )
        self.assertEqual(
            seoul.name,
            'Seoul Name'
        )
        self.assertEqual(
            seoul.denonym,
            'Seoul Denonym'
        )

    def test_update_translations_level_0_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        # change
        europe.name = 'Europe Name'
        europe.denonym = 'Europe Denonym'
        germany.name = 'Germany Name'
        germany.denonym = 'Germany Denonym'
        cologne.name = 'Cologne Name'
        cologne.denonym = 'Cologne Denonym'
        asia.name = 'Asia Name'
        asia.denonym = 'Asia Denonym'
        south_korea.name = 'South Korea Name'
        south_korea.denonym = 'South Korea Denonym'
        seoul.name = 'Seoul Name'
        seoul.denonym = 'Seoul Denonym'
        continents.update_translations(lang='de')

        # reapply
        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europe Name'
        )
        self.assertEqual(
            europe.denonym,
            'Europe Denonym'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asia Name'
        )
        self.assertEqual(
            asia.denonym,
            'Asia Denonym'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    def test_update_translations_level_1_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1 = ('countries',)
        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        # change
        europe.name = 'Europe Name'
        europe.denonym = 'Europe Denonym'
        germany.name = 'Germany Name'
        germany.denonym = 'Germany Denonym'
        cologne.name = 'Cologne Name'
        cologne.denonym = 'Cologne Denonym'
        asia.name = 'Asia Name'
        asia.denonym = 'Asia Denonym'
        south_korea.name = 'South Korea Name'
        south_korea.denonym = 'South Korea Denonym'
        seoul.name = 'Seoul Name'
        seoul.denonym = 'Seoul Denonym'
        continents.update_translations(*lvl_1, lang='de')

        # reapply
        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europe Name'
        )
        self.assertEqual(
            europe.denonym,
            'Europe Denonym'
        )
        self.assertEqual(
            germany.name,
            'Germany Name'
        )
        self.assertEqual(
            germany.denonym,
            'Germany Denonym'
        )
        self.assertEqual(
            cologne.name,
            'Köln'
        )
        self.assertEqual(
            cologne.denonym,
            'Kölner'
        )
        self.assertEqual(
            asia.name,
            'Asia Name'
        )
        self.assertEqual(
            asia.denonym,
            'Asia Denonym'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea Name'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korea Denonym'
        )
        self.assertEqual(
            seoul.name,
            'Seül'
        )
        self.assertEqual(
            seoul.denonym,
            'Seüler'
        )

    def test_update_translations_level_2_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_2 = ('countries__cities',)
        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        # change
        europe.name = 'Europe Name'
        europe.denonym = 'Europe Denonym'
        germany.name = 'Germany Name'
        germany.denonym = 'Germany Denonym'
        cologne.name = 'Cologne Name'
        cologne.denonym = 'Cologne Denonym'
        asia.name = 'Asia Name'
        asia.denonym = 'Asia Denonym'
        south_korea.name = 'South Korea Name'
        south_korea.denonym = 'South Korea Denonym'
        seoul.name = 'Seoul Name'
        seoul.denonym = 'Seoul Denonym'
        continents.update_translations(*lvl_2, lang='de')

        # reapply
        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europe Name'
        )
        self.assertEqual(
            europe.denonym,
            'Europe Denonym'
        )
        self.assertEqual(
            germany.name,
            'Deutschland'
        )
        self.assertEqual(
            germany.denonym,
            'Deutsche'
        )
        self.assertEqual(
            cologne.name,
            'Cologne Name'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologne Denonym'
        )
        self.assertEqual(
            asia.name,
            'Asia Name'
        )
        self.assertEqual(
            asia.denonym,
            'Asia Denonym'
        )
        self.assertEqual(
            south_korea.name,
            'Südkorea'
        )
        self.assertEqual(
            south_korea.denonym,
            'Südkoreanisch'
        )
        self.assertEqual(
            seoul.name,
            'Seoul Name'
        )
        self.assertEqual(
            seoul.denonym,
            'Seoul Denonym'
        )

    def test_update_translations_level_1_2_relation_with_lang(self):
        create_samples(
            continent_names=['europe', 'asia'],
            country_names=['germany', 'south korea'],
            city_names=['cologne', 'seoul'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de', 'tr']
        )

        lvl_1_2 = ('countries', 'countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        # change
        europe.name = 'Europe Name'
        europe.denonym = 'Europe Denonym'
        germany.name = 'Germany Name'
        germany.denonym = 'Germany Denonym'
        cologne.name = 'Cologne Name'
        cologne.denonym = 'Cologne Denonym'
        asia.name = 'Asia Name'
        asia.denonym = 'Asia Denonym'
        south_korea.name = 'South Korea Name'
        south_korea.denonym = 'South Korea Denonym'
        seoul.name = 'Seoul Name'
        seoul.denonym = 'Seoul Denonym'
        continents.update_translations(*lvl_1_2, lang='de')

        # reapply
        continents = Continent.objects.prefetch_related(*lvl_1_2)
        continents.apply_translations(*lvl_1_2, lang='de')
        europe = [x for x in continents if x.code == 'EU'][0]
        germany = europe.countries.all()[0]
        cologne = germany.cities.all()[0]
        asia = [x for x in continents if x.code == 'AS'][0]
        south_korea = asia.countries.all()[0]
        seoul = south_korea.cities.all()[0]

        self.assertEqual(
            europe.name,
            'Europe Name'
        )
        self.assertEqual(
            europe.denonym,
            'Europe Denonym'
        )
        self.assertEqual(
            germany.name,
            'Germany Name'
        )
        self.assertEqual(
            germany.denonym,
            'Germany Denonym'
        )
        self.assertEqual(
            cologne.name,
            'Cologne Name'
        )
        self.assertEqual(
            cologne.denonym,
            'Cologne Denonym'
        )
        self.assertEqual(
            asia.name,
            'Asia Name'
        )
        self.assertEqual(
            asia.denonym,
            'Asia Denonym'
        )
        self.assertEqual(
            south_korea.name,
            'South Korea Name'
        )
        self.assertEqual(
            south_korea.denonym,
            'South Korea Denonym'
        )
        self.assertEqual(
            seoul.name,
            'Seoul Name'
        )
        self.assertEqual(
            seoul.denonym,
            'Seoul Denonym'
        )

    def test_update_translations_invalid_simple_relation(self):
        create_samples(
            continent_names=['europe'],
            continent_fields=['name', 'denonym'],
            langs=['de']
        )

        continents = Continent.objects.all()

        with self.assertRaises(FieldDoesNotExist) as error:
            continents.update_translations('wrong')

        self.assertEqual(
            error.exception.args[0],
            "Continent has no field named 'wrong'"
        )

    def test_update_translations_invalid_nested_relation(self):
        create_samples(
            continent_names=['europe'],
            country_names=['germany'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            langs=['de']
        )

        lvl_1 = ('countries',)

        continents = Continent.objects.prefetch_related(*lvl_1)

        with self.assertRaises(FieldDoesNotExist) as error:
            continents.update_translations('countries__wrong')

        self.assertEqual(
            error.exception.args[0],
            "Country has no field named 'wrong'"
        )

    def test_update_translations_invalid_lang(self):
        create_samples(
            continent_names=['europe'],
            continent_fields=['name', 'denonym'],
            langs=['de']
        )

        continents = Continent.objects.all()

        with self.assertRaises(ValueError) as error:
            continents.update_translations(lang='xx')

        self.assertEqual(
            error.exception.args[0],
            'The language code `xx` is not supported.'
        )

    def test_update_translations_invalid_prefetch_simple_relation(self):
        create_samples(
            continent_names=['europe'],
            country_names=['germany'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            langs=['de']
        )

        lvl_1 = ('countries',)

        continents = Continent.objects.all()

        with self.assertRaises(RuntimeError) as error:
            continents.update_translations(*lvl_1)

        self.assertEqual(
            error.exception.args[0],
            ('The relation `countries` of the model `Continent` must' +
             ' be prefetched.')
        )

    def test_update_translations_invalid_prefetch_nested_relation(self):
        create_samples(
            continent_names=['europe'],
            country_names=['germany'],
            city_names=['cologne'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de']
        )

        lvl_2 = ('countries__cities',)

        continents = Continent.objects.all()

        with self.assertRaises(RuntimeError) as error:
            continents.update_translations(*lvl_2)

        self.assertEqual(
            error.exception.args[0],
            ('The relation `countries` of the model `Continent` must' +
             ' be prefetched.')
        )

    def test_update_translations_invalid_prefetch_part_nested_relation(self):
        create_samples(
            continent_names=['europe'],
            country_names=['germany'],
            city_names=['cologne'],
            continent_fields=['name', 'denonym'],
            country_fields=['name', 'denonym'],
            city_fields=['name', 'denonym'],
            langs=['de']
        )

        lvl_1 = ('countries',)
        lvl_2 = ('countries__cities',)

        continents = Continent.objects.prefetch_related(*lvl_1)

        with self.assertRaises(RuntimeError) as error:
            continents.update_translations(*lvl_2)

        self.assertEqual(
            error.exception.args[0],
            ('The relation `cities` of the model `Country` must' +
             ' be prefetched.')
        )