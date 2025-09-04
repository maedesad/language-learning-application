topic_output_examples = {

    #########################  reading practice examples   #########################

    "reading_practice_vocab_categories_dialogue" : [
        {
            "exerciseType": "Reading Practice",
            "context": '''{
                'is_dialogue': True, 
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': None, 
                'grammar_topics': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                    'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                }, 
                'vocab_categories': {
                    'Mountaineering': ['Summit', 'Altitude', 'Base camp', 'Ice axe', 'Crampons', 'Rope', 'Harness', 'Backpack'], 
                    'Art': ['aesthetics', 'avant-garde', 'brushstroke', 'calligraphy', 'composition', 'depiction', 'fresco', 'minimalism', 'mosaic', 'perspective', 'proportion', 'surrealism']
                
                }
            }''',

            "output": '''
                [
                    {
                        "title": "Brushstrokes on the Summit",
                        "description": "A dialogue between two friends combining their love for painting and mountain climbing, naturally practicing present simple, continuous, and present perfect while using art and mountaineering vocabulary."
                    },
                    {
                        "title": "The Artist at Base Camp",
                        "description": "An exchange where a climber explains life at base camp to an artist, mixing everyday contexts with mountain vocabulary and artistic terms, while practicing grammar tenses."
                    },
                    {
                        "title": "Colors Above the Clouds",
                        "description": "A conversation about how climbing experiences inspire artistic expression, reinforcing mountaineering and art vocabulary in a dialogue rich with present and past forms."
                    },
                    {
                        "title": "Canvas of the Mountain",
                        "description": "A creative dialogue where one person describes a mountain as a giant canvas, allowing learners to review everyday contexts, grammar points, and vocab from art and climbing."
                    }
                ]
            '''
        }
    ],

    "reading_practice_vocab_categories_monologue" : [
            {
                "exerciseType": "Reading Practice",
                "context": '''{
                    'is_dialogue': False, 
                    'difficulty': {'5': 
                                    {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                    'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                    'difficulty_example_words': ['music', 'excited', 'park']}                           
                    }, 
                    'semantic_domain': None, 
                    'grammar_topics': {
                        'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                        'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                    }, 
                    'vocab_categories': {
                        'Mountaineering': ['Summit', 'Altitude', 'Base camp', 'Ice axe', 'Crampons', 'Rope', 'Harness', 'Backpack'], 
                        'Art': ['aesthetics', 'avant-garde', 'brushstroke', 'calligraphy', 'composition', 'depiction', 'fresco', 'minimalism', 'mosaic', 'perspective', 'proportion', 'surrealism']
                    
                    }
                }''',

                "output": '''
                    [
                        {
                            "title": "Painting the Summit",
                            "description": "A reflective monologue of a climber-artist describing how reaching the summit feels like painting on the largest canvas in the world, naturally weaving together art and mountaineering vocabulary while practicing key grammar forms."
                        },
                        {
                            "title": "The Mountain as a Masterpiece",
                            "description": "A personal narration where the speaker compares the layers of rock and snow to brushstrokes in a fresco, connecting mountaineering imagery with artistic language in an engaging monologue."
                        },
                        {
                            "title": "Colors at High Altitude",
                            "description": "A climber shares how the changing light and altitude inspire artistic perspectives, integrating vocabulary from both art and mountaineering while practicing present and past grammar points."
                        },
                        {
                            "title": "From Base Camp to Canvas",
                            "description": "A story-like monologue where the journey from base camp is described as building the composition of a painting, allowing the learner to engage with interconnected art and climbing themes."
                        }
                    ]
                '''
            }
    ],

    "reading_practice_semantic_domain_dialogue" : [
        {
            "exerciseType": "Reading Practice",
            "context": '''{
                'is_dialogue': True, 
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': 'sport', 
                'grammar_topics': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                    'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                }  
                'vocab_categories': None         
            }''',

            "output": '''
                [
                    {
                        "title": "Soccer Strategies Unfold",
                        "description": "A dialogue between two friends discussing soccer techniques and training experiences, naturally practicing present simple, continuous, and present perfect forms while using everyday vocabulary suitable for intermediate learners."
                    },
                    {
                        "title": "Morning Run Insights",
                        "description": "A conversation about running routines and personal experiences in sports, reinforcing grammar points in present and past tenses within a sport-themed everyday context."
                    },
                    {
                        "title": "The Tennis Match Review",
                        "description": "Two learners talk about a recent tennis match, sharing opinions and describing actions, which allows practice of present continuous, present simple, and present perfect in an engaging dialogue format."
                    },
                    {
                        "title": "Cycling Adventures",
                        "description": "A discussion between cycling enthusiasts about challenges and achievements in their weekend rides, providing opportunities to practice grammar points while staying within an everyday intermediate-level sports context."
                    }
                ]
            '''
        }
    ],

    "reading_practice_semantic_domain_monologue" : [
            {
                "exerciseType": "Reading Practice",
                "context": '''{
                    'is_dialogue': False, 
                    'difficulty': {'5': 
                                    {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                    'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                    'difficulty_example_words': ['music', 'excited', 'park']}                           
                    }, 
                    'semantic_domain': 'economy', 
                    'grammar_topics': {
                        'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                        'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                    }  
                    'vocab_categories': None         
                }''',

                "output": '''
                    [
                        {
                            "title": "Voices from the Marketplace",
                            "description": "A reflective monologue that captures the rhythm of daily trade and how small exchanges shape larger economic realities, naturally practicing present and past grammar points."
                        },
                        {
                            "title": "Counting Coins, Chasing Dreams",
                            "description": "A personal narration where the speaker connects their everyday financial struggles to broader economic changes, weaving in grammar practice through vivid storytelling."
                        },
                                            "title": "Starting My Own Business",
                            "description": "A personal story where the narrator explains their typical work routine, what tasks they are doing today, and what progress they have made since opening their shop."
                        },
                        {
                            "title": "From Coins to Cards",
                            "description": "A short text tracing how people usually pay for things, what payment methods are becoming common now, and what changes society has experienced in the economy."
                        }
                    ]
                '''
            }
    ],

    #########################  listening practice examples   ######################

    "listening_practice_vocab_categories_dialogue" : [
            {
                "exerciseType": "listening Practice",
                "context": '''{
                    'is_dialogue': True, 
                    'difficulty': {'5': 
                                    {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                    'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                    'difficulty_example_words': ['music', 'excited', 'park']}                           
                    }, 
                    'semantic_domain': None, 
                    'grammar_topics': {
                        'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                        'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                    }, 
                    'vocab_categories': {
                        'Mountaineering': ['Summit', 'Altitude', 'Base camp', 'Ice axe', 'Crampons', 'Rope', 'Harness', 'Backpack'], 
                        'Art': ['aesthetics', 'avant-garde', 'brushstroke', 'calligraphy', 'composition', 'depiction', 'fresco', 'minimalism', 'mosaic', 'perspective', 'proportion', 'surrealism']
                    
                    }
                }''',

                "output": '''
                    [
                        {
                            "title": "Conversations at the Art Exhibit",
                            "description": "A dialogue between visitors at an art gallery, discussing paintings and exhibitions, designed for intermediate learners to practice present simple, continuous, and present perfect forms while listening carefully to everyday vocabulary from art and mountaineering contexts."
                        },
                        {
                            "title": "Mountain Trek Reflections",
                            "description": "Two friends describe their recent hiking experience, mentioning equipment and challenges. The dialogue format allows learners to follow and understand grammar points in present and past tenses, suitable for listening practice."
                        },
                        {
                            "title": "Painting Techniques Discussed",
                            "description": "A conversation between an artist and a student about different brushstrokes and composition methods, integrating mountaineering anecdotes, providing clear listening content with intermediate-level grammar and vocabulary."
                        },
                        {
                            "title": "Summit Stories Shared",
                            "description": "A dialogue recounting adventures on a mountain peak, combining narrative elements with descriptive language, enabling learners to practice listening comprehension while reinforcing grammar and thematic vocabulary."
                        }
                    ]
                '''
            }
    ],

    "listening_practice_vocab_categories_monologue" : [
        {
            "exerciseType": "listening Practice",
            "context": '''{
                'is_dialogue': False, 
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': None, 
                'grammar_topics': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                    'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                }, 
                'vocab_categories': {
                    'Mountaineering': ['Summit', 'Altitude', 'Base camp', 'Ice axe', 'Crampons', 'Rope', 'Harness', 'Backpack'], 
                    'Art': ['aesthetics', 'avant-garde', 'brushstroke', 'calligraphy', 'composition', 'depiction', 'fresco', 'minimalism', 'mosaic', 'perspective', 'proportion', 'surrealism']
                
                }
            }''',

            "output": '''
                [
                    {
                        "title": "Sketching at the Base Camp",
                        "description": "A monologue where the speaker recalls setting up camp during a mountain expedition while sketching the scenery, using mountaineering terms alongside artistic vocabulary like brushstroke and composition."
                    },
                    {
                        "title": "The Summit and the Canvas",
                        "description": "A reflective story about reaching the summit and later painting the view, practicing present and past tenses with integrated vocabulary from both mountaineering and art."
                    },
                    {
                        "title": "A Gallery of Mountains",
                        "description": "A personal narrative in which the speaker describes how they usually climb mountains and how they are currently preparing an exhibition of artworks inspired by their expeditions."
                    },
                    {
                        "title": "From Ropes to Frescoes",
                        "description": "A creative monologue where the narrator connects the precision of mountaineering equipment with the careful details of fresco painting, practicing grammar through vivid imagery."
                    }
                ]
            '''
        }
    ],

    "listening_practice_semantic_domain_dialogue" : [
        {
            "exerciseType": "Listening Practice",
            "context": '''{
                'is_dialogue': True, 
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': 'sport', 
                'grammar_topics': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                    'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                }  
                'vocab_categories': None         
            }''',

            "output": '''
                [
                    {
                        "title": "Morning Jog Chat",
                        "description": "A dialogue between two friends discussing their morning jog routines and sports activities, designed for intermediate learners to practice present simple, continuous, and present perfect forms while listening attentively to sports-related vocabulary."
                    },
                    {
                        "title": "Preparing for the Marathon",
                        "description": "A conversation between runners planning their training schedule and sharing tips, allowing learners to follow clear audio input and reinforce grammar points in present and past tenses."
                    },
                    {
                        "title": "Team Sports Talk",
                        "description": "Two teammates discuss their experiences and strategies in a recent football match, providing vivid listening content and integrating everyday sports vocabulary suitable for intermediate learners."
                    },
                    {
                        "title": "Gym Time Stories",
                        "description": "A dialogue about fitness routines and personal progress at the gym, offering engaging listening practice while naturally practicing target grammar structures and sports-related vocabulary."
                    }
                ]
            '''
        }
    ],

    "listening_practice_semantic_domain_monologue" : [
        {
            "exerciseType": "Listening Practice",
            "context": '''{
                'is_dialogue': False, 
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': 'art', 
                'grammar_topics': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                    'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                }  
                'vocab_categories': None         
            }''',

            "output": '''
                [
                    {
                        "title": "The Sculpture That Never Ends",
                        "description": "An artist talks about a project that has taken a long time, describing what they usually do, what they are currently working on, and what they have already finished."
                    },
                    {
                        "title": "Listening to Colors",
                        "description": "A monologue where someone explains their feelings about colors in paintings, practicing present simple for general opinions and present continuous for current impressions in the gallery."
                    },
                    {
                        "title": "Painting My First Portrait",
                        "description": "A personal story about learning to paint: what the speaker usually does when painting, what they are working on at the moment, and what they have completed so far."
                    },
                    {
                        "title": "In Front of the Canvas",
                        "description": "A painter describes their daily routine in the studio and what they are working on right now, using present simple for habits and present continuous for current actions."
                    }
                ]
            '''
        }
    ], 

    #########################  writing practice examples   ########################

    "writing_practice_vocab_categories" : [
        {
            "exerciseType": "Writing Practice",
            "context": '''{            ' 
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': None, 
                'grammar_topics': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                    'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                }, 
                'vocab_categories': {
                    'Mountaineering': ['Summit', 'Altitude', 'Base camp', 'Ice axe', 'Crampons', 'Rope', 'Harness', 'Backpack'], 
                    'Art': ['aesthetics', 'avant-garde', 'brushstroke', 'calligraphy', 'composition', 'depiction', 'fresco', 'minimalism', 'mosaic', 'perspective', 'proportion', 'surrealism']
                
                }
            }''',

            "output": '''
                [
                    {
                        "title": "Describe a Day at Base Camp and How It Felt to Experience the Mountain Environment",
                        "description": "Write a short text about what a day at a mountaineering base camp might be like. Include activities, feelings, and simple opinions, while showing how daily life is different in such a place compared to the city."
                    },
                    {
                        "title": "Tell the Story of Visiting an Art Exhibition That Reminded You of Nature or Adventure",
                        "description": "Imagine you went to an exhibition where the paintings made you think of climbing mountains or exploring new places. Write about your experience, describing what you saw and how you felt."
                    },
                    {
                        "title": "Write About a Time You Learned a New Skill Like Climbing or Painting and How It Changed You",
                        "description": "Think about learning something challenging, such as using climbing equipment or practicing a new art technique. Write a short story about the process, your feelings, and what you can do now."
                    },
                    {
                        "title": "Explain How Music, Art, or Sports Can Inspire People to Feel Excited and Motivated",
                        "description": "Write a short essay explaining how creative activities like listening to music, climbing a mountain, or painting can influence people’s emotions and help them stay motivated in everyday life."
                    }
                ]
                    '''
        }
    ],

    "writing_practice_semantic_domain" : [
        {
            "exerciseType": "Writing Practice",
            "context": '''{            
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': 'sport', 
                'grammar_topics': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                    'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                }  
                'vocab_categories': None         
            }''',

            "output": '''
                [
                    {
                        "title": "Write About a Sport You Practice Regularly and How It Fits Into Your Daily Life",
                        "description": "Describe a sport or physical activity that you do often. Explain when and how you usually practice it, what you enjoy about it, and how it makes you feel."
                    },
                    {
                        "title": "Tell the Story of a Memorable Match or Game You Watched or Played",
                        "description": "Write a short story about a specific sports event in the past. Explain what happened, who was involved, and why it was exciting or meaningful for you."
                    },
                    {
                        "title": "Explain How Playing or Watching Sports Has Changed Your Habits or Feelings Over Time",
                        "description": "Write about the ways sports have influenced your life. Focus on how your feelings or routines are different now compared to before."
                    },
                    {
                        "title": "Describe the Reasons Why You Enjoy a Particular Sport",
                        "description": "Write about one sport that you like most. Explain what makes it enjoyable for you and why it is important in your life."
                    }
                ]
            '''
        }
    ],


    #########################  conversation practice examples   ###################

    "conversation_practice_vocab_categories" : [
        {
            "exerciseType": "Conversation Practice",
            "context": '''{            ' 
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': None, 
                'grammar_topics': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                    'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                }, 
                'vocab_categories': {
                    'Mountaineering': ['Summit', 'Altitude', 'Base camp', 'Ice axe', 'Crampons', 'Rope', 'Harness', 'Backpack'], 
                    'Art': ['aesthetics', 'avant-garde', 'brushstroke', 'calligraphy', 'composition', 'depiction', 'fresco', 'minimalism', 'mosaic', 'perspective', 'proportion', 'surrealism']
                
                }
            }''',

            "output": '''
                [
                    {
                        "title": "Art Exhibition at the Mountain Base",
                        "description": "You are a visitor at a base camp where an art exhibition shows paintings of summits and mountaineering life. The AI is the artist explaining the use of perspective and surrealism in the works."
                    },
                    {
                        "title": "Discussing Mountain Photography",
                        "description": "You are a climber who meets a photographer on the trail. The AI is the photographer, and together you talk about capturing the altitude, landscapes, and composition of the mountain scenes."
                    },
                    {
                        "title": "Designing a Monument for Climbers",
                        "description": "You are a mountaineer invited to share ideas. The AI is an avant-garde artist asking you about your experiences with ropes, harnesses, and summits to inspire a sculpture or fresco."
                    },
                    {
                        "title": "Gallery Talk: Adventure Meets Art",
                        "description": "You are a guest at an art gallery where works are inspired by mountaineering. The AI is the artist, discussing how tools like an ice axe and the feeling of altitude shaped their mosaic or brushstrokes."
                    }
                ]
                    '''
        }       
    ],

    "conversation_practice_semantic_domain" : [
        {
            "exerciseType": "Conversation Practice",
            "context": '''{            
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': 'sport', 
                'grammar_topics': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}, 
                    'Present perfect and past': {'7': 'Present perfect 1 (I have done)'}
                }  
                'vocab_categories': None         
            }''',

            "output": '''
                [
                    {
                        "title": "Talking About Playing Football",
                        "description": "You are a student describing how you usually play football and what you did in your last match. The AI is a teacher asking you about your routine and experiences."
                    },
                    {
                        "title": "Joining a Basketball Club",
                        "description": "You are a new member of a basketball club. The AI is the coach asking about your current skills, past training, and what you expect from the club."
                    },
                    {
                        "title": "Planning a Weekend Hiking Trip",
                        "description": "You are a friend suggesting a hiking trip this weekend. The AI is another friend responding, talking about what they are doing now and what hiking trips they have already done."
                    },
                    {
                        "title": "Explaining Your Swimming Experience",
                        "description": "You are a swimmer sharing your experiences at the swimming pool. The AI is a reporter asking what you usually do there and what you have recently achieved."
                    }
                ]
            '''
        }
    ],

    #########################  grammar learning examples   ########################

    "grammar_learning_dialogue" : [
        {
            "exerciseType": "Grammar Practice",
            "context": '''{
                'is_dialogue': True, 
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': cooking, 
                'grammar_topic': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}                
                },

            }''',

            "output": '''
                [
                    {
                        "title": "The Mystery of the Missing Spoon",
                        "description": "Read a dialogue between two friends trying to find a lost cooking utensil, practicing present simple for routines and present continuous for what they are doing now."
                    },
                    {
                        "title": "Planning a Weekend Dinner",
                        "description": "Read a dialogue where two people discuss their weekend cooking plans, using present simple for regular activities and present continuous for current preparations."
                    },
                    {
                        "title": "A Busy Morning Recipe",
                        "description": "Read a dialogue describing someone's breakfast routine while cooking, practicing present simple for habits and present continuous for actions happening now."
                    },
                    {
                        "title": "Trying a New Recipe",
                        "description": "Read a short dialogue about someone following the steps of a new dish, practicing present continuous for actions in progress and present simple for general cooking facts."
                    }
                ]
            '''
        }
    ],

    "grammar_learning_monologue" : [
        {
            "exerciseType": "Grammar Practice",
            "context": '''{
                'is_dialogue': False, 
                'difficulty': {'5': 
                                {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                'difficulty_example_words': ['music', 'excited', 'park']}                           
                }, 
                'semantic_domain': cooking, 
                'grammar_topic': {
                    'Present and past': {'3': 'Present continuous and present simple 1 (I am doing and I do)'}                
                },

            }''',

            "output": '''
                [
                        {
                            "title": "My Morning in the Kitchen",
                            "description": "Read a short monologue where someone describes their usual breakfast routine and what they are preparing right now, contrasting habits with current actions."
                        },
                        {
                            "title": "Cooking While Listening to Music",
                            "description": "A monologue about a person talking about how they usually cook with music and what they are cooking at the moment, practicing present simple and present continuous."
                        },
                        {
                            "title": "The Perfect Pasta Story",
                            "description": "Read a monologue where a cook explains how they usually make pasta and what they are currently doing to prepare a new recipe."
                        },
                        {
                            "title": "A Day as a Busy Chef",
                            "description": "A monologue describing a chef’s daily cooking routines and what dishes they are preparing right now, mixing general facts with actions in progress."
                        }
                    ]
            '''
        }
    ],

    #########################  vocab learning examples   #########################

    "vocab_learning" : [
            {
                "exerciseType": "Vocab Learning",
                "context": '''{            
                    'difficulty': {'5': 
                                    {'difficulty_level': 'level 5 - Everyday Contexts – Intermediate (B1-)', 
                                    'level_description': 'More variety in vocabulary, covering feelings, hobbies, and simple opinions.', 
                                    'difficulty_example_words': ['music', 'excited', 'park']}                           
                    }, 
                    'semantic_domain': Sport, 
                    'existing_vocab_categories': {
                        'Art': ['aesthetics', 'avant-garde', 'brushstroke', 'calligraphy', 'composition', 'depiction', 'fresco', 'minimalism', 'mosaic', 'perspective', 'proportion', 'surrealism'], 
                        'Breakfast Items': ['plate', 'cup', 'pan', 'Carafe', 'Sugar bowl', 'Napkin holder', 'Jam jar', 'Toast', 'Butter', 'Cereal', 'Yogurt', 'Boiled egg', 'Breakfast tray', 'Orange juice'], 
                        'Cryptocurrency': ['blockchain', 'wallet', 'token', 'mining', 'decentralization', 'exchange', 'ledger', 'smart contract', 'NFT', 'staking', 'gas fee', 'hashrate'], 
                        'Healthy Nutrition': ['fiber', 'protein', 'whole grains', 'legumes', 'vitamins', 'minerals', 'antioxidants', 'hydration', 'balanced diet', 'superfoods', 'healthy fats', 'portion control'], 
                        'Mountaineering': ['Summit', 'Altitude', 'Base camp', 'Ice axe', 'Crampons', 'Rope', 'Harness', 'Backpack']
                    }
                }''',

                "output": '''
                    [
                        {
                            "vocab_category": "Indoor Sports Equipment",
                            "description": "Vocabulary related to gear and tools used in indoor sports, such as badminton rackets, yoga mats, dumbbells, and table tennis paddles."
                        },
                        {
                            "vocab_category": "Team Sports Positions",
                            "description": "Words describing roles and positions in team sports, like goalkeeper, striker, midfielder, pitcher, and point guard."
                        },
                        {
                            "vocab_category": "Water Sports Activities",
                            "description": "Terms for common water-based sports and actions, including swimming, kayaking, diving, surfing, and paddleboarding."
                        },
                        {
                            "vocab_category": "Fitness Exercises",
                            "description": "Vocabulary covering different exercises in fitness routines, such as push-ups, squats, lunges, planks, and jumping jacks."
                        }
                    ]
                '''
            }
    ],

}