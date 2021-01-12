my_list = [13,200,1,-1,3,10,14,-12,19]
def sor_t(m_list):
    sorted_list = []
    while m_list:
        minimum = m_list[0]  # arbitrary number in list 
        for x in m_list: 
            if x < minimum:
                minimum = x
        sorted_list.append(minimum)
        m_list.remove(minimum)
    return sorted_list

print(sor_t(my_list))



        
