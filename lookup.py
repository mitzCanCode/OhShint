import requests

# Function to search for username across multiple websites
def search(username: str) -> dict:
    # List of mainstream websites to check
    websites = [
        f'https://www.instagram.com/{username}', f'https://www.facebook.com/{username}', 
        f'https://www.twitter.com/{username}', f'https://www.youtube.com/{username}', 
        f'https://{username}.blogspot.com', f'https://plus.google.com/s/{username}/top', 
        f'https://www.reddit.com/user/{username}', f'https://{username}.wordpress.com', 
        f'https://www.pinterest.com/{username}', f'https://www.github.com/{username}', 
        f'https://{username}.tumblr.com', f'https://www.flickr.com/people/{username}', 
        f'https://steamcommunity.com/id/{username}', f'https://vimeo.com/{username}', 
        f'https://soundcloud.com/{username}', f'https://disqus.com/by/{username}', 
        f'https://medium.com/@{username}', f'https://{username}.deviantart.com', 
        f'https://vk.com/{username}', f'https://about.me/{username}', 
        f'https://imgur.com/user/{username}', f'https://flipboard.com/@{username}', 
        f'https://slideshare.net/{username}', f'https://fotolog.com/{username}', 
        f'https://open.spotify.com/user/{username}', f'https://www.mixcloud.com/{username}', 
        f'https://www.scribd.com/{username}', f'https://www.badoo.com/en/{username}', 
        f'https://www.patreon.com/{username}', f'https://bitbucket.org/{username}', 
        f'https://www.dailymotion.com/{username}', f'https://www.etsy.com/shop/{username}', 
        f'https://cash.me/{username}', f'https://www.behance.net/{username}', 
        f'https://www.goodreads.com/{username}', f'https://www.instructables.com/member/{username}', 
        f'https://keybase.io/{username}', f'https://kongregate.com/accounts/{username}', 
        f'https://{username}.livejournal.com', f'https://angel.co/{username}', 
        f'https://last.fm/user/{username}', f'https://dribbble.com/{username}', 
        f'https://www.codecademy.com/{username}', f'https://en.gravatar.com/{username}', 
        f'https://pastebin.com/u/{username}', f'https://foursquare.com/{username}', 
        f'https://www.roblox.com/user.aspx?username={username}', f'https://www.gumroad.com/{username}', 
        f'https://{username}.newgrounds.com', f'https://www.wattpad.com/user/{username}', 
        f'https://www.canva.com/{username}', f'https://creativemarket.com/{username}', 
        f'https://www.trakt.tv/users/{username}', f'https://500px.com/{username}', 
        f'https://buzzfeed.com/{username}', f'https://tripadvisor.com/members/{username}', 
        f'https://{username}.hubpages.com', f'https://{username}.contently.com', 
        f'https://houzz.com/user/{username}', f'https://blip.fm/{username}', 
        f'https://www.wikipedia.org/wiki/User:{username}', f'https://news.ycombinator.com/user?id={username}', 
        f'https://www.reverbnation.com/{username}', f'https://www.designspiration.net/{username}', 
        f'https://www.bandcamp.com/{username}', f'https://www.colourlovers.com/love/{username}', 
        f'https://www.ifttt.com/p/{username}', f'https://www.ebay.com/usr/{username}', 
        f'https://{username}.slack.com', f'https://www.okcupid.com/profile/{username}', 
        f'https://www.trip.skyscanner.com/user/{username}', f'https://ello.co/{username}', 
        f'https://tracky.com/user/~{username}', f'https://{username}.basecamphq.com/login',
        f'https://twitch.tv/{username}', f'https://www.periscope.tv/{username}', 
        f'https://www.smashcast.tv/{username}', f'https://mixer.com/{username}', 
        f'https://www.dlive.tv/{username}', f'https://www.caffeine.tv/{username}', 
        f'https://www.peertube.social/video-channels/{username}', f'https://www.brighteon.com/channel/{username}', 
        f'https://www.minds.com/{username}', f'https://www.gab.com/{username}', 
        f'https://www.parler.com/profile/{username}', f'https://www.bitchute.com/channel/{username}', 
        f'https://www.odysee.com/@{username}', f'https://www.rumble.com/c/{username}', 
        f'https://www.gettr.com/user/{username}', f'https://www.truthsocial.com/@{username}', 
        f'https://www.clouthub.com/{username}', f'https://www.vk.com/{username}', 
        f'https://www.patreon.com/{username}', f'https://ko-fi.com/{username}', 
        f'https://www.buymeacoffee.com/{username}', f'https://www.subscribestar.com/{username}', 
        f'https://www.ustream.tv/{username}', f'https://www.livestream.com/{username}', 
        f'https://www.picarto.tv/{username}', f'https://www.trovo.live/{username}'
    ]

    found_lst = []
    count = 0
    match = True
    for url in websites:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                if match:
                    match = False
                print(f'\033[92m\n{url} - {r.status_code} - OK\033[0m')  # Green for OK status
                if username in r.text:
                    print(f'\033[92mPositive match.\033[0m')  # Green for positive match
                else:
                    print(f'\033[93mPositive match.\n WARNING: \033[91mtext has NOT been detected in url, could be a false positive.\033[0m')  # Yellow for warning and red for false positive warning
                found_lst.append(url)
                count += 1
        except requests.RequestException as e:
            print(f'\033[91m[-] Error accessing {url}: {e}\033[0m')  # Red for error
    passwords = {index: url for index, url in enumerate(found_lst)}
    print(f'\033[92mFINISHED: A total of {count} MATCHES found out of {len(websites)} websites.\033[0m')  # Green for finished summary
    return passwords

if __name__ == '__main__':
    username = input('\033[92m{+} Enter username to lookup: \033[0m')
    search(username)
