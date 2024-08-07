class Solution:
    def numberToWords(self, num: int) -> str:
        d = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

        def chunk_name(x):
            if x == 0:
                return None
            result = ''
            if x >= 100:
                result += f'{d[x//100]} {d[100]} '
            if x % 100 >= 20:
                result += d[(x % 100)//10*10] + ' '
                if x % 10 > 0:
                    result += d[x%10]
            elif x % 100 > 0:
                result += d[x%100]
            return result.strip()

        def parse_number(x, prefix):
            if x <= 0:
                return None
            parsed_num = parse_number(x//1000, prefix*1000)
            chunk_name_num = chunk_name(x%1000)
            if parsed_num:
                if chunk_name_num:
                    if (x // 1000) % 1000 == 0:
                        return f'{parsed_num} {chunk_name_num}'
                    return f'{parsed_num} {d[prefix*1000]} {chunk_name_num}'
                if (x // 1000) % 1000 == 0:
                    return parsed_num
                return f'{parsed_num} {d[prefix*1000]}'
            return chunk_name_num
            
        if num == 0:
            return 'Zero'
        return parse_number(num, 1).strip()




