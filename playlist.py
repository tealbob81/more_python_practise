##playlist = [[{'Track': 'One'},
##             {'Artist': 'Bear'},
##             {'Album': 'Bear\'s Greatest Hits'},
##             {'Duration': '2:20'}],
##            [{'Track': 'Two'},
##             {'Artist': 'Bear feat. The Cat'},
##            {'Album': 'Bear and Friends'},
##            {'Duration': '45:22'}]]
##
##
##
##new_l = [i for i in playlist if 'Track' == 'Two']
##print(new_l)


playlist = {
    'title': 'Bear\'s playlist',
    'maker': 'Bear',
    'songs': [
        {'title': 'How much is that doggy in the window',
         'artist': ['Bear'], 'duration': 3.45},
        {'title': 'Aint nothin but a hound dog',
         'artist': ['Bear', 'DJ TheCat'], 'duration': 4.20},
        {'title': 'I love cats',
         'artist': ['Bear'], 'duration': 2.30},
        {'title': 'Who let the dogs out',
         'artist': ['Bear and Friends'], 'duration': 8.57},
    ]
}

total_len = 0

for song in playlist['songs']:
    total_len += song['duration']
print(total_len)
          
