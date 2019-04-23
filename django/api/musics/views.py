from django.shortcuts import render, get_object_or_404
from .models import Music, Artist, Comment
from rest_framework.decorators import api_view
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer
from rest_framework.response import Response


@api_view(['GET'])
# Create your views here.
def music_list(request):
    musics = Music.objects.all()    # 여러 개 가져온거
    serializers = MusicSerializer(musics, many = True)
    return Response(serializers.data)
    
    # Serializer = 흩뿌리는 거. 번역기 역할.
    
    
@api_view(['GET'])
def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)   # 한 개 가져온거
    serializers = MusicSerializer(music)
    return Response(serializers.data)
    

@api_view(['GET'])    
def artist_list(request):
    artists = Artist.objects.all()
    serializers = ArtistSerializer(artists, many =True)
    return Response(serializers.data)
    
    
@api_view(['GET'])     
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id = artist_id)
    serializers = ArtistDetailSerializer(artist)
    return Response(serializers.data)
    
    
@api_view(['POST'])  
def comment_create(request, music_id):  # urls.py 주소로부터 받아온 music_id
    serializer = CommentSerializer(data = request.data) # 키워드 인자로 넘겨줘야함.
        # 음악에 대한 정보가 없다. content 만 있다. valid는 통과한다.
    if serializer.is_valid(raise_exception=True):   # 유효한 값이 안들어왔을 때, 400 response라는 에러응답을 보여주게 됨.
        # (raise_exception=True) : 사용자 친화적 코드
        serializer.save(music_id = music_id)    # 장고가 업데이트되어서 commit=False 대신에 넣는다.
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])        
def comment_update_and_delete(request, music_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'PUT':
        serializer = CommentSerializer(data = request.data, instance = comment)
        # data = request.data 정보 받은 것으로 업데이트 하겠다.
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Comment has been updated!'})
    else:
        comment.delete()
        return Response({'message':'Comment has been deleted!'})    # 딕셔너리 형태로 데이터를 넘김.
    