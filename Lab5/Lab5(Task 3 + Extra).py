import collections

from vk_api import *
from vk_api.audio import VkAudio


# Task 3
# vk.com

def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def main():
    """ Пример обработки двухфакторной аутентификации """

    login, password = 'login', 'password'  # ваш логин и пароль
    vk_session = vk_api.VkApi(
        login, password,
        # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler
    )
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    # вывод всех постов со стены
    tools = vk_api.VkTools(vk_session)

    wall = tools.get_all('wall.get', 100, {'owner_id': 1})

    print('Posts count:', wall['count'])

    if wall['count']:
        print('First post:', wall['items'][0], '\n')

    if wall['count'] > 1:
        print('Last post:', wall['items'][-1])

    """ Пример составления топа исполнителей для профиля вк """
    vkaudio = VkAudio(vk_session)

    artists = collections.Counter(
        track['artist'] for track in vkaudio.get_iter()
    )

    # Составляем рейтинг первых 15
    print('Top 15:')
    for artist, tracks in artists.most_common(15):
        print('{} - {} tracks'.format(artist, tracks))

    # Ищем треки самого популярного
    most_common_artist = artists.most_common(1)[0][0]

    print('\nSearching for {}:'.format(most_common_artist))

    tracks = vkaudio.search(q=most_common_artist, count=10)

    for n, track in enumerate(tracks, 1):
        print('{}. {} {}'.format(n, track['title'], track['url']))


if __name__ == '__main__':
    main()
