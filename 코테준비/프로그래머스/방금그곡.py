def solution(m, musicinfos):

    music_info = []
    for music in musicinfos:
        start, end, name, song = music.split(",")
        start_hour, start_min = map(int, start.split(":"))
        end_hour, end_min = map(int, end.split(":"))
        last_min = 60 * (end_hour - start_hour) + (end_min - start_min)
        song_list = []
        song = song.replace("C#", "c")
        song = song.replace("B#", "b")
        song = song.replace("D#", "d")
        song = song.replace("F#", "f")
        song = song.replace("G#", "g")
        song = song.replace("A#", "a")
        song = song.replace("E#", "e")
        # print("어", song)
        song = list(song)

        for i in range(last_min):
            song_list.append(song[i % len(song)])

        song = "".join(song_list)
        music_info.append([last_min, name, song])
    #     print("읭", song_list)
    # print(music_info)
    music_info.sort(reverse=True)
    # print(music_info)
    m = m.replace("C#", "c")
    m = m.replace("B#", "b")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")
    m = m.replace("E#", "e")
    for music in music_info:
        if m in music[2]:
            return music[1]

    # print(last_min)
    # print(start_hour, end_min)
    return "(None)"


m = "ABCDEFG"
m = "ABC"
m = "CC#BCC#BCC#"
# m = "CC#BCC#BCC#BCC#B"
musicinfos = ["12:00,12:14,HELLO,CDE#F#GAB", "13:00,13:05,WORLD,ABCDEF"]
musicinfos = ["12:00,12:14,HELLO,C#D#EFGA#B#", "13:00,13:05,WORLD,ABCDEF"]
musicinfos = ["03:00,03:08,FOO,CC#B"]
m = "CCB"
musicinfos = ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]
# musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))
