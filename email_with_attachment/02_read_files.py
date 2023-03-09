from os import listdir
import pandas as pd
pd.set_option('display.max_columns', None)


def make_email_list(data_path, partners_filename, title, target_filename='이메일발송목록.xlsx'):
    filenames = listdir(data_path)

    df_partners = pd.read_excel(partners_filename)


    r = []
    for filename in filenames:
        partner_name = filename.replace('.xlsx', '').replace('[패스트몰] ', '')
        print('업체명:', partner_name)
        found_row = df_partners[df_partners['업체명'].str.contains(partner_name)]
        email1 = str(found_row['이메일1'].values[0])
        partner_manager_name = str(found_row['컨택담당자'].values[0])
        email_cc = str(found_row['참조이메일'].values[0])

        # nan이면 빈칸
        if email_cc == 'nan':
            email_cc = ''
        info = {'담당자메일':email1, '참조':email_cc, '컨텍담당자':partner_manager_name,
                '제목':title, '첨부파일명':filename
                }
        r.append(info)

        email_list = pd.DataFrame(r)
        email_list.to_excel(target_filename)
    print(f'엑셀로 저장 완료 되었습니다. 파일명:{target_filename}')


if __name__ == '__main__':
    make_email_list('data/', '파트너목록.xlsx',
                    '[패스트몰] 금일 발주 목록 입니다. 확인부탁드립니다.', 'email_list.xlsx')
