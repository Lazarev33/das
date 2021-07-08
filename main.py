import vk_api
import time
access_token = "21ea03d8c41d253b48b15843b62116a35eebcdbe1fa9c2ac53b2208ff0be5fd03eff8a8736a807921bf94"
vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

while True:
    e = vk.wall.getComments(owner_id='226594619', post_id='2392', count='1', sort='desc', v=5.124)
    if int((e['items'][0]['from_id']))>0:
        e1 = vk.users.get(user_ids=str(e['items'][0]['from_id']), v=5.124)
        print(e1[0]['last_name'])
        print(vk.account.saveProfileInfo(last_name=str(e1[0]['last_name']), v=5.124))
        time.sleep(60)
