"""
Use this file as your template file to write your program in. This is so you can access the dictionary
below to display information requested by the user.

Please fill in your names, lab group number, and date below. 
Make sure to read the marking guide to see how to get extra points!
"""

#####################################################################
""" 
                   ISC 2024 Beginner CS Lab                    
Group Number:                                                   
Group Members:                                                  
Date:                                                           
"""
#####################################################################

# Here is the nested dictionary of the tv shows to use in your information system
TV_Shows = {
    "Breaking Bad": {
        "Title": "Breaking Bad",
        "Genre": "Crime, Drama, Thriller",
        "Published Date": "January 20, 2008",
        "Brief Description": "A high school chemistry teacher turned methamphetamine manufacturer teams up with a former student.",
        "Number of Seasons": 5,
    },
    "Stranger Things": {
        "Title": "Stranger Things",
        "Genre": "Drama, Fantasy, Horror",
        "Published Date": "July 15, 2016",
        "Brief Description": "A group of kids in a small town uncover supernatural mysteries and government experiments.",
        "Number of Seasons": 4,
    },
    "The Mandalorian": {
        "Title": "The Mandalorian",
        "Genre": "Action, Adventure, Fantasy",
        "Published Date": "November 12, 2019",
        "Brief Description": "A lone bounty hunter navigates the outer reaches of the galaxy in the Star Wars universe.",
        "Number of Seasons": 2,
    },
    "The Office": {
        "Title": "The Office",
        "Genre": "Comedy",
        "Published Date": "March 24, 2005",
        "Brief Description": "A mockumentary-style sitcom that depicts the everyday work lives of office employees.",
        "Number of Seasons": 9,
    },
    "Black Mirror": {
        "Title": "Black Mirror",
        "Genre": "Drama, Sci-Fi, Thriller",
        "Published Date": "December 4, 2011",
        "Brief Description": "An anthology series exploring the dark and often dystopian aspects of modern society and technology.",
        "Number of Seasons": 5,
    },
    "Game of Thrones": {
        "Title": "Game of Thrones",
        "Genre": "Action, Adventure, Drama",
        "Published Date": "April 17, 2011",
        "Brief Description": 'A complex fantasy drama based on the "A Song of Ice and Fire" novels by George R.R. Martin.',
        "Number of Seasons": 8,
    },
    "The Simpsons": {
        "Title": "The Simpsons",
        "Genre": "Animation, Comedy",
        "Published Date": "December 17, 1989",
        "Brief Description": "A satirical depiction of a middle-class American family and their everyday lives.",
        "Number of Seasons": 33,
    },
    "Friends": {
        "Title": "Friends",
        "Genre": "Comedy, Romance",
        "Published Date": "September 22, 1994",
        "Brief Description": "Follows a group of friends living in New York City as they navigate through life, love, and work.",
        "Number of Seasons": 10,
    },
    "Naruto": {
        "Title": "Naruto",
        "Genre": "Animation, Action, Adventure",
        "Published Date": "October 3, 2002",
        "Brief Description": "Follows Naruto Uzumaki, a young ninja with dreams of becoming the strongest ninja and leader of his village.",
        "Number of Seasons": 5,
    },
    "The Crown": {
        "Title": "The Crown",
        "Genre": "Biography, Drama, History",
        "Published Date": "November 4, 2016",
        "Brief Description": "Chronicles the reign of Queen Elizabeth II and major events in British history.",
        "Number of Seasons": 5,
    },
    "SpongeBob SquarePants": {
        "Title": "SpongeBob SquarePants",
        "Genre": "Animation, Comedy, Family",
        "Published Date": "May 1, 1999",
        "Brief Description": "Follows the adventures of SpongeBob and his friends in the underwater city of Bikini Bottom.",
        "Number of Seasons": 13,
    },
    "The Witcher": {
        "Title": "The Witcher",
        "Genre": "Action, Adventure, Drama",
        "Published Date": "December 20, 2019",
        "Brief Description": "Follows Geralt of Rivia, a monster hunter, as he navigates a world filled with magic, political intrigue, and dangerous creatures.",
        "Number of Seasons": 2,
    },
    "Rick and Morty": {
        "Title": "Rick and Morty",
        "Genre": "Animation, Adventure, Comedy",
        "Published Date": "December 2, 2013",
        "Brief Description": "Follows the interdimensional adventures of an eccentric and alcoholic scientist, Rick, and his good-hearted but easily influenced grandson, Morty.",
        "Number of Seasons": 5,
    },
    "The Umbrella Academy": {
        "Title": "The Umbrella Academy",
        "Genre": "Action, Adventure, Comedy",
        "Published Date": "February 15, 2019",
        "Brief Description": "A dysfunctional family of adopted superhero siblings reunites to solve the mystery of their father's death and prevent an impending apocalypse.",
        "Number of Seasons": 3,
    },
    "Brooklyn Nine-Nine": {
        "Title": "Brooklyn Nine-Nine",
        "Genre": "Comedy, Crime",
        "Published Date": "September 17, 2013",
        "Brief Description": "Follows the detectives of the 99th precinct of the NYPD as they solve crimes and navigate office dynamics.",
        "Number of Seasons": 8,
    },
    "MasterChef": {
        "Title": "MasterChef",
        "Genre": "Reality, Cooking, Competition",
        "Published Date": "July 27, 2010",
        "Brief Description": "Amateur chefs compete in various cooking challenges to win the title of MasterChef.",
        "Number of Seasons": 11,
    },
    "Sherlock": {
        "Title": "Sherlock",
        "Genre": "Crime, Drama, Mystery",
        "Published Date": "July 25, 2010",
        "Brief Description": "Modern adaptation of Arthur Conan Doyle's classic detective stories, featuring Sherlock Holmes and Dr. John Watson.",
        "Number of Seasons": 4,
    },
    "Westworld": {
        "Title": "Westworld",
        "Genre": "Drama, Mystery, Sci-Fi",
        "Published Date": "October 2, 2016",
        "Brief Description": "An amusement park for rich guests, where the attractions are advanced android hosts that cater to every human desire.",
        "Number of Seasons": 4,
    },
    "Survivor": {
        "Title": "Survivor",
        "Genre": "Adventure, Game-Show, Reality",
        "Published Date": "May 31, 2000",
        "Brief Description": "Contestants are stranded in a remote location and must work together and strategize to outwit, outplay, and outlast each other to win a cash prize.",
        "Number of Seasons": 41,
    },
    "Survivor": {
        "Title": "Survivor",
        "Genre": "Adventure, Game-Show, Reality",
        "Published Date": "May 31, 2000",
        "Brief Description": "Contestants are stranded in a remote location and must work together and strategize to outwit, outplay, and outlast each other to win a cash prize.",
        "Number of Seasons": 41,
    },
}

# Here are the genres to use for Part 2
genre_list = [
    "Adventure",
    "Game-Show",
    "Reality",
    "Drama",
    "Mystery",
    "Sci-Fi",
    "Crime",
    "Reality",
    "Cooking",
    "Competition",
    "Comedy",
    "Action",
    "Animation",
    "Family",
    "Biography",
    "History",
    "Romance",
    "Thriller",
    "Fantasy",
    "Horror",
]
