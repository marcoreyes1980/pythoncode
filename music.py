from pytube import YouTube
source = input('please provide YouTube link: ')

YouTube(source).streams.first().download()
yt = YouTube(source)
yt.streams 