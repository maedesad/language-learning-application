from backend.user.user_database import UserDatabase   # Importing the User class

from backend.user.user_class import User   # Importing the User class

from backend.practices.practices_classes.practice_topic_generating_context.reading_practice_topic_generator import ReadingPracticeTopicGenerator
from backend.practices.practices_topic_generating.pass_entries_to_topic_generatorfunction import pass_entries_to_topic_generator
from backend.practices.practices_topic_generating.practices_context_descriptions import passive_context_data_descriptions
from backend.practices.practices_topic_generating.practices_type_descriptions import reading_practice_description

user1 = User(
        username="Ali",
        userID="2",
        semantic_domains=["Architecture", "Sustainability", "History", "Music"]
    )

# اضافه کردن دسته‌های واژگان
user1.add_vocabulary_category("Interior Design (Architecture)", ["Blueprint", "Facade", "Floor plan", "Minimalism", "Texture", "Lighting", "Furniture", "Aesthetics", "Open space", "Proportion", "Symmetry"])
user1.add_vocabulary_category("Fashion", ["Runway", "Haute couture", "Trendsetter", "Fabric", "Silhouette", "Pattern", "Accessory", "Wardrobe", "Vintage", "Styling", "Seasonal collection", "Designer"])
user1.add_vocabulary_category("Social Media Trends", ["Hashtag", "Viral", "Challenge", "Influencer", "Meme", "Engagement", "Repost", "Filter", "Story", "Algorithm", "Follower"])
user1.add_vocabulary_category("Opera", ["Aria", "Libretto", "Overture", "Tenor", "Soprano", "Chorus", "Stage", "Conductor", "Orchestra", "Costume", "Recitative"])
user1.add_vocabulary_category("Music Awards & Competitions", ["Nomination", "Trophy", "Ceremony", "Finalist", "Performance", "Category", "Voting", "Backstage", "Audience", "Judge", "Winner"])    
user1.add_vocabulary_category("Artistic & Musical Eras", ["Renaissance", "Baroque", "Romanticism", "Modernism", "Impressionism", "Expressionism", "Avant-garde", "Postmodern", "Classical", "Medieval"])
user1.add_vocabulary_category("Romantic Date", ["Candlelight", "Bouquet", "Dinner", "Conversation", "Stroll", "Compliment", "Charm", "Reservation", "Intimacy", "Gift", "Kiss"])
user1.add_vocabulary_category("Vegetarianism", ["Plant-based", "Legumes", "Tofu", "Organic", "Grains", "Leafy greens", "Protein", "Vegan", "Sustainability", "Ethical", "Dairy-free"])
user1.add_vocabulary_category("Endangered Nature & Animals", ["Habitat loss", "Poaching", "Extinction", "Biodiversity", "Conservation", "Climate change", "Wildlife", "Sanctuary", "Deforestation", "Protection"])
user1.add_vocabulary_category("Capitalism & Labor", ["Market", "Profit", "Exploitation", "Union", "Factory", "Class struggle", "Wage", "Surplus", "Consumerism", "Employer", "Strike", "Commodity"])
user1.add_vocabulary_category("Makeup & Cosmetics", ["Foundation", "Mascara", "Eyeliner", "Lipstick", "Blush", "Highlighter", "Concealer", "Contour", "Palette", "Brush", "Skincare", "Primer"])

# دسته‌های ضعیف و پیشنهادی
user1.add_weak_vocabulary_category("Makeup & Cosmetics")
user1.add_weak_vocabulary_category("Opera")
user1.add_suggested_vocabulary_category("Architectural styles")
user1.add_suggested_vocabulary_category("Terminology describing building form")

# اضافه کردن لغات ضعیف
user1.add_weak_word("Renaissance")
user1.add_weak_word("Grains")
user1.add_weak_word("Primer")
user1.add_weak_word("Haute couture")
user1.add_weak_word("Legumes")
user1.add_weak_word("Conductor")

# گرامرهای یاد گرفته‌شده
user1.add_learned_grammar("Present and past", "1", "Present continuous (I am doing)")
user1.add_learned_grammar("Present and past", "2", "Present simple (I do)")
user1.add_learned_grammar("Present and past", "3", "Present continuous and present simple 1 (I am doing and I do)")
user1.add_learned_grammar("Present and past", "4", "Present continuous and present simple 2 (I am doing and I do)")
user1.add_learned_grammar("Present and past", "5", "Past simple (I did)")    
user1.add_learned_grammar("Present and past", "6", "Past continuous (I was doing)") 
user1.add_learned_grammar("Present perfect and past", "7", "Present perfect 1 (I have done)") 

# گرامر بعدی
user1.set_next_grammar("Present perfect and past", "8", "Present perfect 2 (I have done)")
    
# گرامر ضعیف
user1.add_week_grammar("Present and past", "3", "Present continuous and present simple 1 (I am doing and I do)")
user1.add_week_grammar("Present perfect and past", "7", "Present perfect 1 (I have done)")

# گرامرهای نیازمند یادگیری
user1.add_unlearned_needed_grammar("Modals", "29", "may and might 1")
user1.add_unlearned_needed_grammar("Questions and auxiliary verbs", "51", "Auxiliary verbs (have/do/can etc.) I think so / I hope so etc.")



db = UserDatabase()


db.save_user(user1)   

user1Reading = ReadingPracticeTopicGenerator(user1) 
user1ReadingContextData = user1Reading.generate_topics(mode="Suggested")


print(user1ReadingContextData)
#print()
#print("reading_practice")
#print()
#print(reading_practice_description)
#print()
#print(passive_context_data_descriptions)



#topics = pass_entries_to_topic_generator(
#    context_data = user1ReadingContextData,
#    practice_type = "reading_practice",
#    practice_description = reading_practice_description,
#    context_descriptions = passive_context_data_descriptions,
#)


#print(topics)
