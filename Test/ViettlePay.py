import requests, json


class ViettlePay:
    def __init__(self, phone, token = None):
        self.phone = phone

        s = requests.session

        s.headers = {
            'Password': 'digital@2020',
            'Channel': 'APP',
            'Content-Type': 'application/json',
            'User-Id': self.phone,
            'User-Agent': 'ViettelPay/3.3.1 (iPhone; iOS 13.3; Scale/3.00)',
            'Authorization': token
        }
        self.s = s

        def requestLogin(self, phone):
            return self.s.get('https://vtpay8.viettel.vn/shake-2020/user/request-login').json()

            def login(self, otp):
                data = {'otp': otp}

                r = self.s.post('https://vtpay8.viettel.vn/shake-2020/user/login', data=json.dumps(data)).json()

                if (r['status']['code'] != '00'):
                    return [False, r]

                self.s.headers['Authorization'] = r['data']['token']

                return [True, r]

            def getProfile(self):
                return self.s.get('https://vtpay8.viettel.vn/shake-2020/user/profile').json()

            def play(self):
                return self.s.post('https://vtpay8.viettel.vn/shake-2020/game/play').json()

        if __name__ == '__main__':
            print('ViettelPay auto roll 2019 - By T-Rekt - J2TEAM\n')

            print('Please input your phone number: ')
            phone = input()
            if (phone[0] == '0'):
                phone = phone[1:]

            vtp = ViettlePay(phone)
            sendOtp = vtp.requestLogin(phone)

            if (sendOtp['status']['code'] != '00'):
                print('Send OTP failed')
                exit(0)

            print('Please input your OTP: ')
            otp = input()
            if (vtp.login(otp)[1]['status']['code'] != '00'):
                print('Login failed')
                exit(0)

            profile = vtp.getProfile()
            turnsLeft = profile['data']['totalTurnLeft']

            while (turnsLeft):
                rollResult = vtp.play()
                reward = ''
                if (rollResult['data']):
                    reward = rollResult['data']['name']
                print(f"Turns left: {turnsLeft}. Rolled: {rollResult['status']['message']}. {reward}")
                # print(rollResult)
                turnsLeft -= 1

            print('Out of turn')
