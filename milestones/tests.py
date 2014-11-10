from rest_framework.test import APITestCase
from rest_framework import status
from milestones.models import Diary, MileStone
from rest_framework.status import HTTP_204_NO_CONTENT

# Create your tests here.

class DiaryViewSetTests(APITestCase):
    
    def setUp(self):
                
        diary1 = Diary.objects.create(title='hoge', description='Hello')
        MileStone.objects.create(diary=diary1, page_id='IIIII')
        MileStone.objects.create(diary=diary1, page_id='XXXXX')
        
        diary2 = Diary.objects.create(title='fuga', description='Good bye')
        MileStone.objects.create(diary=diary2, page_id='JJJJJ')
        MileStone.objects.create(diary=diary2, page_id='YYYYY')
        
        diary3 = Diary.objects.create(title='puyo', description='See you')
        MileStone.objects.create(diary=diary3, page_id='KKKKK')
        MileStone.objects.create(diary=diary3, page_id='ZZZZZ')
            
    def test_view_list_get(self):
        
        response = self.client.get("/diaries/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['title'], 'hoge')
        self.assertEqual(response.data[0]['milestones'][0]['page_id'], 'IIIII')
        self.assertEqual(response.data[0]['milestones'][1]['page_id'], 'XXXXX')

        self.assertEqual(response.data[1]['title'], 'fuga')
        self.assertEqual(response.data[1]['milestones'][0]['page_id'], 'JJJJJ')
        self.assertEqual(response.data[1]['milestones'][1]['page_id'], 'YYYYY')
        
    def test_view_list_get_with_param_title(self):

        response = self.client.get("/diaries/?title=fug")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)

        self.assertEqual(response.data[0]['title'], 'fuga')
        self.assertEqual(response.data[0]['milestones'][0]['page_id'], 'JJJJJ')
        self.assertEqual(response.data[0]['milestones'][1]['page_id'], 'YYYYY')

    def test_view_list_get_with_param_description(self):

        response = self.client.get("/diaries/?description=Good")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 1)

        self.assertEqual(response.data[0]['title'], 'fuga')
        self.assertEqual(response.data[0]['description'], 'Good bye')
        self.assertEqual(response.data[0]['milestones'][0]['page_id'], 'JJJJJ')
        self.assertEqual(response.data[0]['milestones'][1]['page_id'], 'YYYYY')

    def test_view_list_post(self):
         
        data = {
                'title': 'piyo',
                'description': 'hoge fuga piyo',
                'milestones': [
                               {
                                'page_id': 'KKKKK'
                                },
                               {
                                'page_id': 'LLLLL'
                                }
                               ]
                }
        response = self.client.post('/diaries/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
        self.assertEqual(response.data['title'], 'piyo')
        self.assertEqual(response.data['description'], 'hoge fuga piyo')
        self.assertEqual(len(response.data['milestones']), 2)
        self.assertEqual(response.data['milestones'][0]['page_id'], 'KKKKK')
        self.assertEqual(response.data['milestones'][1]['page_id'], 'LLLLL')

    def test_view_detail_get(self):
        
        diary = Diary.objects.get(title='fuga')

        response = self.client.get("/diaries/"+str(diary.id)+"/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.data['title'], 'fuga')
        self.assertEqual(response.data['milestones'][0]['page_id'], 'JJJJJ')
        self.assertEqual(response.data['milestones'][1]['page_id'], 'YYYYY')
        
    def test_view_detail_put(self):
        
        diary = Diary.objects.get(title='hoge')

        response = self.client.get("/diaries/"+str(diary.id)+"/")
         
        self.assertEqual(response.status_code, status.HTTP_200_OK)
         
        self.assertEqual(response.data['title'], 'hoge')
        self.assertEqual(response.data['milestones'][0]['page_id'], 'IIIII')
        self.assertEqual(response.data['milestones'][1]['page_id'], 'XXXXX')
  
        data = {
                'title': 'puyo',
                'description': 'hoge fuga piyo'
                }
        response2 = self.client.put('/diaries/'+str(diary.id)+'/', data, format='json')
 
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.data['title'], 'puyo')
        self.assertEqual(response2.data['description'], 'hoge fuga piyo')
#         self.assertEqual(len(response.data['milestones']), 2)
#         self.assertEqual(response.data['milestones'][0]['page_id'], 'KKKKK')
#         self.assertEqual(response.data['milestones'][1]['page_id'], 'LLLLL')

    def test_view_detail_delete(self):
         
        response = self.client.get("/diaries/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 3)
        
        diary = Diary.objects.get(title='puyo')
        response2 = self.client.delete('/diaries/'+str(diary.id)+'/')
        self.assertEqual(response2.status_code, HTTP_204_NO_CONTENT)
         
        
        response3 = self.client.get("/diaries/")
        
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response3.data), 2)

        
class MilestoneViewSetTests(APITestCase):

     
    def setUp(self):
                
        diary1 = Diary.objects.create(title='hoge')
        MileStone.objects.create(diary=diary1, page_id='IIIII')
        MileStone.objects.create(diary=diary1, page_id='JJJJJ')
         
        diary2 = Diary.objects.create(title='fuga')
        MileStone.objects.create(diary=diary2, page_id='KKKKK')
        MileStone.objects.create(diary=diary2, page_id='LLLLL')
        
    def test_view_list_get(self):
         
        response = self.client.get("/milestones/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 4)

        self.assertEqual(response.data[0]['page_id'], 'IIIII')
        self.assertEqual(response.data[1]['page_id'], 'JJJJJ')
        
    def test_view_list_get_with_param_diary(self):
        
        diary = Diary.objects.get(title='fuga')
        
        response = self.client.get("/milestones/?diary=" + str(diary.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['page_id'], 'KKKKK')
        self.assertEqual(response.data[1]['page_id'], 'LLLLL')
        
    def test_view_list_get_with_param_page_id(self):
        
        response = self.client.get("/milestones/?page_id=KKKKK")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 1)

        self.assertEqual(response.data[0]['page_id'], 'KKKKK')
        
    def test_view_detail_delete(self):
        
        response1 = self.client.get("/milestones/")
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response1.data), 4)
        
        milestone = MileStone.objects.get(page_id="KKKKK")
        response2 = self.client.delete("/milestones/" + str(milestone.id) + "/")
        self.assertEqual(response2.status_code, status.HTTP_204_NO_CONTENT)
        
        response3 = self.client.get("/milestones/")
        self.assertEqual(response3.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response3.data), 3)

    def test_view_list_post(self):
          
        diary = Diary.objects.get(title="fuga")
          
        data = {
                'diary': diary.id,
                'page_id': 'MMMMM'
        }
          
        response = self.client.post('/milestones/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
  
        self.assertEqual(response.data['diary'], diary.id)
        self.assertEqual(response.data['page_id'], 'MMMMM')
  
        response2 = self.client.get('/milestones/')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
  
        self.assertEqual(len(response2.data), 5)

    def test_view_detail_put(self):
        
        milestone = MileStone.objects.get(page_id='IIIII')
        
        response = self.client.get("/milestones/"  + str(milestone.id) + "/")
        data = response.data

        data['page_id'] = "NNNNN"
                    
        response2 = self.client.put('/milestones/' + str(milestone.id) + '/', data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
  
        self.assertEqual(response.data['diary'], data['diary'])
        self.assertEqual(response.data['page_id'], 'NNNNN')