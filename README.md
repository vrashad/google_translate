# Google Translate vasitəsilə sənədlərin tərcümə edilməsi

Bu kiçik bir script vasitəsilə, txt formatında olan sənədləri bir dildən başqa dilə tərcümə etmək mümkündür

Google Translate limitlərini nəzərə alaraq, sənədlər ən çoxu 4000 simvollara bölünərək tərcümə edilir hissə-hissə, sonra bir yerə yığılaraq eyni adda digər qovluğa fayl olaraq yerləşdirilir

Sənədlər qabaqcadan normallaşdırılmalıdır

Hər sətir növbəti sətrə keçid simqolu ilə bitməldir `\n`

Bu sənədin məntiqi olaraq hissələrə bölünməyini və daha dəqiq tərcümə edilməyini təmin edir

`input_directory` veriləninə, tərcümə edilməli olan sənədlərin yerləşdiyi qoyluğun tam ünvanını dəyər olaraq təyin etmək lazımdır

`output_directory` veriləninə isə tərcümə olunmuş sənədlərin yerləşdiriləcəyi qoyluğun tam ünvanını dəyər olaraq təyin etmək lazımdır

`source_language = 'az'` sənədlərin hansı dildə olduğunu bildirir

`destination_language = 'en'` sənədləri hansı dilə tərcümə etmək lazım olduğunu bildirir
