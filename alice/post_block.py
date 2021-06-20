from user import User

class Post:

    # 생성자는 매개변수로 작성자와 내용을 받아,
    # 그 값을 속성에 저장합니다.
    def __init__(self, author, content):
        
        # 속성들을 초기화합니다.
        self.author = author
        self.content = content
        
        # 아래의 코드를 수정하세요.
        self.comments = []
        self.blocks = []
    
    
    # 댓글을 추가하는 기능 가진 addComment 메서드를 생성합니다.
    # 아래의 코드를 수정해서 메서드를 완성하세요.
    def addComment(self,comment_author,comment):
        comments.append([comment_author,comment])
        
    
    # 차단 기능을 가진 addBlock 메서드를 생성합니다.
    # 아래의 코드를 수정해서 메서드를 완성하세요.
    def addBlock(self,user):
        if user in self.blocks:
            self.blocks.remove(user)
        else:
            self.blocks.append(user)
        
        
    # 게시글과 댓글의 내용을 반환해주는 display 메서드를 생성합니다.
    # 아래의 코드를 수정해서 메서드를 완성하세요.
    def display(self, user):
        # 출력할 결과를 저장할 result 입니다.
        result = ""    
        # 차단된 유저가 글을 볼 수 없도록 아래의 조건문을 작성합니다.
        if user not in self.blocks:
            result += "작성자 : " + str(self.author)
            result += "\n내  용 : " + str(self.content)
            result += "\n댓  글\n"
            for i in range(len(self.comments)):
                result += str(self.comments[i][1]) + "-" + str(self.comments[i][0]) + "\n"
            
        else:
            result = "차단된 사용자입니다"
        
        return result

# 새로운 사용자를 생성합니다.
me = User("me")

# 아래에 자유롭게 인스턴스를 생성하고 테스트해보세요.
my_post = Post(me.name, "첫 게시글!!")

