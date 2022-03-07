def get_dict_from_singal():
    singal_dict = {}
    singal_dict['M'] = (0.8, 0.9)
    singal_dict['U'] = (0, 0.3)
    singal_dict['L'] = (0.3, 0.6)
    singal_dict['T'] = (0.6, 0.8)
    singal_dict['I'] = (0.9, 1)
    return singal_dict


def encoder(singal, singal_dict):
    Low = 0
    High = 1
    for s in singal:
        CodeRange = High - Low
        High = Low + CodeRange * singal_dict[s][1]
        Low = Low + CodeRange * singal_dict[s][0]
        print(Low, "-", s, "-", High)
    return Low


def decoder(encoded_number, singal_dict, singal_length):
    singal = []
    while singal_length:
        for k, v in singal_dict.items():
            if v[0] <= encoded_number < v[1]:
                singal.append(k)
                range = v[1] - v[0]
                encoded_number -= v[0]
                encoded_number /= range
                break
        singal_length -= 1
    return singal


singal_dict = get_dict_from_singal()
singal = 'MULTI'
print("Zakodiran string:")
ans = encoder(singal, singal_dict)
print()
singal_rec = decoder(ans, singal_dict, len(singal))
print("Dekodiran string:")
print(singal_rec)