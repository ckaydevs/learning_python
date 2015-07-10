import media
import fresh_tomatoes

dil_chahta_hai= media.Movie("Dil Chahta Hai",
                            "Three inseparable childhood friends are just out of college. Nothing comes between them - until they each fall in love, and their wildly different approaches to relationships creates tension.",
                            "http://cdn.koimoi.com/wp-content/new-galleries/2012/08/Dil-Chahta-Hai-Movie-Poster.jpg",
                            "https://www.youtube.com/watch?v=m13b25V0B10")

the_shawshank_redemption=media.Movie("The Shawshank Redemption",
                                     "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                     "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg",
                                     "https://www.youtube.com/watch?v=NmzuHjWmXOc")

#print(the_shawshank_redemption.storyline)
#dil_chahta_hai.show_trailer()
gladiator=media.Movie("Gladiator",
                      "When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
                      "http://ia.media-imdb.com/images/M/MV5BMTgwMzQzNTQ1Ml5BMl5BanBnXkFtZTgwMDY2NTYxMTE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                      "https://www.youtube.com/watch?v=owK1qxDselE")

znmd=media.Movie("Zindagi Na Milegi Dobara",
                 "Three friends decide to turn their fantasy vacation into reality after one of their number becomes engaged.",
                 "http://ia.media-imdb.com/images/M/MV5BMzQzMTA4ODY4OF5BMl5BanBnXkFtZTcwNjgyMDQxNw@@._V1_SY317_CR2,0,214,317_AL_.jpg",
                 "https://www.youtube.com/watch?v=2JU9KmHNPkk")

taare_zameen_par=media.Movie("Taare Zameen Par",
                             "An eight year old boy is thought to be lazy and a troublemaker, until the new art teacher has the patience and compassion to discover the real problem behind his struggles in school.",
                             "http://ia.media-imdb.com/images/M/MV5BMTU4NzYwNjYzNV5BMl5BanBnXkFtZTcwNjE4MjA3Mg@@._V1_SY317_CR4,0,214,317_AL_.jpg",
                             "https://www.youtube.com/watch?v=q9o6smDsoOE")


the_pursuit_of_happyness=media.Movie("The Pursuit of Happyness",
                                     "A struggling salesman takes custody of his son as he's poised to begin a life-changing professional endeavor.",
                                     "http://ia.media-imdb.com/images/M/MV5BMTQ5NjQ0NDI3NF5BMl5BanBnXkFtZTcwNDI0MjEzMw@@._V1_SX214_AL_.jpg",
                                     "https://www.youtube.com/watch?v=89Kq8SDyvfg")
movies = [taare_zameen_par,dil_chahta_hai,the_shawshank_redemption, gladiator, znmd,  the_pursuit_of_happyness]
fresh_tomatoes.open_movies_page(movies)
"""checking out the predefined class variables"""
#print(media.Movie.__doc__)#gives documentation related to class
#print(media.Movie.__name__)#gives name of the class
#print(media.Movie.__module__)#gives name of the module containing the class


